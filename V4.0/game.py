# _*_ coding: utf-8 _*_
import FSM
import OPdata
import time

def start_new():
    FSM.game()

def start_load():
    print "------------------------------------"
    OPdata.load("333.txt")  
    start_new() 

def start_exit():
    exit(0)


while True:
    print "------------------------------------"
    print "欢迎你来到我的游戏世界，请选择：\n1、开始新游戏\n2、读取新游戏\n3、退出游戏"
    choice = raw_input("> ")
    if choice == "1":
        start_new()
    elif choice == "2":
        start_load()
    elif choice == "3":
        start_exit()
    else:
        print "输入错误，请重新输入"
    time.sleep(1)
