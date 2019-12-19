#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# this script is used to obtain statistical info of databasest
import os
import importlib, sys

importlib.reload(sys)
#sys.setdefaultencoding("utf-8")

dir = "/work9/cslt/kangjiawen/database/cslt-celeb/train"
#dir = "/Users/jiawenkang/Documents/cslt/Data/test_data"


entertain = {'name': 'entertain', 'uttnum': 0, 'dur': 0}
interview = {'name': 'interview', 'uttnum': 0, 'dur': 0}
song = {'name': 'song', 'uttnum': 0, 'dur': 0}
act = {'name': 'act', 'uttnum': 0, 'dur': 0}
movie = {'name': 'movie', 'uttnum': 0, 'dur': 0}
vlog = {'name': 'vlog', 'uttnum': 0, 'dur': 0}
live = {'name': 'live', 'uttnum': 0, 'dur': 0}
speech = {'name': 'speech', 'uttnum': 0, 'dur': 0}
tvs = {'name': 'tvs', 'uttnum': 0, 'dur': 0}
recite = {'name': 'recite', 'uttnum': 0, 'dur': 0}
advertise = {'name': 'advertise', 'uttnum': 0, 'dur': 0}

con_list = [entertain, interview, song, act, movie, vlog, live, speech, tvs, recite, advertise]



def seconds2time(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    time = "{}:{}:{}".format(int(h), int(m), round(s, 2))
    return time


def main():
    dir = "/work9/cslt/kangjiawen/database/cslt-celeb/train"
    names = os.listdir("/work9/cslt/kangjiawen/database/cslt-celeb/train")
    tt_names = str(len(names))
    # pass macos special file
    for name in names:
        if '.DS_Store' in name:
            continue

        wavs = os.listdir(os.path.join(dir,name))


        for wav in wavs:
            if '.DS_Store' in wav:
                continue

            # for conditions
            if 'entertain' in wav or 'entertian' in wav:           
                entertain['uttnum'] += 1
                break
        for wav in wavs:
            if 'interview' in wav or 'added' in wav or 'interiew' in wav:
                interview['uttnum'] += 1
                break
        for wav in wavs:       
            if 'song' in wav or 'music' in wav:
                song['uttnum'] += 1
                break
        for wav in wavs:
            if 'act' in wav or 'play' in wav or 'comic' in wav or 'paly' in wav:
                act['uttnum'] += 1   
                break      
        for wav in wavs:
            if 'movie' in wav or 'movies' in wav or 'moive' in wav:
                movie['uttnum'] += 1
                break
        for wav in wavs:
            if 'vlog' in wav or 'Vlog' in wav:
                vlog['uttnum'] += 1
                break
        for wav in wavs:
            if 'live' in wav:
                live['uttnum'] += 1
                break
        for wav in wavs:
            if 'speech' in wav:
                speech['uttnum'] += 1
                break
        for wav in wavs:
            if 'tvs' in wav or 'tv' in wav:
                tvs['uttnum'] += 1
                break
        for wav in wavs:
            if 'recite' in wav:
                recite['uttnum'] += 1
                break
        for wav in wavs:
            if 'advertise' in wav or 'ad' in wav:
                advertise['uttnum'] += 1
                break

    for condition in con_list:
        print(condition['name'] + ' ' + 'utts:  ' + str(condition['uttnum']) + ' ' +
                              'dur:  '+ seconds2time(condition['dur']) + '\n')
if __name__ == "__main__":
  main()
