#!/bin/bash

#HamHeat	:	A fast and simple package for calculating Hamming distance from multiple allelic sequence data for heatmap visualization
#Authors	:	Alexey V. Rakov & Emilio Mastriani
#Copyright	:	(C) 2020
#Version	:	1.0
#Usage		:	hamheat.sh data_file

data_filename=$1
tmp_out1=$data_filename"_tmpout1.txt"
testout1=$data_filename"_test_out1.txt"
output1=$data_filename"_output1.txt"
output1_idx=$output1"_idx.txt"
data_file_inverted=$data_filename"_inverted.txt"
final_out1=$data_filename"_finalout1.txt"
out2=$data_filename"_out2.txt"
logfile=$data_filename".log"
out3=$data_filename"_out3.txt"


echo -e "Going to analyze the file $data_filename \n"

dos2unix $data_filename

awk 'BEGIN {printf("Seq.\tFreq.\n")} { A[$2]++ } END { for(X in A) printf("%s\t%3d\n", X, (A[X])) }' $data_filename > $tmp_out1

python read_file_param.py $tmp_out1 $testout1 $output1

#insert index
awk 'BEGIN {i=1} {print $1 "\t" i++ "\t" $2}' $output1 > $output1_idx

awk '{print $2 "\t" $1}' $data_filename > $data_file_inverted

awk  -v  out1=$output1_idx 'BEGIN { while (getline < out1) { f[$1] = $2; g[$1] = $3 } } {print $0, "\t",  f[$1], "\t", g[$1] }' $data_file_inverted > $final_out1

python find_diff_param.py  $output1_idx $out2 $logfile

python prepare_last_layout_param.py $out2 $data_filename $out3