# _*_ coding: utf-8 _*_
import linecache

BAG = {'Gold Key':0}
ROOM = {'Gold Key':1}
PLAYER_NAME = "Default"
STATE = "000"

def save(save_name):
    f=open('sav/'+ save_name,'w')
    f.write(str(BAG))
    f.write('\n')
    f.write(str(ROOM))
    f.write('\n')
    f.write(str(PLAYER_NAME))
    f.write('\n')
    f.write(str(STATE))
    f.close

def read_sav(save_name):
#    f=open('sav/'+ save_name)
#    BAG1 = f.readlines()[0]
#    NAME1 = f.readlines()[0]
#    BAG = eval(BAG1)
#    print BAG['Gold Key']
#    print (NAME1)
    NAME1 = linecache.getline('sav/'+ save_name, 3)
    NAME1 = NAME1.strip('\n')
    print (NAME1)



#save('test')
read_sav('test')
