#! /bin/bash
#$Author: ee364b09 $
#$Date: 2015-01-26 21:30:15 -0500 (Mon, 26 Jan 2015) $
#$Revision: 74090 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364b09/Lab01/collect_expr.bash $
#$Id: collect_expr.bash 74090 2015-01-27 02:30:15Z ee364b09 $

if [[ $# < 2 ]]
then 
    echo "usage: collect_expr.bash <output file> <input file 1> [input file 2] ... [input file N]"
    exit 1
else
    out=$1
    if [[ -e $out ]]
    then
	echo "error: output file $out already exists"
	exit 2
    else
	shift
	while (( $# != 0 ))
	do
	    if [[ ! -r $1 || ! -f $1 ]]
	    then
		echo "error: $1 is not a readable file."
		exit 2
	    fi
	    while read line
	    do
		name=$(echo $line | cut -d' ' -f1)
		data1=$(echo $line | cut -d' ' -f2)
		data2=$(echo $line | cut -d' ' -f3)
		data3=$(echo $line | cut -d' ' -f4)
		data4=$(echo $line | cut -d' ' -f5)
		data5=$(echo $line | cut -d' ' -f6)
		sum=$(( $data1 + $data2 + $data3 + $data4 + $data5 ))
		avg=$(( $sum / 5 ))
		echo "$name $data1 $data2 $data3 $data4 $data5 $sum $avg" >>$out
	    done < $1
	    #echo "$name $data1 $data2 $data3 $data4 $data5 $sum $avg	  " >out
	    shift
	done	
    fi
fi




exit 0
