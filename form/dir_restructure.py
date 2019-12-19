#!/usr/bin/python

#this script is used to sort out dirs for cslt-celeb
#use archieve function to generate secondary dir;
#use mvout function to cancel secondary dir
import os
import glob

#dir = "/work9/cslt/kangjiawen/database/temp_data"
dir = "/work9/cslt/kangjiawen/database/cslt-celeb/eval"
scens=['entertain', 'song', 'act', 'movie', 'interview', 'vlog', 'live', 'speech', 'tvs', 'recite', 'advertise']
print(os.system("pwd"))


#generate secondary dir
def archieve(name, curdir):
    if glob.glob(os.path.join(curdir, '*.wav')):
        for scen in scens:
            if glob.glob(curdir + '/' + scen + '-*.wav'):
                os.system("cd %s && mkdir -p %s && mv $(find . -name \"%s\") %s" \
                          % (curdir, scen, scen+'-*', scen+'/'))


#cancel secondary dir
def mvout(scens, curdir):
    for scen in scens:
        if os.path.exists(curdir+'/'+scen):
        # if os.path.exists(os.path.join(curdir, scen)):
            print(os.path.join(curdir, scen))
            os.system("cd %s && mv %s/* . && rm -r %s || rm -r %s" % (curdir, scen, scen, scen))


def main():
    names = os.listdir(dir)
    for name in names:
        print(name)
        curdir = os.path.join(dir, name)
        print(curdir)
        #archieve(name, curdir)
        mvout(scens, curdir)



if __name__ == "__main__":
  main()
