import random
from selenium.webdriver.common.by import By
BASE_URL="https://www.hepsiburada.com/"

ACCEPT_COOKIES_LOC=(By.ID,"onetrust-accept-btn-handler")

#Kategori seçimi

ELECTRONIC_LOC = (By.CLASS_NAME,"sf-MenuItems-WulWXvlfIAwNiOUGY7FP")
COMPUTER_TABLET_LOC =(By.LINK_TEXT, "Bilgisayar/Tablet")
LAPTOP_COMPUTER_LOC=(By.CLASS_NAME, "sf-ChildMenuItems-KdzkrxSVhcwDy3od0Yre.item-1854")
OPERATING_TYPE_LOC=(By.CLASS_NAME,"heroContent-AoOQlh9KimEfuUX1Qd8x")

#SEARCH_CUBICLE_LOC =(By.CSS_SELECTOR, ".searchBoxOld-M1esqHPyWSuRUjMCALPK")
SEARCH_TEXT_WRITE_LOC=(By.CSS_SELECTOR, ".theme-IYtZzqYPto8PhOx3ku3c")
SEARCH_SINGLE_CHARACTER_TEXT= ("A")
REPEAT_SEARCH_BUTTON=(By.CSS_SELECTOR, ".theme-IYtZzqYPto8PhOx3ku3c")

CORRECT_SEARCH_TEXT=("laptop")
SEARCH_BUTTON_LOC=(By.CSS_SELECTOR, ".searchBoxOld-yDJzsIfi_S5gVgoapx6f")
SEARCH_MESSAGE_LOC=(By.CLASS_NAME,"suggestionContainer-JFdcsnrpww4iLf97IFO3")
#SEARCH_MESSAGE_TEXT=("Aramaya başlamak için en az 2 karakter  yazmalısınız")

BRAND_FILTER_LOC=(By.CLASS_NAME,"heroContent-AoOQlh9KimEfuUX1Qd8x")

URUN_LOC=(By.CLASS_NAME,"productListContent-zAP0Y5msy8OHn5z7T_K_")
#ALL_FEATURES=(By.LINK_TEXT, "Tüm Özellikler")

ADD_TO_CART_SUPPLY=(By.CLASS_NAME,"button.big.with-icon")
PRODUCT_ADDED_TO_CART_POPUP=(By.CLASS_NAME,"checkoutui-ProductOnBasketHeader-iw50qYCZPlh2SmNOYu1E")
#CLOSE_MESSAGE=(By.CLASS_NAME,"checkoutui-Modal-iHhyy79iR28NvF33vKJb")
MY_BASKET=(By.CSS_SELECTOR, ".checkoutui-ProductOnBasketHeader-zdTSacusLu4Cu0LDpmnB > button:nth-child(1)")
#NUMBER_OF_PRODUCTS_IN_CART=(By.CLASS_NAME,"basket_itemCount_2NxQo")

INCREASE_PRODUCT=(By.CSS_SELECTOR,".product_quantities_1LpFc > a:nth-child(3) > svg:nth-child(1)")
PRODUCT_QUANTITY=(By.CSS_SELECTOR, ".product_quantities_1LpFc > input:nth-child(2)")
REDUCE_PRODUCT=(By.CSS_SELECTOR, ".product_quantities_1LpFc > a:nth-child(1) > svg:nth-child(1)")

COP_BOX=(By.CLASS_NAME, "delete_button_1lHhf")
#CART_CONTROL=(By.CSS_SELECTOR, ".content_Z9h8v > h1:nth-child(1)")
#CART_CONTROL_TEXT="Sepetin şu an boş"
CART_PURPOSE = (By.CLASS_NAME, "product_name_2Klj3")

# SHOPPING_COMPLETE=(By.ID,"continue_step_btn")
# WITHOUT_MEMBERSHIP=(By.CLASS_NAME,"_1mCdWR7afWBEU4zMRu13zb")
# EMAIL=(By.CLASS_NAME,"hb-AxmsV.gwOB.sfczxnxo358")
# EMAIL_CONTINUE=(By.ID,"btnWithoutMemberShip")



#randon giris

randonint = str(random.randint(1000, 9999))
kullanici_eposta= ("gonca"+ randonint +"@hotmail.com")
kullanici_ad = "gonca"
kullanici_sifre = "g123456789"



#ekran görüntüsü
FOTO_KATEGORI=r'screenshots\category\kategoriler doğru görüntülendi.png'
FOTO_ARAMA_POPUP=r'screenshots\category\iki karakter mesajı.png'
FOTO_URUN_OZELLIKLERI=r'screenshots\category\ürün özellikleri.png'
FOTO_SEPET_KONTROL=r'screenshots\category\sepet ürün eklenmesi.png'
FOTO_SEPET_KONTROL_POPUP_MESAJI=r'screenshots\category\"sepetinize eklendi popup mesajı.png'