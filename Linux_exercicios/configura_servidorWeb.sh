#!/bin/bash

# Prova de Conceito 01 - Tássio Sáles
echo "Prova de Conceito 01 - Tássio Sales"

#Etapa 01 - Atualizando pacotes
apt-get update
apt-get upgrade

#Etapa 02 - Instalando pacote (apache2)
apt-get install -y apache2

#Etapa 03 - Instalando pacote (wget)
apt-get install -y wget

#Etapa 04 - Download do arquivo .zip
wget https://gist.github.com/nunomazer/873219/archive/690e1f604dc8ead2583589e1aee6f8a42040a035.zip

#Etapa 05 - Instalando pacote (zip e unzip)
apt-get install -y zip unzip
# Descompacta o arquivo zip
unzip 690e1f604dc8ead2583589e1aee6f8a42040a035.zip
# Entra na pasta descompactada