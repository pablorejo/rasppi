#!/bin/bash
source variables.sh

#Si pone algun argumento se toma este como la dirección ip 
if [[ $1 != "" ]]
then
set ip=$1
fi

echo "Llendo al directorio $path"
cd $path

echo "Intentando acceder"
echo "Puerto=$puerto"
echo "IP = $ip"

sshpass -p $pass sftp -P $puerto pi@$ip
