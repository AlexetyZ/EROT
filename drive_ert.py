import json
import sys

import config
from crypto import Crypto
import undetected_chromedriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

import dict_creator
from config import Ratnikov_knd
import importlib
from Formular_table import get_phrases_list
from direct_pxl import Operation
import os
import re
import json




class Erot:
    def __init__(self):
        self.options = undetected_chromedriver.ChromeOptions()
        prefs = {"credentials_enable_service", False}
        prefs = {"profile.password_manager_enabled": False}

        self.options.add_experimental_option('prefs', prefs)
        self.options.add_argument('--enable-save-password-bubble=false')
        self.options.add_argument("disable-infobars")
        self.options.add_argument("--disable-extensions")
        self.browser = undetected_chromedriver.Chrome(chrome_options=self.options)
        self.browser.get(config.url_main_page_knd)
        self.autorize()


    def autorize(self):
        try:
            WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(
                (By.XPATH, config.ervk_enter_for_login_and_password_xpath_0))).click()
        except:
            self.browser.refresh()
            WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(
                (By.XPATH, config.ervk_enter_for_login_and_password_xpath_0))).click()


        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.XPATH, config.ervk_login_input_xpath_0))).send_keys(
            Ratnikov_knd['login'])

        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.XPATH, config.ervk_password_input_xpath_0))).send_keys(
            Crypto().unpack_password(Ratnikov_knd['password']))

        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(
            (By.XPATH, config.ervk_submit_button_to_enter_in_akk_xpath_0))).click()

        try:
            WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="cdk-overlay-0"]/div/div[1]/button'))).click()
            # self.browser.refresh()
        except:
            pass

    def controller(self):

        self.find_act(act_text='1.2.3685')
        self.driver()

        while True:
            user_command = input('введите П, чтобы продолжить введите З, чтобы завершить')
            if user_command == 'П':
                importlib.reload(dict_creator)

                self.driver()
            elif user_command == 'З':
                break
            else:
                print("Команда не распознана")


    def driver(self):


        print('начинаю собирать ОТ из таблицы...')

        debts = False
        debts_file_name = ''
        for file in os.listdir():
            if re.search('долги_', file):
                debts = True
                debts_file_name = file
                with open(file, 'r') as f:
                    dict_OT = json.load(f)
        if debts is True:
            input(
                f'есть долги, имя - {debts_file_name}. Значения собраны. \nНайдите структурную единицу и нажмите "Создать ОТ". После загрузки страницы нажмите enter в терминале')
            print('есть долги')
            result = self.enter_OT(
                dict_OT=dict_OT
            )
            if result == 0:
                os.remove(debts_file_name)



        else:
            dict_ot = dict_creator.create_dict_OT()


            input(f'Долгов нет. Значения собраны. \nНайдите структурную единицу и нажмите "Создать ОТ". Проверьте содержание файла и убедитесь, что все хорошо. После загрузки страницы нажмите enter в терминале')

            self.enter_OT(
                dict_OT=dict_ot
            )
        print('завершено!')


    def enter_OT(self, dict_OT):
        made = []

        try:
            for n, (phrase, question) in enumerate(dict_OT.items()):
                print(n)
                try:
                    self.browser.find_element(by=By.XPATH,
                                              value=f'/html/body/app-root/app-mandatory-requirement-create/section/div/div[2]/div[1]/div/div[2]/div[{n + 1}]')
                except:
                    while True:
                        try:
                            self.browser.find_element(by=By.XPATH,
                                                      value='/html/body/app-root/app-mandatory-requirement-create/section/div/div[2]/div[1]/button').click()
                            break
                        except:
                            self.browser.find_element(by=By.TAG_NAME, value='html').send_keys(Keys.DOWN * 10)
                            time.sleep(1)

                self.browser.find_element(by=By.TAG_NAME, value='html').send_keys(Keys.DOWN * 10)

                phrase_textarea = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    f'/html/body/app-root/app-mandatory-requirement-create/section/div/div[2]/div[1]/div/div[2]/div[{n + 1}]/div[1]/app-erot-textarea[1]/label/label/textarea')))

                question_textatea = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    f'/html/body/app-root/app-mandatory-requirement-create/section/div/div[2]/div[1]/div/div[2]/div[{n + 1}]/div[1]/app-erot-textarea[2]/label/label/textarea')))
                try:

                    phrase_textarea.click()
                    self.browser.execute_script(
                        f"""const elem = document.evaluate('/html/body/app-root/app-mandatory-requirement-create/section/div/div[2]/div[1]/div/div[2]/div[{n + 1}]/div[1]/app-erot-textarea[1]/label/label/textarea', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null ).singleNodeValue;elem.value = '{phrase}';""")
                    phrase_textarea.send_keys(Keys.SPACE)
                    phrase_textarea.send_keys(Keys.BACKSPACE)

                    question_textatea.click()
                    self.browser.execute_script(
                        f"""const elem = document.evaluate('/html/body/app-root/app-mandatory-requirement-create/section/div/div[2]/div[1]/div/div[2]/div[{n + 1}]/div[1]/app-erot-textarea[2]/label/label/textarea', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null ).singleNodeValue;elem.value = '{question}';""")
                    question_textatea.send_keys(Keys.SPACE)
                    question_textatea.send_keys(Keys.BACKSPACE)
                    self.browser.find_element(by=By.TAG_NAME, value='html').send_keys(Keys.DOWN * 15)
                except:
                    phrase_textarea.clear()
                    phrase_textarea.send_keys(phrase)
                    question_textatea.clear()
                    question_textatea.send_keys(question)
                    self.browser.find_element(by=By.TAG_NAME, value='html').send_keys(Keys.DOWN * 15)
                made.append(phrase)
                time.sleep(0.5)
            return 0

        except Exception as ex:
            print(ex)

            for m in made:
                dict_OT.pop(m)
            with open('долги_name.json', 'w') as f:
                json.dump(dict_OT, f)
            return 1


    def find_act(self, act_text='1.2.3685'):
        self.browser.get('https://rg.gov.ru/npa-knd/registry')
        WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/app-root/app-npa-knd-registry/section/div/div/div[1]/app-erot-input-search/div/input'))).send_keys(
            act_text)
        time.sleep(2)
        self.browser.find_element(By.XPATH,
                                  value='/html/body/app-root/app-npa-knd-registry/section/div/div/div[1]/app-erot-input-search/div/div[2]').click()
        time.sleep(3)
        act_href = self.browser.find_element(By.XPATH,
                                             value='/html/body/app-root/app-npa-knd-registry/app-npa-knd-table/div/perfect-scrollbar/div/div[1]/table/tbody/tr/td[3]/div/a').get_attribute(
            'href')
        self.browser.get(act_href)


if __name__ == '__main__':
    Erot().controller()
