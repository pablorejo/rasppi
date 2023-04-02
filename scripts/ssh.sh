#!/bin/bash
source variables.sh

#Si pone algun argumento se toma este como la dirección ip 
echo $1
if [[ $1 != "d" ]]
then
set ip=$1
fi

echo "Intentando acceder"
echo "Puerto = $puerto"
echo "IP = $ip"

sshpass -p $pass ssh pi@$ip -p $puerto
