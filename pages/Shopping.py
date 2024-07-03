# import pytest
# from time import sleep
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.action_chains import ActionChains
# from pages.PageBase import PageBase
# from constans.globalconstans import*

# @pytest.mark.usefixtures("setup")
# class SarkıArama(PageBase):
#     def __init__(self,driver):
#         super().__init__(driver)
#         self.driver = driver
    
#     def arama_butonuna_tıkla(self):
#         self.wait_element_visibility(ARAMA_BUTONU).click()

#     def sarkı_araması_yap(self):
#         self.wait_element_visibility(ARAMA_KUTUSU).send_keys(TEST_ARAMA_SARKISI)
#         sleep(2)

#     def sarkıyı_başlat(self):
#         çal= self.wait_element_visibility(PLAY_BUTONU)
#         aria_label = çal.get_attribute('aria-label')
#         çal.click()
#         return aria_label

#     def sarkıyı_atla(self):
#         atla= self.wait_element_visibility(ATLA)
#         aria_label = atla.get_attribute('aria-label')
#         atla.click()
#         return aria_label
    
#     def dur_butonuna_tıkla(self):
#         dur = self.wait_element_visibility(PLAY_BUTONU)
#         aria_label = dur.get_attribute('aria-label')
#         dur.click()
#         return aria_label

#     def sarkıyı_begenilenler_listesine_ekle(self):
#         self.wait_element_visibility(BEGENILEN_SARKI_LISTESI_BUTONU).click()
    
#     def sarkıyı_begenilenler_listesine_popup_mesajı(self):
#         popup = self.wait_element_visibility(BEGENILEN_SARKI_MESAJI_LOCATER)
#         return popup.text
    
#     def ekran_foto_cek(self):
#         ekrangoruntusu_path = FOTO_SARKI_BEGENILENLERE_EKLENDI_POPUP
#         self.driver.save_screenshot(ekrangoruntusu_path)