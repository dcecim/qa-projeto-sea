#!/bin/bash

# Script para instalar dependências e executar os testes automatizados
# Autor: Projeto QA SEA Tecnologia

echo "=== Instalando dependências ==="
pip install playwright pytest pytest-playwright

echo "=== Instalando navegadores para o Playwright ==="
python -m playwright install

echo "=== Executando testes automatizados ==="
cd /home/ubuntu/qa-projeto-sea
python -m pytest tests/ -v

echo "=== Testes concluídos ==="
echo "Verifique os resultados e screenshots na pasta /tests/"
