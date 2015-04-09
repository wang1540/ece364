#! /bin/bash
#$Author: ee364b09 $
#$Date: 2015-01-22 12:03:26 -0500 (Thu, 22 Jan 2015) $
#$Revision: 73516 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364b09/Prelab01/sensor_sum.sh $
#$Id: sensor_sum.sh 73516 2015-01-22 17:03:26Z ee364b09 $

if (( $# == 0 ))
then 
    echo usage: sensor_sum.sh
else
    while (($# != 0))
    do
	if [[ -r $1 ]]
	then
	    while read line
	    do
		sensorid=$(echo $line | cut -d'-' -f1)
		data1=$(echo $line | cut -d' ' -f2)
		data2=$(echo $line | cut -d' ' -f3)
		data3=$(echo $line | cut -d' ' -f4)
		sum=$(( $data1 + $data2 + $data3 ))
		echo $sensorid $sum #$data1 $data2 $data3 
	    done < $1
	else
	    echo error: $1 is not a readable file!
	fi
	echo " "
	shift
    done
fi

exit 0