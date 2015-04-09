#! /bin/bash
#$Author: ee364b09 $
#$Date: 2015-01-22 17:12:18 -0500 (Thu, 22 Jan 2015) $
#$Revision: 73543 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364b09/Lab01/mini_shell.bash $
#$Id: mini_shell.bash 73543 2015-01-22 22:12:18Z ee364b09 $

flag=0

while [[ $flag == 0 ]]
do
    echo -n "Enter a command: "
    read com
    
    if [[ $com == 'hello' ]]
    then
	echo "Hello $(whoami)"
    elif [[ $com == 'quit' ]]
    then 
	echo "Exiting..."
	((flag = 1))
    elif [[ $com == 'compile' ]]
    then
	echo -n "Enter filename: "
	read filename
	if [[ -r $filename ]]
	then
	    gcc -Wall -Werror $filename
	    if [[ $? == 0 ]]
	    then
		echo "Compilation succeeded"
	    else
		echo "Compilation failed"
	    fi
	else
	    echo "That file does not exist"
	fi
    else
	echo "Error: Unrecognized input"
    fi
done

exit 0
