#! /bin/bash
#$Author: ee364b09 $
#$Date: 2015-01-22 08:49:59 -0500 (Thu, 22 Jan 2015) $
#$Revision: 73453 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364b09/Prelab01/exist.bash $
#$Id: exist.bash 73453 2015-01-22 13:49:59Z ee364b09 $

while (( $# != 0 ))
do
    FILENAME=$1
    [[ -r $FILENAME ]]
    fread=$?
    [[ -e $FILENAME ]]
    fexist=$?
    
    if (( $fread == 0 ))
    then 
	printf "File %s is readable\n" $FILENAME
    elif (( $fexist == 1 ))
    then
	touch $FILENAME
    fi
    shift
done
exit 0

