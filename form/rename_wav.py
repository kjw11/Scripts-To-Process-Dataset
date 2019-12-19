#!/usr/bin/python
# --coding: utf-8 —**

# change several condition name.d
import os

dir = "/work9/cslt/kangjiawen/database/CN-Celeb"
#dir = "/work9/cslt/kangjiawen/scripts/test"

def main():
    names = os.listdir(dir)
    names.sort()

    for sub in ['train', 'eval']:
        print(sub)
        names = os.listdir(os.path.join(dir, sub))
        names.sort()
        for name in names:
           namedir = dir+'/'+sub+'/'+name
           wavs = os.listdir(namedir) 
           for wav in wavs:
               if 'entertain' in wav:
                   con_name, v_num, rest = wav.strip().split('-')
                   new_name = 'entertainment' + '-' + v_num + '-' + rest
                   os.rename(os.path.join(namedir, wav), os.path.join(namedir, new_name))

               if 'act' in wav:
                   con_name, v_num, rest = wav.strip().split('-')
                   new_name = 'play' + '-' + v_num + '-' + rest
                   os.rename(os.path.join(namedir, wav), os.path.join(namedir, new_name))

               if 'live' in wav:
                   con_name, v_num, rest = wav.strip().split('-')
                   new_name = 'live_broadcast' + '-' + v_num + '-' + rest
                   os.rename(os.path.join(namedir, wav), os.path.join(namedir, new_name))

               if 'tvs' in wav:
                   con_name, v_num, rest = wav.strip().split('-')
                   new_name = 'drama' + '-' + v_num + '-' + rest
                   os.rename(os.path.join(namedir, wav), os.path.join(namedir, new_name))

               if 'advertise' in wav:
                   con_name, v_num, rest = wav.strip().split('-')
                   new_name = 'advertisement' + '-' + v_num + '-' + rest
                   os.rename(os.path.join(namedir, wav), os.path.join(namedir, new_name))

               if 'recite' in wav:
                   con_name, v_num, rest = wav.strip().split('-')
                   new_name = 'recitation' + '-' + v_num + '-' + rest
                   os.rename(os.path.join(namedir, wav), os.path.join(namedir, new_name))
                 
               if 'song' in wav:
                   con_name, v_num, rest = wav.strip().split('-')
                   new_name = 'singing' + '-' + v_num + '-' + rest
                   os.rename(os.path.join(namedir, wav), os.path.join(namedir, new_name))  



if __name__ == '__main__':
    main()  
