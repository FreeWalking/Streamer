#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2016-03-17 15:17:51
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import livestreamer
from twitch.api import v3
from packages import vlc, irq, myQThread
import os
import sys
import re
import time
import urllib.request
import json
import base64
from static.mainWindows import Ui_MainWindow
from widgets.input_link import def_url
from widgets.twitch_setting import twitch_set
from widgets.send_msg import msg_send
from widgets.help import help_func
from widgets.favorits import favorit
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Streamer(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()
        self.setupUi(self)
        self.setStyleSheet(open('static/style.qss').read())
        self.timer = QTimer(self)

        self.palette = self.video_fr.palette()
        self.palette.setColor(QPalette.Window,
                              QColor(0, 0, 0))
        self.video_fr.setPalette(self.palette)
        self.video_fr.setAutoFillBackground(True)
        self.isPaused = False

        self.volumeSlider_hs.setValue(50)
        self.mediaplayer.audio_set_volume(50)
        self.volumeSlider_hs.setToolTip("Volume")
        self.volumeSlider_hs.valueChanged.connect(self.setVolume)

        self.actionStream.triggered.connect(self.Open_stream)
        self.actionFile.triggered.connect(self.OpenFile)
        self.exit_action.triggered.connect(lambda: exit(0))
        self.actionSettings.triggered.connect(self.Settings_menu)
        self.actionFavorit.triggered.connect(self.Favorits_chan)
        self.actionAbout.triggered.connect(self.about_prog)
        self.actionMesError.triggered.connect(self.error_msg)
        self.actionHelp.triggered.connect(self.help_view)

        self.PlayPause_btn.clicked.connect(self.PlayPause)
        self.Stop_btn.clicked.connect(self.Stop)
        self.Twitch_btn.clicked.connect(self.OpenChatBar)
        self.quality_btn.clicked.connect(self.OpenQualityPanel)
        self.send_btn.clicked.connect(self.send_message)
        self.love_btn.clicked.connect(self.addFavorit)

        self.chat_textBrowser.ensureCursorVisible()
        self.chat_enable = True
        self.Twitch_btn.setDisabled(True)
        self.quality_btn.setDisabled(True)
        self.message_textEdit.setDisabled(True)
        self.send_btn.setDisabled(True)

        self.statusbar.showMessage("© Khorark")
        self.path = 'setting.json'
        self.userpass_twitch()

        self.chatBar_tabWidget.setVisible(0)
        self.quality_cb.setVisible(0)

        self.progressSlider_hs.setToolTip("Position")
        self.progressSlider_hs.setMaximum(1000)
        self.progressSlider_hs.sliderMoved.connect(self.setPosition)

        self.timer = QTimer(self)
        self.timer.setInterval(200)
        self.timer.timeout.connect(self.updateUI)
        self.quality_cb.currentIndexChanged.connect(self.Change_quality)

    def userpass_twitch(self):
        try:
            self.data = json.load(open(self.path))
            self.username = self.data['Username']
            userkey = self.data['Password']
            userkey = base64.b64decode(userkey)
            self.userkey = userkey.decode('utf-8')
        except FileNotFoundError:
            print("File with settings not found")
        except TypeError:
            print("Error type file")
        except KeyError:
            print("In file settings user and pass not set")


    def about_prog(self):
        self.messageBox(
            'Streamer v.1.0 <br> Copyright © 2016 <br> Автор: Khorark <br> Мой GitHub: https://github.com/khorark')

    def error_msg(self):
        msg_err = msg_send.Msg_send()
        if msg_err.exec_():
            pass

    def help_view(self):
        hp = help_func.Help_class()
        if hp.exec_():
            pass

    def Favorits_chan(self):
        fav = favorit.Favorits()
        if fav.exec_():
            try:
                self.url_link = fav.favlist_listWidget.currentItem().text()
                self.processing_stream()
            except AttributeError:
                print('Адрес стрима не задан')

    def addFavorit(self):
        try:
            if self.data['favorit']:
                pass
        except AttributeError:
            self.data = {}
            self.data['favorit'] = []
            #json.dump(self.data, open(self.path, 'w'))
            print ('KeyError maybe )')

        self.data['favorit'].append(self.url_link)
        json.dump(self.data, open(self.path, 'w'))
        self.love_btn.setDisabled(True)

    def OpenChatBar(self):
        if self.chatBar_tabWidget.isVisible():
            self.chatBar_tabWidget.setVisible(0)
            self.Twitch_btn.setIcon(QIcon(":/icons/icons/twitch_on.png"))
        else:
            self.chatBar_tabWidget.setVisible(1)
            self.Twitch_btn.setIcon(QIcon(":/icons/icons/twitch_off.png"))

    def OpenQualityPanel(self):
        if self.quality_cb.isVisible():
            self.quality_cb.setVisible(0)
            self.quality_btn.setIcon(QIcon(":/icons/icons/quality_on.png"))
        else:
            self.quality_cb.setVisible(1)
            self.quality_btn.setIcon(QIcon(":/icons/icons/quality.png"))

    def keyPressEvent(self, qKeyEvent):
        if qKeyEvent.key() == Qt.Key_Return:
            print('Message send')
            self.send_message()
        else:
            super().keyPressEvent(qKeyEvent)

    def mouseDoubleClickEvent(self, event):
        if self.isFullScreen():
            self.showNormal()
            self.menubar.show()
            self.statusbar.show()
            self.PlayPause_btn.show()
            self.Stop_btn.show()
            self.volume_label.show()
            self.volumeSlider_hs.show()
            self.quality_btn.show()
            self.Twitch_btn.show()
            self.progressSlider_hs.show()
            self.label.show()
            print('Normal')
        else:
            self.showFullScreen()
            self.menubar.hide()
            self.chatBar_tabWidget.hide()
            self.statusbar.hide()
            self.PlayPause_btn.hide()
            self.Stop_btn.hide()
            self.volume_label.hide()
            self.volumeSlider_hs.hide()
            self.quality_btn.hide()
            self.quality_cb.hide()
            self.Twitch_btn.hide()
            self.progressSlider_hs.hide()
            self.label.hide()

            print('FullScreen')

    def Change_quality(self):
        qual = self.quality_cb.currentText()
        qual = qual.lower()
        try:
            stream = self.streams[qual]
            self.Stop()
            filename = stream.url
            self.construct_video(filename)
        except AttributeError:
            print("Это не стрим. Нельзя изменить качество видео.")

    def Settings_menu(self):
        twitch_userpass = twitch_set.Twitch_set()
        if twitch_userpass.exec_():
            self.messageBox('Данные успешно сохранены')

    def Open_stream(self):
        self.chat_textBrowser.clear()
        name = def_url.Input_stream()
        if name.exec_():
            self.url_link = name.url_stream_le.text()
            self.processing_stream()

    def processing_stream(self):
        reg_twitch = 'http[s]?://www.twitch.tv/(\w+)'
        reg_link = 'http[s]?://.+'
        if self.url_link:
            if re.match(reg_twitch, self.url_link) is not None:
                chan_name = re.match(reg_twitch, self.url_link).group(1)
                print(chan_name)
                try:
                    if self.url_link in self.data['favorit']:
                        self.love_btn.setDisabled(True)
                except AttributeError:
                    print ("Favorits channel not found")

                self.statusbar.showMessage("Получение адреса стрима...")
                self.streams = livestreamer.streams(self.url_link)
                qual = self.quality_cb.currentText()
                qual = qual.lower()
                try:
                    stream = self.streams[qual]
                    self.statusbar.showMessage(
                        "Устновка качества видео...")
                    filename = stream.url
                    self.channel = chan_name
                    self.construct_video(filename)
                    self.newThreads(filename, chan_name)
                except KeyError:
                    self.messageBox("Извените, но данный канал оффлайн")
            if re.match(reg_link, self.url_link) is not None:
                # self.construct_video(url_link)
                pass
            else:
                self.messageBox("Пожалуйста введите адрес стрима")

    def newThreads(self, filename, chan_name):
        self.threads = []
        t1 = myQThread.MyThread(self.get_messages, (chan_name,), name="First")
        self.threads.append(t1)

        t2 = myQThread.MyThread(self.get_channel_info,
                                (chan_name, ), name="Two")
        self.threads.append(t2)

        # t3 = myQThread.MyThread(self.construct_video,
        #                        (filename,), name="Three")
        # self.threads.append(t3)

        for i in range(len(self.threads)):
            self.threads[i].start()

    def messageBox(self, msg):
        QMessageBox.question(
            self, 'Message', msg, QMessageBox.Ok)

    def get_messages(self, chan_name):
        try:
            nick = self.username
            uspass = self.userkey
            self.message_textEdit.setDisabled(False)
            self.send_btn.setDisabled(False)
            for mess in irq.Chat_bot(chan_name, nick, uspass).main():
                time.sleep(1)
                self.chat_textBrowser.append("{}".format(mess))
                self.chat_textBrowser.moveCursor(QTextCursor.End)

        except AttributeError:
            print('Username и Password не заданы')

    def send_message(self):
        try:
            nick = self.username
            uspass = self.userkey
            chan_name = self.channel
            msg = self.message_textEdit.toPlainText()
            self.message_textEdit.clear()
            if msg and self.channel:
                chan = "#{}".format(self.channel)
                irq.Chat_bot(chan_name, nick, uspass).send_message(chan, msg)
        except AttributeError:
            print('Username и Password не заданы')

    def get_channel_info(self, chan_name):
        self.statusbar.showMessage("Получение информации о канале...")
        self.quality_btn.setDisabled(False)
        self.Twitch_btn.setDisabled(False)
        if os.path.exists("temp") == False:
            os.mkdir("temp")

        channel = v3.channels.by_name(chan_name)

        self.setWindowTitle(channel['status'])
        chan_banner = "temp/{}.png".format(chan_name)
        if os.path.exists(chan_banner) == False:
            urllib.request.urlretrieve(channel['logo'], chan_banner)

        pix = QPixmap(chan_banner)
        self.banner_channel_lb.setPixmap(pix)

        self.game_channel_lb.setText(channel['game'])
        self.folowers_channel_lb.setText(str(channel['followers']))
        self.partner_channel_lb.setText(str(channel['partner']))
        self.views_channel_lb.setText(str(channel['views']))
        self.language_channel_lb.setText(channel['language'])

        time.sleep(0.5)
        self.statusbar.showMessage("Готово!")
        time.sleep(2)
        self.statusbar.showMessage("© Khorark")

    def OpenFile(self):
        """Open a media file in a MediaPlayer
        """
        try:
            for i in range(len(self.threads)):
                self.threads[i].terminate()
                self.threads[i].wait()
        except AttributeError:
            pass

        filename = QFileDialog.getOpenFileName(
            self, "Open File", os.path.expanduser('~'))

        if filename[0]:
            if sys.version < '3':
                filename = unicode(filename)

            self.construct_video(filename[0])

    def construct_video(self, filename):
        self.media = self.instance.media_new(filename)
        self.mediaplayer.set_media(self.media)

        self.media.parse()
        reg_title = "http[s]?://.+"
        if re.match(reg_title, filename) is None:
            self.setWindowTitle(self.media.get_meta(0))
            self.check_filename = True
            self.Twitch_btn.setDisabled(True)
            self.quality_btn.setDisabled(True)
            self.chatBar_tabWidget.setVisible(0)

        else:
            self.check_filename = False

        if sys.platform.startswith('linux'):  # for Linux using the X Server
            self.mediaplayer.set_xwindow(self.video_fr.winId())
        elif sys.platform == "win32":  # for Windows
            self.mediaplayer.set_hwnd(self.video_fr.winId())
        elif sys.platform == "darwin":  # for MacOS
            self.mediaplayer.set_nsobject(self.video_fr.winId())
        self.PlayPause()

    def PlayPause(self):
        print("Start Play/Pause module")
        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()
            self.PlayPause_btn.setIcon(QIcon(":/icons/icons/play.png"))
            self.isPaused = True
        else:
            if self.mediaplayer.play() == -1:
                self.OpenFile()
                return
            self.mediaplayer.play()
            self.PlayPause_btn.setIcon(QIcon(":/icons/icons/pause.png"))
            if self.check_filename:
                self.timer.start()
            self.isPaused = False

    def Stop(self):
        """Stop player
        """
        self.PlayPause_btn.setIcon(QIcon(":/icons/icons/play.png"))
        self.mediaplayer.stop()

    def setVolume(self):
        """Set the volume
        """
        Volume = self.volumeSlider_hs.value()
        self.mediaplayer.audio_set_volume(Volume)
        if Volume == 0:
            self.volume_label.setPixmap(
                QPixmap(":/icons/icons/volume_off.png"))
        elif Volume < 25:
            self.volume_label.setPixmap(
                QPixmap(":/icons/icons/volume_25.png"))
        elif Volume < 50:
            self.volume_label.setPixmap(
                QPixmap(":/icons/icons/volume_50.png"))
        elif Volume < 75:
            self.volume_label.setPixmap(
                QPixmap(":/icons/icons/volume_75.png"))
        else:
            self.volume_label.setPixmap(
                QPixmap(":/icons/icons/volume_100.png"))

    def setPosition(self, position):
        """Set the position
        """
        self.mediaplayer.set_position(position / 1000.0)

    def updateUI(self):
        """updates the user interface"""
        self.progressSlider_hs.setValue(self.mediaplayer.get_position() * 1000)

        if not self.mediaplayer.is_playing():
            self.timer.stop()
            if not self.isPaused:
                self.Stop()


if __name__ == '__main__':
    app = QApplication([])
    w = Streamer()
    w.show()
    # w.resize(640, 480)
    app.exec_()
