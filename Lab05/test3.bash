#! /bin/bash


if [[ $# != 3 ]]
then
    echo "Error: Insufficient information."
    exit 1
fi

while getopts f:-: thisopt
do
        case $thisopt in         
          f)echo $OPTARG
	    if [[ ! -e $OPTARG ]]
	    then
		echo "Error: File does not exist."
		exit 1
	    else	    
		input=$OPTARG
		output=$input'.sorted'
	    fi;;
            -)val=$(echo $OPTARG  | cut -d'=' -f2)
		#echo $val ;;
		if [[ ! $val =~ ^-?[0-9]+$ ]]
		then
		    echo "Error: Unknown option."
		    exit 1
		fi
		if [[ $val > 4 ]]
		then
		    echo "Error: Column number $val does not exist."
		    exit 1	       		
		fi;;
          *)echo "Invalid arg";;
        esac
done

if [[ ! -r $input ]]
then
    echo "Error: File not readable."
    exit
fi
while read line
do
    name=$(echo $line | cut -d' ' -f1)
    data1=$(echo $line | cut -d' ' -f2)
    data2=$(echo $line | cut -d' ' -f3)
    data3=$(echo $line | cut -d' ' -f4)
    data4=$(echo $line | cut -d' ' -f5)  
    echo "1"
    echo "$name $data1 $data2 $data3 $data4" >> $output
done < $input

exit 0

