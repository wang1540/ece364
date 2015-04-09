#! /bin/bash
#$Author: ee364b09 $
#$Date: 2015-01-22 14:04:36 -0500 (Thu, 22 Jan 2015) $
#$Revision: 73527 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364b09/Prelab01/svncheck.bash $
#$Id: svncheck.bash 73527 2015-01-22 19:04:36Z ee364b09 $

flag=0

exec 3< file_list
while read line <&3
do
    echo "$line"
    
    if [[ -e $line ]]
    then
	STATUS=$(svn status $line | head -c 1)
	echo "$STATUS"
	if [[ $STATUS == '?' ]]
	then
	    if [[ -x $line ]]
	    then
		svn add $line
	    else
		flag=0
		while [[ $flag == 0 ]]
		do
		    echo "would you like to execute $line? enter y or n: "
		    read haha
		    echo "you entered:" $haha	
		#while [[ $haha != 'y' ]] || [[$haha != 'n' ]]
		#do		
		#    echo "error, please enter y or n"
		#    read haha
		#    echo "you entered:" $haha
		#done
		#read -p "Enter 'y' if you want to make $line" haha
		    if [[ $haha == 'y' ]]
		    then
			flag=1
			chmod +x $line
			svn add $line		    
		    fi
		    if [[ $haha == 'n' ]]
		    then	   
			flag=1
			svn add $line		   
		    fi
		done
	    fi
	fi
	if [[ $STATUS != '?' ]] && [[ -x $line ]]
	then 
	    svn propset svn:executable ON $line
	fi
    else
	printf "Error: File %s appears to not exist here or in svn.\n" $line
    fi
    
done
svn commit
echo "Autocommitting code"

exit 0