#! /bin/bash
#$Author: ee364b09 $
#$Date: 2015-01-27 15:16:05 -0500 (Tue, 27 Jan 2015) $
#$Revision: 74217 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S15/students/ee364b09/Lab02/sorting.bash $
#$Id: sorting.bash 74217 2015-01-27 20:16:05Z ee364b09 $

if [[ $# != 1 ]]
then
    echo "Usage: ./sorting.bash <input file>"
    exit 1
else
    if [[ ! -r $1 ]]
    then
	echo "Error: $1 is not a readable file."
	exit 2
    else
	flag=0
	echo "./sorting.bash $1"
	echo "Your choices are: "
	echo "1) First 10 people"
	echo "2) Last 5 names by highest zipcode"
	echo "3) Address of 6th-10th by reverse e-mail"
	echo "4) First 12 companies"
	echo "5) Pick a number of people"
	echo "6) Exit"
	
	while (( $flag == 0 ))
	do
	    echo -n "Your choice: "
	    read choices

	    if [[ $choices == '6' ]]
	    then
		echo "Have a nice day!"
		flag=1

	    elif [[ $choices == '1' ]]
	    then			    	       
		line=$(sort -k7,7 -k5,5 -k2,2 -k1,1 -t"," $1 | head -n 10)
		echo "$line"	    

	    elif [[ $choices == '2' ]]
	    then		
		line=$(sort -k8,8 -r -n -t"," $1 | head -n 5 | sort -n -k8,8 -t"," | cut -d',' -f1,2)	      	     
		echo "$line"
	    
	    elif [[ $choices == '3' ]]
	    then
		line=$(sort -k11,11 -r -t"," $1 | head -n 10 | tail -n 5 | cut -d',' -f4)
		echo "$line"
	    
	    elif [[ $choices == '4' ]]
	    then
		line=$(sort -k3,3 -t"," $1 | head -n 12 | cut -d',' -f3)
		echo "$line"
	    
	    elif [[ $choices == '5' ]]
	    then
		echo -n "Enter a number: "
		read num
		
		line=$(sort -k2,2 -k1,1 -t"," $1 | head -n $num)
		echo "$line"
	    else
		echo "Error! Invalid Selection!"
	    fi

	done
    fi
fi

exit 0