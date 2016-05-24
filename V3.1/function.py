# _*_ coding: utf-8 _*_

import time
import OPdata

#功能函数区
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
        print "Worng!"
        exit(0)

# op_room type1:读取 type2:修改
def op_room(type, name, value):
    if type == 1:
        room = OPdata.get_room_data()
        return room[name]
    elif type == 2:
        return update_room(name,value)
    else:
        print "Worng!"
        exit(0)

# op_player none-读取 其他-更新
def op_player(name):
    if name == None:
        return OPdata.get_playerName_data()
    else:
        OPdata.update_playerName_data(name)
        return name
