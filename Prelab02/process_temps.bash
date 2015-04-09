#! /bin/bash
#$Author: ee364b09 $
#$Date: 2015-01-26 22:56:42 -0500 (Mon, 26 Jan 2015) $
#$Revision: 74110 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364b09/Prelab02/process_temps.bash $
#$Id: process_temps.bash 74110 2015-01-27 03:56:42Z ee364b09 $

if [[ $# = 0 ]]
then
    echo "Usage: process_temps.bash <input file>"
    exit 1
elif [[ ! -r $1 ]]
then
    echo "Error: $1 is not a readable file."
    exit 2
else
    (( len=$(wc -l $1 | cut -d' ' -f1) - 1 ))
    #echo $len
    input=$(tail -n $len $1)
    #echo "$input"
    size=$(head -n 2 $1 | tail -n 1 | wc -w)
    #echo "$size"

    for (( i=2; i<($len + 2); i++ ))
    do
	line=$(head -n $i $1 | tail -n 1)
	temp=$(echo $line | cut -d' ' -f1)
	data=0
	for (( j=2; j<=$size; j++ ))
	do
	    (( data = $data + $(echo $line | cut -d' ' -f$j) ))
	done
	((avg = $data / ($size-1) ))
	#echo "$avg"
	echo "Average temperature for time $temp was $avg C."
    done
fi
exit 0
