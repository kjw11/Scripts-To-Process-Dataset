#!/usr/bin/python
# --coding: utf-8 —**

# change speaker name to id format, generate a dict to mapping name and id
import os

dir = "/work9/cslt/kangjiawen/database/CN-Celeb"
listdir = "/work9/cslt/kangjiawen/database/CN-Celeb"
#dir = "/work9/cslt/kangjiawen/scripts/test"
#listdir = os.getcwd()

def main():
    names = os.listdir(dir)
    names.sort()
    n = 0
    f = open(listdir+'/spkid2name', 'w')

    for sub in ['train', 'eval']:
        print(sub)
        subdir = os.path.join(dir, sub)
        names = os.listdir(subdir)
        names.sort()
        for name in names:
            new_name = 'id{:05d}'.format(n)
            f.write(new_name + ' ' + name + '\n')
            os.rename(os.path.join(subdir, name), os.path.join(subdir, new_name))
            n += 1


if __name__ == '__main__':
    main()  
