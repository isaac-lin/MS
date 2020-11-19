#!/usr/local/bin/python3 

import os
import time
import math
from datetime import datetime

platform = os.environ['env']
if not platform:
    platform = 'windows'

# OS configure
TOOL = ''
DATA_DIR = ''
if platform == 'windows':
    DATA_DIR = '/home/mobaxterm/MS/data'
    TOOL = "C:\\\\Program\ Files\ \(x86\)/Nox/bin/nox_adb.exe"
else:
    HOME_DIR = '/Users/isaac_lin/'
    BASE_DIR = HOME_DIR + '/Game/MS'
    DATA_DIR = BASE_DIR + '/data'
    TOOL = '/Applications/NoxAppPlayer.app/Contents/MacOS/adb'

# Common 
APP_GAME_DIR = '/data/data/jp.co.mixi.monsterstrikeTW/'
APP_GAME_PKG = 'jp.co.mixi.monsterstrikeTW'
APP_GAME_ACTIVE_CLASS = 'jp.co.mixi.monsterstrike.MonsterStrike'


datas = ['data10.bin', 'data11.bin', 'data13.bin', 'data14.bin', 'data16.bin']

class MS(object):
    def __init__(self, port=62001):
        self.port = port
        self.server = '127.0.0.1:' + str(self.port)

    def connect(self):
        cmd = TOOL + ' connect 127.0.0.1:' + str(self.port)
        os.system(cmd)

    def disconnect(self):
        cmd = TOOL + ' disconnect 127.0.0.1:' + str(self.port)
        os.system(cmd)

    def pull(self, name):
        for data in datas:
            cmd = TOOL + ' -s %s pull %s/%s %s/%s/' % (self.server, APP_GAME_DIR, data, DATA_DIR, name)
            os.system(cmd)

    def remove(self):
        for data in datas:
            cmd = TOOL + ' -s %s shell rm -f %s/%s' % (self.server, APP_GAME_DIR, data)
            os.system(cmd)

    def push(self, name):
        for data in datas:
            cmd = TOOL + ' -s %s push %s/%s/%s %s' %s (self.server, DATA_DIR, name, data, APP_GAME_DIR)
            os.system(cmd)

    def start(self):
        cmd = TOOL + ' -s %s shell am start -n %s/%s' % (self.server, APP_GAME_PKG, APP_GAME_ACTIVE_CLASS)
        os.system(cmd)

    def stop(self):
        cmd = TOOL + ' -s %s shell am force-stop %s' % (self.server, APP_GAME_PKG)
        os.system(cmd)

    def tap(self, x, y, delay=None):
        cmd = TOOL + " shell input tap %d %d" % (self.server, int(x, 16), int(y, 16))
        os.system(cmd)
        if delay:
            time.sleep(delay)

    def swipe(self, x, y, delay=2, hold=0, off_x=1, off_y=1):
        if (hold == 0):
            cmd = TOOL + ' -s %s shell input swipe %d %d %d %d' % (self.server, int(x, 16), int(y, 16), int(x, 16) + off_x, int(y, 16) + off_y)
        else:
            cmd = TOOL + ' -s %s shell input swipe %d %d %d %d %d' % (self.server, int(x, 16), int(y, 16), int(x, 16) + off_x, int(y, 16) + off_y, hold * 1000)
        os.system(cmd)
        if delay:
            time.sleep(delay)
        pass

    def keyin(self, data):
        pass
