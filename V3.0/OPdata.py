# _*_ coding: utf-8 _*_

BAG = {'金钥匙':0}
ROOM = {'金钥匙':1}
PLAYER_NAME = "Default"

# BAG 数据操作
def get_bag_data():
    return BAG

def update_bag_data(new_bag):
    BAG = new_bag
    return BAG

# ROOM 数据操作
def get_room_data():
    return ROOM

def update_room_data(new_room):
    ROOM = new_room
    return ROOM

# PLAYER NAME 数据操作
def get_playerName_data():
    return PLAYER_NAME

def update_playerName_data(new_player):
    PLAYER_NAME = new_player
    return PLAYER_NAME
