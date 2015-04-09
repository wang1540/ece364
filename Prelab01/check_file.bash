#! /bin/bash
#$Author: ee364b09 $
#$Date: 2015-01-22 08:49:59 -0500 (Thu, 22 Jan 2015) $
#$Revision: 73453 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364b09/Prelab01/check_file.bash $
#$Id: check_file.bash 73453 2015-01-22 13:49:59Z ee364b09 $

#touch File_1
#chmod 600 File_1

if (( $# == 0 ))
then
    printf "Usage: ./check_file.bash <filename>\n"
else
    while (( $# > 0 ))
    do
	file=$1

	if [[ -e $file ]]
	then 
	    printf "%s exists\n" $file
	else
	    printf "%s does not exist\n" $file
	fi
     
	if [[ -d $file ]]
	then 
	    printf "%s is a directory\n" $file
	else
	    printf "%s is not a directory\n" $file
	fi

	if [[ -f $file ]]
	then 
	    printf "%s is an ordinary file\n" $file
	else
	    printf "%s is not an ordinary file\n" $file
	fi

	if [[ -r $file ]]
	then 
	    printf "%s is readable\n" $file
	else
	    printf "%s is not readable \n" $file
	fi

	if [[ -w $file ]]
	then 
	    printf "%s is writable\n" $file
	else
	    printf "%s is not writable\n" $file
	fi

	if [[ -x $file ]]
	then 
	    printf "%s is a executable\n" $file
	else
	    printf "%s is not executable\n" $file
	fi

	shift
    done
fi

exit 0