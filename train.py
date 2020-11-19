#!/usr/local/bin/python3 

import os
import time
import math
from datetime import datetime
from lib import MS

def start_task(list):
    print("start task")
    for ms in list:
        # 主選單
       ms.swipe('003b', '04c6', 3)
    for ms in list:
        # 長壓冒險
        ms.swipe('167', '402', 2, 3)
    for ms in list:
        # 關卡
        ms.swipe('14e', '2df')
    for ms in list:
        # 單人
        ms.swipe('d3', '2a9')
    for ms in list:
        # 好友
        ms.swipe('184', '204')
    for ms in list:
        # 出擊
        ms.swipe('176', '347')

def shoot(ms, angle):
    radians = (angle/180 + 1) * math.pi #反向
    length = 100
    off_x = int(math.cos(radians) * length)
    off_y = -int(math.sin(radians) * length)
    ms.swipe('24a', '24a', 2, 0, off_x, off_y);
    

def fight(list):
    print("start fight")
    for i in range(1, 31):
        if ((i+1)%10 == 0):
            print("%d-th shoot" % i)
        for ms in list:
            shoot(ms, -30)

def end(list):
    print("end")
    for i in range (1, 6):
        for ms in list:
            ms.swipe('176', '347', 3)

if __name__ == '__main__':
    ms = MS(62001)
    ms2 = MS(62027)
    obj_list = [MS(62001), MS(62026), MS(62027)]
    for i in range(1, 501):
        print("round %d" % i)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)	
        start_task(obj_list)
        time.sleep(4)
        fight(obj_list)
        end(obj_list)
        time.sleep(2)
