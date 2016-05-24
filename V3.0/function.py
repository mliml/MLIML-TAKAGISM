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
def update_bag(equip_name, equip_count):
    bag = OPdata.get_bag_data()
    if bag[equip_name] != 0:
        bag[equip_name] = bag[equip_name] + equip_count
    else:
        bag[equip_name] = equip_count
    OPdata.update_bag_data(bag)
    print "你得到了%s，目前数量为%d" % (equip_name, bag[equip_name])

    return bag[equip_name]

# update_room() 更新屋内物品
def update_room(equip_name, equip_count):
    room = OPdata.get_room_data()
    room[equip_name] = room[equip_name] - equip_count
    OPdata.update_room_data(room)

    return room[equip_name]

# op_global_data() 进行全局数据的读取和修改,目前可以读取用户名，读取和修改背包物品数量
# 1-player_name 2-bag 3-room
def op_global_data(typeNo,m_data,c_data):
    if typeNo == 1:
        if c_data == None:
            return OPdata.get_playerName_data()
        else:
            OPdata.update_playerName_data(c_data)
            return c_data
    elif typeNo == 2:
        if c_data == None:
            bag = OPdata.get_bag_data()
            return bag[m_data]
        else:
            return update_bag(m_data,c_data)
    elif typeNo == 3:
        if c_data == None:
            room = OPdata.get_room_data()
            return room[m_data]
        else:
            return update_room(m_data,c_data)
    else:
        print "get_global_data() typeNO is wrong."
        exit(0)
