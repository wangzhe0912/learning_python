# -*- coding: utf-8 -*-
import pickle

wangzhe = dict(zip(['name','age'], ['wangzhe',24]))      #得到两个字典
lijianguo = dict(zip(['name','age'], ['lijianguo',25]))
db = [wangzhe,lijianguo]   #得到一个由字典组成的列表

if __name__ == '__main__':
    dbfile = open('dbpickle','wb')   #打开一个文件，用于存储Python对象
    pickle.dump(db,dbfile)    #将对象存储至文件中
    dbfile.close()  #关闭文件

    dbfile = open('dbpickle','rb')  #打开文件
    db = pickle.load(dbfile)   #得到Python的列表
    print db
