# _*_ coding: utf-8 _*_

import time
#数据结构区

BAG = {'金钥匙':0}
ROOM = {'金钥匙':1}
PLAYER_NAME = "Default"

#功能函数区
# player_input() 得到玩家输入
def player_input(info):
    print info
    player_choice = raw_input("> ")
    time.sleep(1)
    return player_choice

# update_bag() 更新玩家背包物品
def update_bag(equip_name, equip_count):
    global BAG
    if BAG[equip_name] != 0:
        BAG[equip_name] = BAG[equip_name] + equip_count
    else:
        BAG[equip_name] = equip_count

    print "你得到了%s，目前数量为%d" % (equip_name, BAG[equip_name])
    return BAG[equip_name]

# update_room() 更新屋内物品
def update_room(equip_name, equip_count):
    global ROOM
    ROOM[equip_name] = ROOM[equip_name] - equip_count

    return ROOM[equip_name]

# op_global_data() 进行全局数据的读取和修改,目前可以读取用户名，读取和修改背包物品数量
def op_global_data(typeNo,m_data,c_data):
    global PLAYER_NAME
    global BAG
    if typeNo == 1:
        if c_data == None:
            return PLAYER_NAME
        else:
            PLAYER_NAME = c_data
            return PLAYER_NAME
    elif typeNo == 2:
        if c_data == None:
            return BAG[m_data]
        else:
            update_bag(m_data,c_data)
            return BAG[m_data]
    elif typeNo == 3:
        if c_data == None:
            return ROOM[m_data]
        else:
            update_room(m_data,c_data)
            return ROOM[m_data]
    else:
        print "get_global_data() typeNO is wrong."
        exit(0)
