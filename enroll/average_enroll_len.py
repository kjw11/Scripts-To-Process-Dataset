#!usr/bin/python
# --coding: utf-8 —**

# this is a inner script of subdata_by_dur.sh, which obtain a bash function
import sys
import os
from random import shuffle


def sub_set(srcdir):
    f = open(srcdir+'/spk2utt', 'r')
    spk2utt = f.readlines()
    f.close()
    f = open(srcdir+'/feats_vad.ark', 'r')
    scp = f.readlines()
    f.close()
    sum = 0
    for spk_line in spk2utt:
        name = spk_line.strip().split()[0]
        utts = spk_line.strip().split()[1:]
        print("%s" % name)
        for utt in utts:
            for utt_line in scp:
                if  utt_line.strip().split()[0]== utt:
                    wavdir = utt_line.strip().split()[1]
                    dur = os.popen('soxi -D %s' % wavdir).read()
                    sum += float(dur.strip())
                    break
    f.close()
    print(sum)

def sub_set_vad(srcdir):
    f = open(srcdir+'/spk2utt', 'r')
    spk2utt = f.readlines()
    f.close()
    f = open(srcdir+'/feats_vad.ark', 'r')
    scp = f.readlines()
    f.close()
    sum = 0
    for spk_line in spk2utt:
        name = spk_line.strip().split()[0]
        utts = spk_line.strip().split()[1:]
        print("%s" % name)
        for utt in utts:
            for utt_line in scp:
                if  utt_line.strip().split()[0]== utt:
                    wavlen = utt_line.strip().split()[1]
                    sum += int(wavlen)
                    break
    f.close()
    print(sum)

def main():
    #srcdir = sys.argv[1]
    #desdir = sys.argv[2]
    srcdir = "/work9/cslt/kangjiawen/cslt-celeb/egs/i-vector/data/data/eval_enroll"
    #sub_set(srcdir)
    sub_set_vad(srcdir)

if __name__ =="__main__":
    main()
