from time import sleep
from ddt import ddt, data, unpack
from selenium import webdriver
from pages.Category import *
from pages.Shopping import *
import softest
import unittest
import pytest
from constest import *

@pytest.mark.usefixtures("setup")
@ddt


class Test_Scenario_TS002_Shopping_Supermarket_Management (softest.TestCase, unittest.TestCase):
    
    def test_Case_TC005_Add_product_to_cart (self):
        search = Product_search_and_filtering_of_results(self.driver)
        category =Accuracy_of_features_and_price_on_product_detail_page(self.driver)
        shopping=Add_product_to_cart(self.driver)
        search.accept_cookies()
        search.Click_onthe_Search_button()
        search.Type_a_single_character()
        search.Click_on_the_Search_button()
        search.page_down_slide()
        search.Select_the_brand_from_the_menu_and_filter()
        category.Click_on_a_product_from_product_list()
        self.driver.close()
        category.return_first_tab()
        shopping.Click_the_Add_to_Cart_button_on_the_product_detail_page()
        shopping.display_popup_message_in_your_product_pocket()
        shopping.take_a_screen_photoo()
        shopping.Go_to_the_cart_paget()
        shopping.take_a_screen_photo()

    def test_Case_TC006_Increasing_the_quantity_of_items_in_the_basket(self):
        
        category =Accuracy_of_features_and_price_on_product_detail_page(self.driver)
        shopping=Add_product_to_cart(self.driver)
        product_augmentation= Increasing_the_quantity_of_items_in_the_basket(self.driver)

        shopping.accept_cookies()
        shopping.Click_on_the_electronics_category_in_the_top_left_menu_on_the_homepage()
        shopping.Hover_over_the_Computer_Tablet_category()
        shopping.Choose_the_laptop()
        shopping.Filter_operating_type()
        shopping.filter_brand()
        shopping.Click_on_a_product_from_product_list()
        self.driver.close()
        category.return_first_tab()
        shopping.Click_the_Add_to_Cart_button_on_the_product_detail_page()
        shopping.Go_to_the_cart_paget()
        product_augmentation.Increase_the_quantity_of_items_in_the_basket()
        product_augmentation.Check_the_increase_of_the_basket_content()


    def test_Case_TC007_Reducing_the_quantity_of_items_in_the_basket(self):
        category =Accuracy_of_features_and_price_on_product_detail_page(self.driver)
        shopping=Add_product_to_cart(self.driver)
        product_augmentation= Increasing_the_quantity_of_items_in_the_basket(self.driver)
        reduce_product=Reducing_the_quantity_of_items_in_the_basket(self.driver)

        shopping.accept_cookies()
        shopping.Click_on_the_electronics_category_in_the_top_left_menu_on_the_homepage()
        shopping.Hover_over_the_Computer_Tablet_category()
        shopping.Choose_the_laptop()
        shopping.Filter_operating_type()
        shopping.filter_brand()
        shopping.Click_on_a_product_from_product_list()
        self.driver.close()
        category.return_first_tab()
        shopping.Click_the_Add_to_Cart_button_on_the_product_detail_page()
        shopping.display_popup_message_in_your_product_pocket()
        shopping.Go_to_the_cart_paget()
        product_augmentation.Increase_the_quantity_of_items_in_the_basket()
        reduce_product.You_reduced_the_quantity_of_items_in_the_basket()
        
    
    def test_Case_TC008_Remove_Product_in_Cart(self):

        remove_product= Remove_Product_in_Cart(self.driver) #ürün kaldırma
        category =Accuracy_of_features_and_price_on_product_detail_page(self.driver) #ürün sayfası
        shopping=Add_product_to_cart(self.driver)#ürün ekle
        product_augmentation= Increasing_the_quantity_of_items_in_the_basket(self.driver) #ürün artır
        reduce_product=Reducing_the_quantity_of_items_in_the_basket(self.driver) #ürün azalt

        shopping.accept_cookies()
        shopping.Click_on_the_electronics_category_in_the_top_left_menu_on_the_homepage()
        shopping.Hover_over_the_Computer_Tablet_category()
        shopping.Choose_the_laptop()
        shopping.Filter_operating_type()
        shopping.filter_brand()
        shopping.Click_on_a_product_from_product_list()
        self.driver.close()
        category.return_first_tab()
        shopping.Click_the_Add_to_Cart_button_on_the_product_detail_page()
        shopping.display_popup_message_in_your_product_pocket()
        shopping.Go_to_the_cart_paget()
        product_augmentation.Increase_the_quantity_of_items_in_the_basket()
        product_augmentation.Check_the_increase_of_the_basket_content()
        reduce_product.You_reduced_the_quantity_of_items_in_the_basket()
        remove_product.Click_remove_item_from_basket_button()
        remove_product.Check_that_the_product_has_been_removed_from_the_pallet()

