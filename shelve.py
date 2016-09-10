# -*- coding: utf-8 -*-

import shelve

wangzhe = dict(zip(['name','age'],['wangzhe',24]))
lijianguo = dict(zip(['name','age'],['lijianguo',25]))

if __name__ == '__main__':
    db = shelve.open('shelveDict')  #打开一个文件
    db['wangzhe'] = wangzhe   #向文件中添加内容，添加方式与给字典添加键值对相同
    db['lijianguo'] = lijianguo
    db.close()   #关闭文件

    db = shelve.open('shelveDict')  #打开文件
    print db['wangzhe']  #向从字典中获取键的方式一样读取内容
    print db['lijianguo']  #结果为{'age': 25, 'name': 'lijianguo'}
    db.close()  #关闭文件

    db = shelve.open('shelveDict')  #打开文件
    wangzhe = db['wangzhe']     #从文件中读取之前存储的对象
    wangzhe['name'] = 'wang zhe'   #直接对对象进行修改
    db['wangzhe'] = wangzhe     #重新存储至字典文件对象中
    print db['wangzhe']     #结果如下{'age': 24, 'name': 'wang zhe'}
    db.close()   #关闭文件