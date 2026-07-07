#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
POLO DE INOVAÇÃO IFAM - CAMPUS MANAUS ZONA LESTE
DIGITAL TRANSFORMATION ACADEMY - LG INOVA
DISCIPLINA: Técnicas de Hyperautomation
PROFESSOR: Moisés Levy

Autor: João Lucas Mota Ausier (Aluno C)
Módulo: Automação de Exportação de Dados (Cenário A - BPMN)
Descrição: Script utilizando BotCity Web para automatizar a extração de dados 
           do Portal Fake nos formatos CSV e JSON.
"""

import sys
from botcity.web import WebBot, Browser

def exportar_dados():
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME

    try:
        print("[ALUNO C] Iniciando automação do módulo de Exportação de Dados...")
        
        # URL local padrão do Portal Fake
        portal_url = "http://localhost:5500" 
        bot.browse(portal_url)
        bot.wait(2000)
        
        print("[ALUNO C] Verificando se há registros na grid para exportação...")
        
        # Validação de QA: Evita exportar base vazia
        row_count = bot.execute_javascript("return document.querySelectorAll('table tbody tr').length;")
        
        if row_count == 0:
            raise Exception("Base de dados vazia! Ação de exportação abortada para evitar arquivos corrompidos.")

        print(f"[ALUNO C] Validação concluída. {row_count} registros encontrados na tabela.")
        
        # Executa o clique no botão de exportação JSON (ID mapeado no portal)
        if bot.find_element("btnExportarJSON", by="id"):
            bot.click()
            print("[ALUNO C] Exportação JSON executada com sucesso.")
        else:
            bot.click_on("#btn-export-json")
            print("[ALUNO C] Exportação JSON executada via seletor alternativo CSS.")
            
        bot.wait(2000)
        
    except Exception as erro:
        print(f"ALERTA DE ERRO OPERACIONAL (QA): {str(erro)}")
        
    finally:
        print("[ALUNO C] Finalizando a instância do navegador.")
        bot.stop_browser()

if __name__ == "__main__":
    exportar_dados()