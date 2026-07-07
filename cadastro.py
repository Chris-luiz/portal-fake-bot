import time
from pathlib import Path
import pandas as pd

from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

DELAY = 0.5

def b_cadastrar_usuario(bot, usuario):
    bot.find_element("#btnNovo", By.CSS_SELECTOR).click()
    time.sleep(DELAY)

    for campo_id, coluna in [
        ("f_nome", "nome"),
        ("f_sobrenome", "sobrenome"),
        ("f_cpf", "cpf"),
        ("f_telefone", "telefone"),
        ("f_email", "email"),
        ("f_nascimento", "nascimento"),
        ("f_endereco", "endereco"),
        ("f_observacao", "observacao"),
    ]:
        el = bot.find_element(f"#{campo_id}", By.CSS_SELECTOR)
        el.clear()
        el.send_keys(str(usuario[coluna]))

    Select(bot.find_element("#f_status", By.CSS_SELECTOR)).select_by_value(usuario['status'])
    bot.find_element('#btnSalvar', By.CSS_SELECTOR).click()
    time.sleep(DELAY)