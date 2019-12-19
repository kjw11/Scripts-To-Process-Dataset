#!/bin/bash
# Copyrigh       2017  Ignacio Viñals
#           2017-2018  David Snyder
#
# This script prepares the SITW data.  It creates separate directories
# for dev enroll, eval enroll, dev test, and eval test.  It also prepares
# multiple trials files, in the test directories, but we usually only use the
# core-core.lst list.

if [  $# != 2 ]; then
    echo "Usage: make_sitw.sh <SITW_PATH> <this_out_dir>"
    echo "E.g.: make_sitw.sh /export/corpora/SRI/sitw data"
    exit 1
fi

set -e

in_dir=`readlink -f $1`
out_dir=`readlink -f $2`

data_dir=$in_dir/data
dev_dir=$in_dir/dev
eval_dir=$in_dir/eval


if [ ! -d "$1" ]; then
    echo "$0: no such directory $dir"
    exit 1;
fi

for dir in $data_dir $dev_dir $eval_dir; do
  if [ ! -d "$dir" ]; then
    echo "$0: no such directory $dir, please check your corpus."
  fi
done

# config n_job, to make this script run in parallel
nj=20
tmp_fifofile="/tmp/$$.fifo" #pipeline file
mkfifo "$tmp_fifofile"
mkdir -p $out_dir/{train,eval_enroll,eval_test}

# associate descriptor 6 and pipeline file
# add blank line to pipeline file
exec 6<>"$tmp_fifofile"
for ((i=0;i<$nj;i++)); do echo; done >&6;

# Prepare the development data
echo "Prepare the development data"
for spkrid in `cat $dev_dir/dev.lst`; do
  read -u6  # read line from pipeline file
  {
  for utt in `ls $data_dir/$spkrid/ |sort -u | xargs -I {} basename {} .wav`; do
    uttid=${spkrid}-${utt}
    wav=$data_dir/$spkrid/$utt.wav
    echo ${uttid} ${wav} >> $out_dir/train/wav.scp
    echo ${uttid} ${spkrid} >> $out_dir/train/utt2spk
  done
  # write blank line
  echo "" >&6
  } &  # running in subshell
done

wait  # waiting for subshell
exec 6>&-  # delete descriptor

utils/fix_data_dir.sh $out_dir/train

# Prepare the enrollment data
echo "Prepare the enrollment data"
cat $eval_dir/lists/enroll.lst | \
while read line; do
  spkrid=${line:0:7}
  uttid=$spkrid-enroll
  wav=${eval_dir}/${line:15}
  echo ${uttid} ${wav} >> $out_dir/eval_enroll/wav.scp
  echo ${uttid} ${spkrid} >> $out_dir/eval_enroll/utt2spk
done
utils/fix_data_dir.sh $out_dir/eval_enroll

# Prepare the test data
echo "Prepare the test data"
cat $eval_dir/lists/test.lst | \
while read line; do
  spkrid=${line:5:7}
  uttid=${line:5:-4}
  wav=${eval_dir}/${line}
  echo "${uttid} ${wav}" >> $out_dir/eval_test/wav.scp
  echo ${uttid} ${spkrid} >> $out_dir/eval_test/utt2spk
done
utils/fix_data_dir.sh $out_dir/eval_test

# Prepare trials
echo "Prepare trials"
mkdir -p $out_dir/eval_test/trials
cat $eval_dir/lists/trials.lst | sed 's@-enroll@@g' | sed 's@test/@@g' | sed 's@.wav@@g' |\
    awk '{if ($3 == "1")
           {print $1,$2,"target"}
         else
           {print $1,$2,"nontarget"}
         }'> $out_dir/eval_test/trials/trials.lst

