#!/bin/bash
WORDFILE="/usr/share/dict/words"
NUMWORDS=15
for i in 'seq $NUMWORDS'
do
rnum=$((RANDOM%NUMWORDS+1))
sed -n "$rnum p" $WORDFILE
done
