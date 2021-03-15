# Напишите скрипт на bash, который будет искать наибольший общий делитель (НОД, greatest common divisor, GCD) двух чисел.
# При запуске ваш скрипт не должен ничего писать на экран, а просто ждет ввода двух натуральных чисел через пробел. После 
# ввода чисел скрипт считает их НОД и выводит на экран сообщение "GCD is <посчитанное значение>", например, для чисел 15 и 
# 25 это будет "GCD is 5". После этого скрипт опять входит в режим ожидания двух натуральных чисел. Если в какой-то момент 
# работы пользователь ввел вместо этого пустую строку, то нужно написать на экран "bye" и закончить свою работу.

#!/usr/bin/bash

gcd ()
{
    if [[ $1 == $2 ]]; then
        GCD=$1
    elif [[ $1 -gt $2 ]]; then
        let "A=$1-$2"
        gcd $A $2
    else
        let "A=$2-$1"
        gcd $1 $A
    fi
}

while [[ True ]]
do
    read arg1 arg2
    if [[ $arg1 == "" || $arg2 == "" ]]; then
        echo "bye"
        break
    else
        gcd arg1 arg2
        echo "GCD is $GCD"
    fi
done
