#!usr/bin/python3

# check if there is common spkr in train and eval data
import os

dir = "/work9/cslt/kangjiawen/database/cslt-celeb"

name1 = os.listdir(dir+'/train') 
name2 = os.listdir(dir+'/eval')

repeat = False
for trainer in name1:
  for evaler in name2:
    if trainer == evaler:
      print("repeat name: %s" % trainer)
      repeat = True

if not repeat:
  print("no repeat")
