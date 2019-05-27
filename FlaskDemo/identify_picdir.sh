#!/bin/bash
list_dir(){
for file in `ls $1`
do
    if [ -d $1"/"$file ]
    then
    list_dir $1"/"$file
    else
    #echo $1$file
    cp $1/$file ./result/
    fi
done
}
list_dir $1