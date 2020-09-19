#!/bin/bash

if (($# == 1)) ; then 
	caminho_bkup=$1
elif (($# >1)) ; then
	echo "Re-execute o comando com número de arugmentos apropriados (1/0)."
	exit 10
else
	caminho_bkup="html_bkup.tar.gz"
fi

aptitude remove -y apache2 > log_desinstala.saida 2> log_desinstala.erro
if (($? ==0)) ; then
	cd /var/www
	if [ -d html -a -r html ] ; then
		tar cvzf /tmp/$caminho_bkup html
		rm -fr html
	else
		echo "Pasta html inexistente ou sem permissão de leitura"
	fi
else
	echo "Erro ao desinstalar apache2"
fi
