# --coding: utf-8 —**
# this script is used for checking one person's audios
import os 
dir="/work9/cslt/kangjiawen/database/cslt-celeb/eval/颜如晶"

wavs=os.listdir(dir)

for wav in wavs:
  wavepath = os.path.join(dir, wav)
  os.system("ffmpeg -i %s -ac 1 -ar 16000  %s" \
            % (wavepath, wavepath[:-4]+'_new.wav'))
  os.rename(wavepath[:-4]+'_new.wav', wavepath)


