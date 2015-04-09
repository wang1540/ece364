#! /bin/bash
#$Author: ee364b09 $
#$Date: 2015-01-22 08:49:59 -0500 (Thu, 22 Jan 2015) $
#$Revision: 73453 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364b09/Prelab01/sum.bash $
#$Id: sum.bash 73453 2015-01-22 13:49:59Z ee364b09 $

#count=$#
sump=0

while (( $# != 0 ))
do
	#((count=$count-1))
	((sump=$1+$sump))
	shift
done

echo "sum of all inputs is $sump"
