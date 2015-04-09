#! /bin/bash

while read line
do
	#echo "$line"
	data1=$(echo $line | cut -d'-' -f1)
	echo $data1
	#sen = $(echo $line | cut -d' ' -f2)
done < $1

#! /bin/bash

head -n 10 file
head -c 10 file
tail -n 10 file

cut -f1 file
cut -d' ' -f1-5 file
paste file1 file2 file3
paste -d ':' file1 file2

wc -lwc file
wc -L file
cat txt | wc -w
ls a* | wc -w
ls a* | cut -d'
' -f1-5 | wc -w