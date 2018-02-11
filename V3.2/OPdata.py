# _*_ coding: utf-8 _*_

BAG = {'金钥匙':0}
ROOM = {'金钥匙':1}
PLAYER_NAME = "Default"
STATE = "000"
SAV = None

# BAG 数据操作
def get_bag_data():
    global BAG
    return BAG

def update_bag_data(new_bag):
    global BAG
    BAG = new_bag
    return BAG

# ROOM 数据操作
def get_room_data():
    global ROOM
    return ROOM

def update_room_data(new_room):
    global ROOM
    ROOM = new_room
    return ROOM

# PLAYER NAME 数据操作
def get_playerName_data():
    global PLAYER_NAME
    return PLAYER_NAME

def update_playerName_data(new_player):
    global PLAYER_NAME
    PLAYER_NAME = new_player
    return PLAYER_NAME

# STATE 数据操作
def get_state_data():
    global STATE
    return STATE

def update_state_data(new_state):
    global STATE
    STATE = new_state
    return STATE

# 存档与读取
def save(save_name):
    f=open('sav/'+ save_name +'.txt','w')
    f.write(str(PLAYER_NAME)+'\n')
    f.write(str(STATE)+'\n')
    f.write(str(BAG)+'\n')
    f.write(str(ROOM))
