# _*_ coding: utf-8 _*_

#数据结构区
STATE = 000
BAG = {'金钥匙':0}
ROOM = {'金钥匙':1}
PLAYER_NAME = "Default"

#功能函数区
# player_input() 得到玩家输入
def player_input(info):
    print info
    player_choice = raw_input("> ")
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

# get_global_data() 进行全局数据的读取和修改,目前可以读取用户名，读取和修改背包物品数量
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

# change_st() 改变状态机
def change_st(new_state):
    global STATE
    STATE = new_state

#状态机区
# 000 游戏开始状态
def st000():
    global BAG
    print "你好，欢迎你来到我的密室"
    print "不要关心你是怎么进来的"
    print "关心，"
    print "你要怎么出去"
    name = op_global_data(1,0,player_input("首先，请告诉我你的名字"))
    print "你好，%s， 祝你玩得尽兴。" % name

    change_st(001)

# 001 普通状态
def st001():
    print "你来到屋子中间，环顾四周，一扇大门紧紧锁着"

    if op_global_data(3,"金钥匙",None) != 0:
        print "屋子的角落里好像有一个闪闪发亮的东西。"
        choice = player_input("你想要做什么：\n1.看看那是什么\n2.尝试去开门\n3.什么也不做")

        if choice == "1":
            print "你向那个闪闪发亮的东西走去"
            change_st(002)
        elif choice == "2":
            print "走到了大门口"
            change_st(100)
        else:
            print "什么也没有发生"
            change_st(001)

    elif op_global_data(3,"金钥匙",None) == 0:
        choice = player_input("你想要做什么：\n1.尝试去开门\n2.什么也不做")

        if choice == "1":
            print "你走到了大门口"
            change_st(100)
        else:
            print "什么也没有发生"
            change_st(001)

# 002 拿钥匙状态
def st002():
    print "走近后发现，这是一个金色的钥匙，看起来是开门用的"
    print "你捡起了钥匙\n钥匙+1"
    op_global_data(2,"金钥匙",1)
    op_global_data(3,"金钥匙",1)

    change_st(001)

# 100 开门状态get_global_data(2,0,x)
def st100():
    print "你来到了大门前"
    choice = player_input("你想要做什么：\n1.尝试开门\n2.什么也不做")

    if choice == "1":
        if op_global_data(2,"金钥匙",None) >= 1:
            print "你打开了大门"
            print "恭喜你重获自由，再见，%s" % op_global_data(1,0,None)
            exit(0)
        else:
            print "大门紧锁"
            change_st(001)
    else:
        change_st(001)


while True:
    print "------------------------------------"
    if STATE == 000:
        st000()
    elif STATE == 001:
        st001()
    elif STATE == 002:
        st002()
    elif STATE == 100:
        st100()
    else:
        print "state WRONG!"
        exit(0)
