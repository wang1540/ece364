#! /bin/bash
#$Author: ee364b09 $
#$Date: 2015-02-17 20:53:08 -0500 (Tue, 17 Feb 2015) $
#$Revision: 75994 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364b09/Lab05/sort.bash $
#$Id: sort.bash 75994 2015-02-18 01:53:08Z ee364b09 $

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
		if [[ $val > 4 ]]
		then
		    echo "Error: Column number $val does not exist."
		    exit 1
		fi
		if [[ $val < 0 ]]
		then
		    echo "Error: Unknown option."
		    exit 1
		fi
		sort -k $val,$val -t" " $input >> $output;;
          *)echo "Invalid arg";;
        esac
done
exit 0
