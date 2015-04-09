#! /bin/bash
#$Author$
#$Date$
#$Revision$
#$HeadURL$
#$Id$
flag=0
while [[ $flag = 0 ]]
do
    echo -n "Enter something: "
    read haha
    echo "You entered:" $haha
    if [[ $haha = 'i' ]]
    then
	flag=1
    fi
done
STATUS=$(svn status exist.bash | head -c 1)
DATA=$(head -1 exist.bash)
echo "$STATUS"
#? M null
echo "$DATA"

FILETYPE=c
FILES=$(ls *.$FILETYPE)
echo $FILES

exit 0
