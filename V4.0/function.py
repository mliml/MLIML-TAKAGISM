# _*_ coding: utf-8 _*_

import time
import OPdata

#功能函数区

# sys_menu()
def sys_menu():
    input_st = True
    while(input_st):
        input_st = False
        print "------------------------------------"
        print "--系统菜单--"
        print "------------------------------------"
        print "Q-退出游戏\nS-保存游戏\nB-查看背包\nR-退出系统菜单"

        p_choice = raw_input("> ")

        if p_choice == "Q":
            q_choice = player_input("你是否确定要退出游戏？Y-yes，N-no")
            if q_choice == "Y":
                exit(0)
            else :
                print "请你重新选择..."
                time.sleep(1)
                input_st = True
        elif p_choice == "S":
            q_choice = player_input("你是否要保存当前记录？Y-yes，N-no")
            if q_choice == "Y":
                filename = player_input("请输入文件名")
                print "正在保存中..."
                OPdata.save(filename)
                time.sleep(2)
                print "记录已保存。"
                input_st = True
            else:
                print "请你重新选择..."
                time.sleep(1)
                input_st = True
        elif p_choice == "B":
            print "你的背包有如下物品"
            print "--------你的背包--------\n"
            bag = OPdata.get_bag_data()
            for key, value in bag.items():
                print key ,"*", value
            print "\n--------你的背包--------"
        elif p_choice == "R":
            print "..."
        else:
            print "我读不懂你的输入，请重新输入。"
            input_st = True
    print "正在返回之前的游戏，请等待"
    print "------------------------------------"
    time.sleep(3)


# error(reason)
def error_deal(def_name, reason):
    print "---------------!!!!!---------------"
    print "There are some ERRORS"
    print def_name
    exit(0)
    print "---------------!!!!!---------------"

# output_handle(choice)
def output_handle(choice,count):
    print "你想要做什么？"
    print "X、系统菜单"

    no = 1
    while(count > 0):
        st = '%s' % no
        print "%d、%s" % (no, choice[st])
        count -= 1
        no += 1

# input_handle(choice)
def input_handle(bg, choice, count):
    input_st = True
    print bg
    while(input_st):

        output_handle(choice,count)
        player_choice = raw_input("> ")

        no = 1
        no2 = count

        # 判断用户输入，如果是 X 执行系统菜单，如果是剧情选择的序号，则返回给状态机相应序号
        # 如果都不是，则让用户重新输入
        if player_choice == "X":
            sys_menu()
        else:
            while(no2 > 0):
                st = '%s' % no
                if player_choice == st:
                    input_st = False
                    return player_choice
                else:
                    no2 -= 1
                    no += 1
        # 判断是否要重新进行一遍这个循环，可能是输入错误，可能是结束了系统菜单
        if input_st:
            print "请重新输入。"
            print "------------------------------------"
            print bg
            time.sleep(1)
        else:
            time.sleep(1)

    return player_choice

# player_input() 得到玩家输入
def player_input(info):
    print info
    player_choice = raw_input("> ")
    time.sleep(1)
    return player_choice

# update_bag() 更新玩家背包物品
def update_bag(name, value):
    bag = OPdata.get_bag_data()
    if bag[name] != 0:
        bag[name] = bag[name] + value
    else:
        bag[name] = value
    OPdata.update_bag_data(bag)
    print "你得到了%s，目前数量为%d" % (name, bag[name])

    return bag[name]

# update_room() 更新屋内物品
def update_room(name, value):
    room = OPdata.get_room_data()
    room[name] = room[name] - value
    OPdata.update_room_data(room)

    return room[name]

# op_bag type1:读取 type2:修改
def op_bag(type, name, value):
    if type == 1:
        bag = OPdata.get_bag_data()
        return bag[name]
    elif type == 2:
        return update_bag(name,value)
    else:
        error_deal("op_bag", "illegal input")

# op_room type1:读取 type2:修改
def op_room(type, name, value):
    if type == 1:
        room = OPdata.get_room_data()
        return room[name]
    elif type == 2:
        return update_room(name,value)
    else:
        error_deal("op_bag", "illegal input")

# op_player none-读取 其他-更新
def op_player(name):
    if name == None:
        return OPdata.get_playerName_data()
    else:
        OPdata.update_playerName_data(name)
        return name
