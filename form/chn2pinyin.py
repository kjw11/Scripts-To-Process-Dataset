#!/usr/bin/python
# --coding: utf-8 —**
#this script is used to convert Chinese filename into pinyin

import os
from xpinyin import Pinyin

p = Pinyin()
#dir = "/work9/cslt/kangjiawen/database/part3-1"
listdir = "/work9/cslt/kangjiawen/database/CN-Celeb/spkid2name"
destdir = "/work9/cslt/kangjiawen/database/CN-Celeb/spkid2name_plus_pinyin"
tempdir = "/work9/cslt/kangjiawen/database/CN-Celeb/temp"
#file_name = os.listdir(dir)


def convert_dir():
    for name in file_name:
      print(name)
      p_name = p.get_pinyin(name, '')
      print(p_name)
      os.rename(dir+'/'+name, dir+'/'+p_name)


def convert_list():
    f = open(listdir, 'r')
    dest_f = open(destdir, 'w')
    temp = open(tempdir, 'w')
    for line in f.readlines():
        cn_name, id = line.strip().split()
        piny_name = p.get_pinyin(cn_name, '')
        dest_f.write(id + ' ' +cn_name + ' ' +piny_name + '\n')
        temp.write(id + ' ' +cn_name + '\n')

if __name__ == '__main__':
    convert_list()

