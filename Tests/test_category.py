from time import sleep
from ddt import ddt, data, unpack
from selenium import webdriver
from pages.Category import *
import softest
import unittest
import pytest
from constest import *

@pytest.mark.usefixtures("setup")
@ddt

class Test_Scenario_TS001_Product_Catalog_Imaging(softest.TestCase, unittest.TestCase):
    
    def test_Case_TC001_category_and_sub_category_selection(self):
        
        category =category_and_sub_category_selection(self.driver)
        category.accept_cookies()
        category.Click_on_the_electronics_category_in_the_top_left_menu_on_the_homepage()
        category.Click_on_the_ComputerTablet_category()
        category.take_a_screen_photo()
       

    def test_Case_TC002_Search_with_one_character(self):
 
        category =Search_with_one_character(self.driver)
        category.accept_cookies()
        category.Click_onthe_Search_button()
        category.Type_a_single_character()
        category.Click_on_the_Search_button()
        category.click_again_search_bar()
        category.Display_the_message_You_must_type_at_least_2_characters_to_start_searching()
        category.take_a_screen_photo()

    def test_Case_TC003_Product_search_and_filtering_of_resultssil(self):
        category = Product_search_and_filtering_of_results(self.driver)
        category.accept_cookies()
        category.Click_onthe_Search_button()
        category.Type_a_single_character()
        category.Click_on_the_Search_button()
        category.page_down_slide()
        category.Select_the_brand_from_the_menu_and_filter()

    def test_Case_TC004_Accuracy_of_features_and_price_on_product_detail_page(self):
        search = Product_search_and_filtering_of_results(self.driver)
        category =Accuracy_of_features_and_price_on_product_detail_page(self.driver)
        search.accept_cookies()
        search.Click_onthe_Search_button()
        search.Type_a_single_character()
        search.Click_on_the_Search_button()
        search.page_down_slide()
        search.Select_the_brand_from_the_menu_and_filter()
        category.Click_on_a_product_from_product_list()
        self.driver.close()
        category.return_first_tab()
        category.page_down_slide()
        category.Click_all_features_button()
        category.take_a_screen_photoo()