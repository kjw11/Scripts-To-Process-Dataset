#!/usr/bin/python
# --coding: utf-8 —**

# renumber the audio serial numebers to make them continuous
import os

dir = "/work9/cslt/kangjiawen/database/CN-Celeb"
#dir = "/work9/cslt/kangjiawen/scripts/test"

def main():
    names = os.listdir(dir)
    names.sort()

    #print(sub)
    data = "data"
    names = os.listdir(os.path.join(dir, data))
    names.sort()
    for name in names:
       namedir = dir+'/'+data+'/'+name
       wavs = os.listdir(namedir)
       wavs.sort()
       v_list = []
       con_list = []
       for wav in wavs:
           #print(name, wav)
           con_name, v_num, rest = wav.strip().split('-')
           v_name = con_name + '-' +v_num + '-' 

           if v_name not in v_list:
               v_list.append(v_name)
           if con_name not in con_list:
               con_list.append(con_name)

#           for v_name in v_list:
#               n = 1
#               for wav in wavs:
#                   if v_name in wav:
#                       rest = "{:03d}.wav".format(n)
#                       n += 1
#                       newname = v_name + rest
#                       print(name, wav, newname)
#                       os.rename(os.path.join(namedir, wav), os.path.join(namedir, newname))
           
       for con_name in con_list:
           nn = 1
           for v_name in v_list:
               if con_name in v_name:
                   new_v_name = "{}-{:02d}-".format(con_name, nn) 
                   nn += 1
                   n = 1
                   for wav in wavs:
                       if v_name in wav:
                           rest = "{:03d}.wav".format(n)
                           n += 1
                           newname = new_v_name + rest
                           print(name, wav, newname)
                           
                           os.rename(os.path.join(namedir, wav), os.path.join(namedir, newname)) 

if __name__ == '__main__':
    main()  
