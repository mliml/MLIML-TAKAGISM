# _*_ coding: utf-8 _*_

import function
import OPdata

import time


#状态机区

# 000 游戏开始状态
def st000():
    print "游戏正在启动..."
    time.sleep(1)
    print "------------------------------------"
    print "你好，欢迎你来到我的密室"
    print "不要关心你是怎么进来的"
    print "关心，"
    print "你要怎么出去"
    name = function.op_player(function.player_input("首先，请告诉我你的名字"))
    print "你好，%s，祝你玩得尽兴。" % name

    OPdata.update_state_data("001")

# 001 普通状态
def st001():
    print "你来到屋子中间，环顾四周，一扇大门紧紧锁着，角落里有一张桌子"
    choice = function.player_input("你想要做什么：\n1.看看桌子那里有什么线索\n2.走到大门前\n3.什么也不做")
    if choice == "1":
        print "你向桌子走去..."
        OPdata.update_state_data("002")
    elif choice == "2":
        print "你向大门走去..."
        OPdata.update_state_data("100")
    else:
        print "你在房间内踱步，不知道该做些什么，或许你应该冷静下来，再好好观察观察..."
        OPdata.update_state_data("001")

# 002 书桌前
def st002():
    print "你走到了桌子前，开始仔细地检查桌子的各个角落"
    print "..."
    if function.op_room(1,"金钥匙",None) >= 1:
        choice = function.player_input("你突然发现一个桌子腿下面压着一把钥匙！\n你想要做什么：\n1、拿起钥匙\n2、什么也不做")
        if choice == "1":
            print "你捡起了钥匙\n钥匙+1"
            function.op_bag(2,"金钥匙",1)
            function.op_room(2,"金钥匙",1)
        else:
            print "你在桌子前什么也没有发现，或许你应该再到别处看看..."
    else:
        print "你在桌子前什么也没有发现，或许你应该再到别处看看..."
    OPdata.update_state_data("001")

# 100 开门状态get_global_data(2,0,x)
def st100():
    print "你来到了大门前"
    choice = function.player_input("你想要做什么：\n1.试着把门打开\n2.什么也不做")

    if choice == "1":
        if function.op_bag(1,"金钥匙",None) >= 1:
            print "你打开了大门"
            print "恭喜你重获自由，再见，%s" % function.op_player(None)
            print "游戏结束..."
            OPdata.update_state_data("999")
        else:
            print "大门锁的很紧，看起来没有钥匙根本打不开"
            OPdata.update_state_data("001")
    else:
        print "你在大门前什么也没有发现，或许你应该再到别处看看..."
        OPdata.update_state_data("001")

# 999 退出状态
def st999():
    print "即将退出到游戏启动界面..."
    time.sleep(1)



def game():
    while True:
        print "------------------------------------"
        if OPdata.get_state_data() == "000":
            st000()
        elif OPdata.get_state_data() == "001":
            time.sleep(1)
            st001()
        elif OPdata.get_state_data() == "002":
            time.sleep(1)
            st002()
        elif OPdata.get_state_data() == "100":
            time.sleep(1)
            st100()
        elif OPdata.get_state_data() == "999":
            time.sleep(1)
            st999()
            OPdata.update_state_data("000")
            break
        else:
            print "state WRONG!"
            exit(0)
