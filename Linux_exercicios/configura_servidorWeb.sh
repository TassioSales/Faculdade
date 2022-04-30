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