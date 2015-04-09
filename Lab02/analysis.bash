#! /bin/bash
#$Author: ee364b09 $
#$Date: 2015-01-27 15:16:05 -0500 (Tue, 27 Jan 2015) $
#$Revision: 74217 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364b09/Lab02/analysis.bash $
#$Id: analysis.bash 74217 2015-01-27 20:16:05Z ee364b09 $

if [[ $# != 1 ]]
then
    echo "Usage: analysis.bash <input file>"
    exit 1
else
    if [[ ! -r $1 ]]
    then
	echo "Error: $1 is not a readable file."
	exit 2
    else
	wtt=0
	while read line
	do
	    avg=0
	    sum=0
	    a=($line)
	    (( size=${#a[*]} - 1 ))
	    #echo "$size"
	    name=${a[0]}
	    #echo "$name"
	    for (( i=2; i < $size; i++ ))
	    do
		(( sum=$sum + ${a[i]} ))		
	    done 
	    (( avg=$sum / ($size-2) ))	  
	    #echo "$avg"
	    (( nwtt=$avg/${a[$size]} ))
	    #echo "$wtt"

	    if [[ $wtt < $nwtt ]]
	    then
		wtt=$nwtt
		wttname=$name
		(( wttspeed=${a[1]} ))
	    fi
	    
	    for (( i=2; i < $size; i++ ))
	    do
		(( nine  =  (90 * $avg) / 100 ))
		#echo "$nine"
		if [[ ${a[i]} < $nine ]]		
		then
		    echo "Run 1 for $name ${a[1]} with score ${a[i]} was 90% less than average"
		fi
	    done 
	    echo "$name ${a[1]} scored an average of $avg"
	done < $1
    fi
fi

echo "The best performance per watt was achieved by $name $wttspeed at $wtt"

exit 0