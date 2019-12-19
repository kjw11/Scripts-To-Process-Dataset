#!/udr/bin/python
# --coding: utf-8 —**
#this script is used to transform mp4 file into wav file
#defaully set sample frequency as 16k, cannel num as 1

import sys
import os
import glob
import wave
# import ffmpeg as ff

desdir="/work9/cslt/kangjiawen/database/cslt-celeb/eval"


def mp42wav(curdir):
    files = os.listdir(curdir)
    for file in files:
        os.system("ffmpeg -y -i %s -ac 1 -ar 16000  %s && rm %s" % (os.path.join(curdir,file),\
                                        os.path.join(curdir, file[:-4]+'.wav'),\
                                        os.path.join(curdir, file)))
        print("transform %s into %s" % (file, file[:-4]+'.wav'))


def check_audio(curdir, wavs):
    for wav in wavs:
        wavepath = os.path.join(curdir, wav)
        print wavepath
        #get the params of each wav file
        f = wave.open(wavepath, 'rb')
        params = f.getparams()
        f.close()

        #check nchannel and sample frequency
        if (params[0] != 1) or (params[2] != 16000):
            os.system("ffmpeg -i %s -ac 1 -ar 16000  %s" \
                                             % (wavepath, wavepath[:-4]+'_new.wav'))
            os.rename(wavepath[:-4]+'_new.wav', wavepath)
            print("modify parameters for %s" % (wavepath))


def main():
    names = os.listdir(desdir)
    # os.remove("name.log")
    pass_flag = 1
    for name in names:
        #if pass_flag==1 and name != '秦海璐':
        #    print("pass %s" % name)
        #    continue
        #else:
        #    pass_flag = 0
        #    print("find 秦海璐")
        #os.system("echo %s >> name_part2.log" % (name))
        curdir = os.path.join(desdir, name)
        # if any wav file already exist, delete all mp4 files; otherwise transform mp4 to wav
        wavs = glob.glob(os.path.join(curdir,"*.wav"))
        if wavs:
            check_audio(curdir, wavs)
            for file in glob.glob(os.path.join(curdir,"*.mp4")):
                os.remove(os.path.join(curdir, file))
                print("delete %s" % (file))
        else:
            mp42wav(curdir)
    print("Finish all data modification!")


if __name__ == "__main__":
    main()
