#! /bin/bash
#$Author: ee364b09 $
#$Date: 2015-01-22 08:49:59 -0500 (Thu, 22 Jan 2015) $
#$Revision: 73453 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364b09/Prelab01/line_num.bash $
#$Id: line_num.bash 73453 2015-01-22 13:49:59Z ee364b09 $

count=$#
xy=1

if (( $count != 1))
then 
	printf "Usage: line_num.bash <filename>\n"
	exit 0
elif [[ ! -r $1 ]]
then
	printf "Cannot read %s\n" $1
else
	while read line
	do
		echo -n "$xy:"
		echo "$line"
		((xy=$xy+1))
	done < $1 
fi
exit 0
