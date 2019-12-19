#!/bin/bash

# Copyright   2014  Johns Hopkins University (author: Daniel Povey) 
#             2016  Tsinghua University (author: Dong Wang)
#             2019  Tsinghua University (author: Jiawen Kang)
# Apache 2.0

# Adapted from librispeech recipe local/download_and_untar.sh

set -e

remove_archive=false

if [ "$1" == --remove-archive ]; then
  remove_archive=true
  shift
fi

if [ $# -ne 2 ]; then
  echo "Usage: $0 [--remove-archive] <corpus-base> <url-base>"
  echo "e.g.: $0 /nfs/public/materials/data/thchs30-openslr www.openslr.org/resources/18 data_cnceleb"
  echo "With --remove-archive it will remove the archive after successfully un-tarring it."
  exit 1;
fi

data=$1
url=$2
name="wav"

if [ ! -d "$data" ]; then
  echo "$0: no such directory $data"
  exit 1;
fi

if [ -z "$url" ]; then
  echo "$0: empty URL base."
  exit 1;
fi

size="31844634248"

if [ -f $data/$name.tgz ]; then
  s=$(/bin/ls -l $data/$name.tgz | awk '{print $5}')
  size_ok=false
  if [ $s == $size ]; then size_ok=true; fi
  if ! $size_ok; then
    echo "$0: removing existing file $data/$name.tgz because its size in bytes $size"
    echo "does not equal the size of archives."
    rm $data/$name.tgz
  else
    echo "$data/$name.tgz exists and appears to be complete, untaring it."
  fi
fi

if [ ! -f $data/$name.tgz ]; then
  if ! which wget >/dev/null; then
    echo "$0: wget is not installed."
    exit 1;
  fi
  echo "$0: downloading data from $url.  This may take some time, please be patient."

  cd $data
  pwd
  echo " wget --no-check-certificate $url"
  if ! wget --no-check-certificate $url >/dev/null; then
    echo "$0: error executing wget $url"
    exit 1;
  fi
fi
cd $data

echo "untaring $name.tgz..."
if ! tar -xvzf $name.tgz >/dev/null; then
  echo "$0: error un-tarring archive $data/$name.tgz"
  exit 1;
fi

echo "$0: Successfully downloaded and un-tarred $data/$name.tgz"

if $remove_archive; then
  echo "$0: removing $data/$name.tgz file since --remove-archive option was supplied."
  rm $data/$name.tgz
fi
