#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# this script is used to obtain statistical info of databasest
import librosa
import os
import importlib, sys

importlib.reload(sys)
#sys.setdefaultencoding("utf-8")

dir = "/work9/cslt/kangjiawen/database/cslt-celeb/train"
#dir = "/Users/jiawenkang/Documents/cslt/Data/test_data"
os.system("rm -r ./statistics")
os.mkdir("./statistics")
destdir = "./statistics"


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

dur_distrb = {'<2': 0, '2-5': 0, '5-10': 0, '10-15': 0,
              '15-20': 0, '20-25': 0, '25-30': 0, '>30': 0}


def seconds2time(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    time = "{}:{}:{}".format(int(h), int(m), round(s, 2))
    return time


def main():
    tt_dur_sum = 0
    tt_nsum = 0
    p_processed = 0

    names = os.listdir(dir)
    tt_names = str(len(names))
    f = open(destdir + '/' +'name_list', 'w')
    for name in names:
        f.write(str(name) + '\n')
    persons = open(destdir + '/persons', 'w')
    # pass macos special file
    for name in names:
        if '.DS_Store' in name:
            continue

        p_dur_sum = 0
        p_nsum = 0
        p_song = 0
        wavs = os.listdir(os.path.join(dir,name))

        # pass and mark null file
        if len(wavs) == 0:
            os.system("echo %s >> %s" % (name, destdir+'/null_file'))
            continue

        for wav in wavs:
            if '.DS_Store' in wav:
                continue
            wavpath = dir + '/' + name + '/' +wav

            dur = librosa.get_duration(filename=wavpath)

            # for conditions
            if 'entertain' in wav:
                entertain['uttnum'] += 1
                entertain['dur'] += dur
            elif 'interview' in wav:
                interview['uttnum'] += 1
                interview['dur'] += dur
            elif 'song' in wav:
                song['uttnum'] += 1
                song['dur'] += dur
                p_song += 1
            elif 'act' in wav:
                act['uttnum'] += 1
                act['dur'] += dur
            elif 'movie' in wav:
                movie['uttnum'] += 1
                movie['dur'] += dur
            elif 'vlog' in wav:
                vlog['uttnum'] += 1
                vlog['dur'] += dur
            elif 'live' in wav:
                live['uttnum'] += 1
                live['dur'] += dur
            elif 'speech' in wav:
                speech['uttnum'] += 1
                speech['dur'] += dur
            elif 'tvs' in wav:
                tvs['uttnum'] += 1
                tvs['dur'] += dur
            elif 'recite' in wav:
                recite['uttnum'] += 1
                recite['dur'] += dur
            elif 'advertise' in wav:
                advertise['uttnum'] += 1
                advertise['dur'] += dur

            # for duration distribution
            if dur < 2:
                dur_distrb['<2'] += 1
            elif 2 <= dur < 5:
                dur_distrb['2-5'] += 1
            elif 5 <= dur < 10:
                dur_distrb['5-10'] += 1
            elif 10 <= dur < 15:
                dur_distrb['10-15'] += 1
            elif 15 <= dur < 20:
                dur_distrb['15-20'] += 1
            elif 20 <= dur < 25:
                dur_distrb['20-25'] += 1
            elif 25 <= dur < 30:
                dur_distrb['25-30'] += 1
            else:
                dur_distrb['>30'] += 1

            # total stats
            tt_dur_sum += dur
            tt_nsum += 1

            # personal stats
            p_dur_sum += dur
            p_nsum += 1

        p_processed += 1
        print(name + ' ' + str(p_processed) + '/' + tt_names)

        # write personal stats
        persons.write(name + ' || ' + str(p_nsum) + ' || ' + seconds2time(p_dur_sum) +
                      ' || ' + seconds2time(p_dur_sum/p_nsum) + '   ' + 'song_num' + '   ' + str(p_song) + '\n')
# again
    dir2 = "/work9/cslt/kangjiawen/database/cslt-celeb/eval"
    names = os.listdir(dir2)
    tt_names = str(len(names))
    f = open(destdir + '/' +'name_list', 'w')
    for name in names:
        f.write(str(name) + '\n')
    persons = open(destdir + '/persons', 'w')
    # pass macos special file
    for name in names:
        if '.DS_Store' in name:
            continue

        p_dur_sum = 0
        p_nsum = 0
        p_song = 0
        wavs = os.listdir(os.path.join(dir2,name))

        # pass and mark null file
        if len(wavs) == 0:
            os.system("echo %s >> %s" % (name, destdir+'/null_file'))
            continue

        for wav in wavs:
            if '.DS_Store' in wav:
                continue
            wavpath = dir2 + '/' + name + '/' +wav

            dur = librosa.get_duration(filename=wavpath)

            # for conditions
            if 'entertain' in wav:
                entertain['uttnum'] += 1
                entertain['dur'] += dur
            elif 'interview' in wav:
                interview['uttnum'] += 1
                interview['dur'] += dur
            elif 'song' in wav:
                song['uttnum'] += 1
                song['dur'] += dur
                p_song += 1
            elif 'act' in wav:
                act['uttnum'] += 1
                act['dur'] += dur
            elif 'movie' in wav:
                movie['uttnum'] += 1
                movie['dur'] += dur
            elif 'vlog' in wav:
                vlog['uttnum'] += 1
                vlog['dur'] += dur
            elif 'live' in wav:
                live['uttnum'] += 1
                live['dur'] += dur
            elif 'speech' in wav:
                speech['uttnum'] += 1
                speech['dur'] += dur
            elif 'tvs' in wav:
                tvs['uttnum'] += 1
                tvs['dur'] += dur
            elif 'recite' in wav:
                recite['uttnum'] += 1
                recite['dur'] += dur
            elif 'advertise' in wav:
                advertise['uttnum'] += 1
                advertise['dur'] += dur

            # for duration distribution
            if dur < 2:
                dur_distrb['<2'] += 1
            elif 2 <= dur < 5:
                dur_distrb['2-5'] += 1
            elif 5 <= dur < 10:
                dur_distrb['5-10'] += 1
            elif 10 <= dur < 15:
                dur_distrb['10-15'] += 1
            elif 15 <= dur < 20:
                dur_distrb['15-20'] += 1
            elif 20 <= dur < 25:
                dur_distrb['20-25'] += 1
            elif 25 <= dur < 30:
                dur_distrb['25-30'] += 1
            else:
                dur_distrb['>30'] += 1

            # total stats
            tt_dur_sum += dur
            tt_nsum += 1

            # personal stats
            p_dur_sum += dur
            p_nsum += 1

        p_processed += 1
        print(name + ' ' + str(p_processed) + '/' + tt_names)

        # write personal stats
        persons.write(name + ' || ' + str(p_nsum) + ' || ' + seconds2time(p_dur_sum) +
                      ' || ' + seconds2time(p_dur_sum/p_nsum) + '   ' + 'song_num' + '   ' + str(p_song) + '\n')


    # write conditions stats
    conditions = open(destdir + '/conditions', 'w')
    for condition in con_list:
        conditions.write(condition['name'] + ' ' + 'utts:  ' + str(condition['uttnum']) + ' ' +
                              'dur:  '+ seconds2time(condition['dur']) + '\n')

    # write total stats
    total = open(destdir + '/total', 'w')
    total.write("total utterance number:" + ' ' + str(tt_nsum) + '\n'
                + "total duration:" + seconds2time(tt_dur_sum) + '\n'
                + "average duration per utterance:" + str(tt_dur_sum/tt_nsum) + 's' + '\n'
                + "average duration per speaker:" + seconds2time(tt_dur_sum/len(names)) + '\n' +'\n')
    for key in dur_distrb:
        total.write(key + ': ' + str(dur_distrb[key]) + '\n')

    print("Finish statistics")


if __name__ == "__main__":
  main()
