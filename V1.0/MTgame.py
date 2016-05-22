# _*_ coding: utf-8 _*_

#数据结构区
state = 000
bag = [['door_key',0]]
PLAYER_NAME = "Default"

#功能函数区
# player_input() 得到玩家输入
def player_input(info):
    print info
    player_choice = raw_input("> ")
    return player_choice

# update_bag() 更新玩家背包物品
def update_bag(equip_no,equip_count):
    bag[equip_no][1] = equip_count
    return "Now you have %d %s" % (equip_count, bag[equip_no][0])

#状态机区
# 000 游戏开始状态
def st000():
    global PLAYER_NAME
    print "你好，欢迎你来到我的密室"
    print "不要关心你是怎么进来的"
    print "关心，"
    print "你要怎么出去"
    PLAYER_NAME = player_input("首先，告诉我你的名字")
    print "你好，%s， 祝你玩得尽兴。" % PLAYER_NAME


    game_state = 001
    return game_state

# 001 普通状态
def st001():
    print "你来到屋子中间，环顾四周，一扇大门紧紧锁着"

    if bag[0][1] == 0:
        print "屋子的角落里好像有一个闪闪发亮的东西。"
        choice = player_input("你想要做什么：\n1.看看那是什么\n2.尝试去开门\n3.什么也不做")

        if choice == "1":
            print "你向那个闪闪发亮的东西走去"
            game_state = 002
            return game_state
        elif choice == "2":
            print "走到了大门口"
            game_state = 100
            return game_state
        else:
            print "什么也没有发生"
            game_state = 001
            return game_state

    elif bag[0][1] >= 1:
        choice = player_input("你想要做什么：\n1.尝试去开门\n2.什么也不做")

        if choice == "1":
            print "你走到了大门口"
            game_state = 100
            return game_state
        else:
            print "什么也没有发生"
            game_state = 001
            return game_state

# 002 拿钥匙状态
def st002():
    print "走近后发现，这是一个金色的钥匙，看起来是开门用的"
    print "你捡起了钥匙\n钥匙+1"
    update_bag(0,1)
    game_state = 001
    return game_state

# 100 开门状态
def st100():
    global PLAYER_NAME
    print "你来到了大门前"
    choice = player_input("你想要做什么：\n1.尝试开门\n2.什么也不做")

    if choice == "1":
        if bag[0][1] >= 1:
            print "你打开了大门"
            print "恭喜你重获自由，再见，%s" % PLAYER_NAME
            exit(0)
        else:
            print "大门紧锁"
            game_state = 001
            return game_state
    else:
        game_state = 001
        return game_state


while True:
    print "------------------------------------"
    if state == 000:
        state = st000()
    elif state == 001:
        state = st001()
    elif state == 002:
        state = st002()
    elif state == 100:
        state = st100()
    else:
        print "State WRONG!"
        exit(0)
