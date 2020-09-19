#!/bin/bash

aptitude install -y apache2 >log.saida 2> log.erro
if (($? == 0)) ; then
	cd /var/www
	caminho="/tmp/html_lucas_bkp2.tar.gz"
	if [ -r $caminho ] ; then
		tar xzf $caminho
		echo "Backup restaurado"
	else
		echo "Backup inexistente ou permissão para leitura faltando"
	fi
else
	echo -e "\nErro na instalação do apache2 pelo aptitude"
fi

#NOME="Lucas Manchine"

#echo Hello World - $NOME
#echo $1
#echo $0
#echo $*
