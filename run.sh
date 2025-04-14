#!/bin/bash

pip install PyMuPDF || {
    echo "Erro ao instalar PyMuPDF"
}

if [ "$?" -eq 0 ]; then
    echo "PyMuPDF instalado"
fi

if [ "$#" -ne 1 ]; then
    echo "Utilização: $0 <caminho_do_arquivo.pdf>"
    exit 1
fi

pdf="$1"

if [ ! -f "$pdf" ]; then
    echo "Erro: '$pdf' não encontrado!"
    exit 1
fi

python3 main.py  "$pdf"
