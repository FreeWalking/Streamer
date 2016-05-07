#!/usr/bin/env python3

import re
import socket
import random


class Chat_bot():
    """docstring for Chant_bot"""

    def __init__(self, CHAN, USER, PASS):

        # --------------------------------------------- Start Settings --------
        # Hostname of the IRC-Server in this case twitch's
        self.HOST = "irc.twitch.tv"
        self.PORT = 6667                                     # Default IRC-Port
        # Channelname = #{Nickname}
        self.CHAN = '#{}'.format(CHAN)
        print('this is CHAN', self.CHAN)
        # Nickname = Twitch username
        self.NICK = USER
        self.PASS = PASS
        print('This is user', USER)
        print('Password = ', PASS)
        #self.NICK = "Atom_love_blonde"
        # www.twitchapps.com/tmi/ will help to retrieve the required authkey
        #self.PASS = "oauth:ax5t4imm7xt0b4ts7xi6ff4b0wuleo"
        # --------------------------------------------- End Settings ----------

    # def connect(self):
        self.con = socket.socket()
        self.con.connect((self.HOST, self.PORT))
        self.send_pass(self.PASS)
        self.send_nick(self.NICK)
        self.join_channel(self.CHAN)
        print('This IRQ client')
    # --------------------------------------------- Start Functions ----------

    def send_pong(self, msg):
        self.con.send(bytes('PONG %s\r\n' % msg, 'UTF-8'))

    def send_message(self, chan, msg):
        self.con.send(bytes('PRIVMSG %s :%s\r\n' % (chan, msg), 'UTF-8'))

    def send_nick(self, nick):
        self.con.send(bytes('NICK %s\r\n' % nick, 'UTF-8'))

    def send_pass(self, password):
        self.con.send(bytes('PASS %s\r\n' % password, 'UTF-8'))

    def join_channel(self, chan):
        self.con.send(bytes('JOIN %s\r\n' % chan, 'UTF-8'))

    def part_channel(self, chan):
        self.con.send(bytes('PART %s\r\n' % chan, 'UTF-8'))
    # --------------------------------------------- End Functions ------------

    # --------------------------------------------- Start Helper Functions ---
    def get_sender(self, msg):
        result = ""
        for char in msg:
            if char == "!":
                break
            if char != ":":
                result += char
        return result

    def get_message(self, msg):
        result = ""
        i = 3
        length = len(msg)
        while i < length:
            result += msg[i] + " "
            i += 1
        result = result.lstrip(':')
        return result

    def parse_message(self, msg):
        if len(msg) >= 1:
            msg = msg.split(' ')
    # --------------------------------------------- End Helper Functions -----

    # --------------------------------------------- Start Command Functions --
    def command_send(self, message):
        if message:
            self.send_message(self.CHAN, message)

    # --------------------------------------------- End Command Functions ----

    def main(self):
        data = ""
        color = ['ff9000', 'ff0000', '00cc00', '3c13af',
                 'cc0074', 'fefe00', 'cc0073', 'febd00', '9bec00']
        while True:
            try:
                data = data + self.con.recv(1024).decode('UTF-8')
                data_split = re.split(r"[~\r\n]+", data)
                data = data_split.pop()

                for line in data_split:
                    line = str.rstrip(line)
                    line = str.split(line)

                    if len(line) >= 1:
                        if line[0] == 'PING':
                            self.send_pong(line[1])

                        if line[1] == 'PRIVMSG':
                            sender = self.get_sender(line[0])
                            message = self.get_message(line)
                            self.parse_message(message)
                            yield('<b><font color="#' + random.choice(color) + '">' + sender + '</font></b>' + ": " + message)

            except socket.error:
                print("Socket died")

            except socket.timeout:
                print("Socket timeout")


if __name__ == '__main__':
    Chat_bot().main()
