import re
import pytest
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from pages.PageBase import PageBase
from constans.globalconstans import*

#Ürünü sepete ekleme 
@pytest.mark.usefixtures("setup")

class Add_product_to_cart (PageBase):
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

    #Bilgisayar/Tablet kategorisinin üzerine gel..

    def Hover_over_the_Computer_Tablet_category(self):
        self.hover(COMPUTER_TABLET_LOC)
    
    #Diz üstü bilgisayarı seç.
    def Choose_the_laptop(self):
        self.wait_element_visibility(LAPTOP_COMPUTER_LOC).click()
    
    #İşletim tipini filtrele
    def Filter_operating_type(self):
        self.wait_element_visibility(OPERATING_TYPE_LOC).click
    
    #marka filtrele
    def filter_brand(self):
        self.wait_element_visibility(OPERATING_TYPE_LOC).click
    
    #Ürün listesinden bir ürün seçin.
    def Click_on_a_product_from_product_list(self):
         self.wait_element_visibility(URUN_LOC).click()
         sleep(2)

    #Ürün detay sayfasında "Sepete Ekle" butonuna tıklayın
    def Click_the_Add_to_Cart_button_on_the_product_detail_page(self):
        self.wait_element_visibility(ADD_TO_CART_SUPPLY).click()

    #ürün sepetinizde popup mesajını görüntüle.
    def display_popup_message_in_your_product_pocket(self):
        popup = self.wait_element_visibility(PRODUCT_ADDED_TO_CART_POPUP)
        return popup.text
    
    #Sepetim sayfasına gidin.
    def Go_to_the_cart_paget(self):
        # Sepete git butonunu bul ve tıkla
        self.wait_element_visibility(MY_BASKET).click()

    def take_a_screen_photo(self):
        ekrangoruntusu_path = FOTO_SEPET_KONTROL
        self.driver.save_screenshot(ekrangoruntusu_path)
        
#Sepetteki ürünlerin miktarının arttırılması.
@pytest.mark.usefixtures("setup")
class Increasing_the_quantity_of_items_in_the_basket(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    #Sepette ki ürün miktarını arttırın.
    def Increase_the_quantity_of_items_in_the_basket(self):
        self.wait_element_visibility(INCREASE_PRODUCT).click()

    ##Sepet içeriğinin arttışını kontrol edin.
    def Check_the_increase_of_the_basket_content(self):
        Basket_contents = self.wait_element_visibility(PRODUCT_QUANTITY)
        product_quantity = Basket_contents.get_attribute("value")
        return product_quantity


    
#Sepetteki ürünlerin miktarının azaltılması.
@pytest.mark.usefixtures("setup")
class Reducing_the_quantity_of_items_in_the_basket(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

#Sepette ki ürün miktarını azalttın.
    def You_reduced_the_quantity_of_items_in_the_basket(self):
        self.wait_element_visibility(REDUCE_PRODUCT).click()

#Sepetteki Ürünün kaldırılması
@pytest.mark.usefixtures("setup")
class Remove_Product_in_Cart(PageBase):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    
#Sepetteki ürünü kaldır butonuna tıklayın.
    def Click_remove_item_from_basket_button(self):
 
        self.wait_element_visibility(COP_BOX).click()

#Ürünün sepetten kaldırıldığını kontrol edin.
    def Check_that_the_product_has_been_removed_from_the_pallet(self):

        basket_control = self.wait_element_visibility(CART_PURPOSE)
        return basket_control.text


 
