# -*- coding: utf-8 -*-
from qqbot import _bot as bot
from qqbot import qqbotsched
import random
import sqlite3

TMP = sqlite3.connect('REPETED_TMP.db')
cursor = TMP.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS REPETED(
                       ID      TEXT NOT NULL,
                                       WORDS    TEXT NOT NULL PRIMARY KEY );''')

def onQQMessage(bot,contact,member,content):

    if '@Repeater' in content:
        bot.SendTo(contact,'@'+member.name)
    else:
        if not getattr(member, 'uin', None) == '249215026':
            try:
                cursor.execute("INSERT INTO REPETED(ID,WORDS) VALUES('"+member.name+"','"+content+"') ")
                bot.SendTo(contact,content)
            except sqlite3.IntegrityError:
                pass
