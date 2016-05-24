# MLIML-TAKAGISM
It's my first python game, about escaping from a room.

---

### V1.0 版本说明：

设计了最初的游戏结构

设计了游戏的基本状态机

编写了游戏的基本功能函数

#### 状态机：

000——游戏开始

001——普通状态

002——拿钥匙状态

100——开门状态

#### 功能函数：

player_input():获得玩家输入

update_bag():更新背包物品

---

### V1.1 版本说明：

更新了数据结构：将全局变量的操作集中在一个函数中。

编写了全局变量操作函数，目前可以查看、更改 player_name 和 bag 变量

将状态机的更改单独成了一个函数

#### 状态机：

000——游戏开始

001——普通状态

002——拿钥匙状态

100——开门状态

#### 功能函数：

player_input():获得玩家输入

update_bag():更新背包物品

op_global_data(typeNo,m_data,c_data):操作全局变量

change_st(new_state): 更改状态机

---

### V1.2 版本说明：

更新了数据结构：

-新增了房间物品字典，用于触发状态机

-将背包的数据结构更改为字典

编写了房间物品操作函数

更新了全局变量操作函数，目前可以查看、更改 玩家姓名，背包和房间物品

#### 状态机：

000——游戏开始

001——普通状态

002——拿钥匙状态

100——开门状态

#### 功能函数：

player_input():获得玩家输入

update_bag():更新背包物品

update_room(): 更新房间物品数量

op_global_data(typeNo,m_data,c_data):操作全局变量

change_st(new_state): 更改状态机