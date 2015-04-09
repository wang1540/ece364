#! /bin/bash

arr=(1 2 3 hello)
brr=()
echo ${arr[0]}
echo ${arr[*]}
echo ${#arr[*]}
arr[0]=9
echo ${!arr[*]}

vals="afeae"
arr=$vals
set $vals

echo $1 $2 ...


for I in ${A[*]}
do
    echo "$I"
done


in=$1
out=$2
for (( i=1; i<=10; i++ ))
do
    line=$(head -n $i $in| tail -n 1)
    echo "$line" >> $2
done

for (( i=6; i<=10; i++ ))
do
    line=$(head -n $i $in| tail -n 1)
    echo "$line"
done
exit 0