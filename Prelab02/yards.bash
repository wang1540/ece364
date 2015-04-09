#! /bin/bash
#$Author: ee364b09 $
#$Date: 2015-01-26 22:56:42 -0500 (Mon, 26 Jan 2015) $
#$Revision: 74110 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364b09/Prelab02/yards.bash $
#$Id: yards.bash 74110 2015-01-27 03:56:42Z ee364b09 $

if [[ $# != 1 ]]
then
    echo "Usage: yards.bash <filename>"
    exit 1
else
    if [[ ! -r $1 ]]
    then
	echo "Error: $1 is not readable"
	exit 2
    else
	max=0
	while read line
	do
	    var=0
	    sum=0
	    txt=($line)
	    (( size=${#txt[*]} - 1 ))
	    #echo "$size"
	    #echo "new line"
	    for (( i=1; i <= $size; i++ ))
	    do
		((sum=$sum+${txt[i]}))		
	    done
	    ((avg=$sum/$size))
	    #echo "$avg"
	    for (( i=1; i<= $size; i++ ))
	    do
		(( var=$var+(${txt[i]}-$avg)**2 ))
	    done

	    name=$(echo $line | cut -d' ' -f1)
	    (( x=$var/$size ))
	    #echo "$x"
	    
	    echo "$name schools averaged $avg yards receiving with a variance of $x"

	    if [[ $max < $avg ]]
	    then
		max=$avg
	    fi
	done < $1
	echo "The largest average yardage was $max"
    fi
fi

exit 0
