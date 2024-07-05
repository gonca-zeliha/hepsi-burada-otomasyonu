import pytest
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from pages.PageBase import PageBase
from constans.globalconstans import*

#kategori_ve_alt_kategori_seçimi
@pytest.mark.usefixtures("setup")
class category_and_sub_category_selection(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    
    def accept_cookies(self):
        click= self.wait_element_visibility(ACCEPT_COOKIES_LOC)
        click.click()

#Anasayfadaki_sol_üst_menüde_elektronik_kategorisine_tıklayın
    def Click_on_the_electronics_category_in_the_top_left_menu_on_the_homepage (self):
       
        click= self.wait_element_visibility(ELECTRONIC_LOC)
        click.click()

    #Bilgisayar/Tablet kategorisine tıklayın.

    def Click_on_the_ComputerTablet_category(self):
        self.wait_element_visibility(COMPUTER_TABLET_LOC).click()

    def take_a_screen_photo(self):
        ekrangoruntusu_path = FOTO_KATEGORI
        self.driver.save_screenshot(ekrangoruntusu_path)

#Tek_karakter_ile_arama_yapılması
@pytest.mark.usefixtures("setup")
class Search_with_one_character(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def accept_cookies(self):
        tıkla= self.wait_element_visibility(ACCEPT_COOKIES_LOC)
        tıkla.click()
    
    #Ana sayfadaki arama çubuğuna tıklayın.
    def Click_onthe_Search_button(self):
        self.wait_element_visibility(SEARCH_BUTTON_LOC).click()
     #Tek karakter yazın.
    def Type_a_single_character(self):
       self.wait_element_visibility(SEARCH_TEXT_WRITE_LOC).send_keys(SEARCH_SINGLE_CHARACTER_TEXT)

    #Ara butonuna tıklayın.
    def Click_on_the_Search_button(self):
        self.wait_element_visibility(SEARCH_BUTTON_LOC).click()

    #tekrar arama butonuna tıkla.
    def click_again_search_bar(self):
        self.wait_element_visibility(REPEAT_SEARCH_BUTTON).click()

    #"Aramaya başlamak için  en az 2 karakter  yazmalısınız" mesajını görüntüleyin. 
    def Display_the_message_You_must_type_at_least_2_characters_to_start_searching(self):
        popup = self.wait_element_visibility(SEARCH_MESSAGE_LOC)
        return popup.text
    
    #ekran fotosu
    def take_a_screen_photo(self):
        ekrangoruntusu_path = FOTO_ARAMA_POPUP
        self.driver.save_screenshot(ekrangoruntusu_path)
 
# Ürün araması ve sonuçların filtrelenmesi 
@pytest.mark.usefixtures("setup")
class  Product_search_and_filtering_of_results(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    
    def accept_cookies(self):
        click= self.wait_element_visibility(ACCEPT_COOKIES_LOC)
        click.click()
    
    def Click_onthe_Search_button(self):
        self.wait_element_visibility(SEARCH_BUTTON_LOC).click()

    #laptop yazın
    def Type_a_single_character(self):
       self.wait_element_visibility(SEARCH_TEXT_WRITE_LOC).send_keys(CORRECT_SEARCH_TEXT)

     #Ara butonuna tıklayın.
    def Click_on_the_Search_button(self):
        self.wait_element_visibility(SEARCH_BUTTON_LOC).click()
    
    def page_down_slide (self):
        self.driver.execute_script("scrollBy(0,500)")

    #menüden markayı seçin ve filtreleyin.
    def Select_the_brand_from_the_menu_and_filter(self):

        self.wait_element_visibility(BRAND_FILTER_LOC).click()
        

# Ürün detay sayfasında özelliklerin ve fiyatın doğruluğu
@pytest.mark.usefixtures("setup")
class  Accuracy_of_features_and_price_on_product_detail_page(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    #Ürün listesinden bir ürün seçin.
    def Click_on_a_product_from_product_list(self):
         self.wait_element_visibility(URUN_LOC).click()
         sleep(2)
        
    #diğer sayfaya geç
    def return_first_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
    
    def item_description_assert(self):
        # Öğenin açıklamasını bul ve döndür
        item_desc = self.wait_element_visibility(URUN_LOC)
        return item_desc.text








    


    


  


    


    