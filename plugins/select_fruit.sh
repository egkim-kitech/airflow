#!/bin/bash
FRUIT=$1
if [ $FRUIT == APPLE ];then
    echo "selected APPLE"
elif [ $FRUIT == BANANA ];then
    echo "selected BANANA"
elif [ $FRUIT == GRAPE ];then
    echo "selected GRAPE"
else
    echo "Unidentified FRUIT!!"
fi
    
