import random
from selenium.webdriver.common.by import By
BASE_URL="https://www.hepsiburada.com/"

CEREZLERI_KABUL_ET=(By.ID,"onetrust-accept-btn-handler")

#Kategori seçimi

ELEKTRONIK_LOC = (By.CLASS_NAME,"sf-MenuItems-WulWXvlfIAwNiOUGY7FP")
BILGISAYAR_TABLET_LOC =(By.LINK_TEXT, "Bilgisayar/Tablet")
DIZUSTU_BILGISAYAR_LOC=(By.CLASS_NAME, "sf-ChildMenuItems-KdzkrxSVhcwDy3od0Yre.item-1854")
ISLETIM_TIPI_LOC=(By.CLASS_NAME,"heroContent-AoOQlh9KimEfuUX1Qd8x")

ARAMA_CUBUGU_LOC =(By.CSS_SELECTOR, ".searchBoxOld-M1esqHPyWSuRUjMCALPK")
ARAMA_METIN_YAZ_LOC=(By.CSS_SELECTOR, ".theme-IYtZzqYPto8PhOx3ku3c")
ARAMA_TEK_KARAKTER_TEXT= ("A")
TEKRAR_ARAMA_BUTONU=(By.CSS_SELECTOR, ".theme-IYtZzqYPto8PhOx3ku3c")

DOGRU_ARAMA_TEXT=("laptop")
ARA_BUTONU_LOC=(By.CSS_SELECTOR, ".searchBoxOld-yDJzsIfi_S5gVgoapx6f")
ARAMA_MESAJI_LOC=(By.CLASS_NAME,"suggestionContainer-JFdcsnrpww4iLf97IFO3")
ARAMA_MESAJI_TEXT=("Aramaya başlamak için en az 2 karakter  yazmalısınız")

MARKA_FILTRESI_LOC=(By.CLASS_NAME,"heroContent-AoOQlh9KimEfuUX1Qd8x")

URUN_LOC=(By.CLASS_NAME,"productListContent-zAP0Y5msy8OHn5z7T_K_")
TUM_OZELLIKLER=(By.LINK_TEXT, "Tüm Özellikler")

SEPETE_EKLE=(By.CLASS_NAME,"button.big.with-icon")
URUN_SEPETE_EKLENDI_POPUP=(By.CLASS_NAME,"checkoutui-ProductOnBasketHeader-iw50qYCZPlh2SmNOYu1E")
MESAJI_KAPAT=(By.CLASS_NAME,"checkoutui-Modal-iHhyy79iR28NvF33vKJb")
SEPETIM=(By.CSS_SELECTOR, ".checkoutui-ProductOnBasketHeader-zdTSacusLu4Cu0LDpmnB > button:nth-child(1)")
SEPETTEKI_URUN_SAYISI=(By.CLASS_NAME,"basket_itemCount_2NxQo")

URUNU_ARTTIR=(By.CSS_SELECTOR,".product_quantities_1LpFc > a:nth-child(3) > svg:nth-child(1)")
URUN_MIKTARI=(By.CSS_SELECTOR, ".product_quantities_1LpFc > input:nth-child(2)")
URUNU_AZALT=(By.CSS_SELECTOR, ".product_quantities_1LpFc > a:nth-child(1) > svg:nth-child(1)")

COP_KUTUSU=(By.CLASS_NAME, "delete_button_1lHhf")
SEPET_KONTROL=(By.CSS_SELECTOR, ".content_Z9h8v > h1:nth-child(1)")
SEPET_KONTROL_TEXT="Sepetin şu an boş"
SEPET_URUN = (By.CLASS_NAME, "product_name_2Klj3")

ALISVERISI_TAMAMLA=(By.ID,"continue_step_btn")
UYEOLMADAN_DEVAMET=(By.CLASS_NAME,"_1mCdWR7afWBEU4zMRu13zb")
EPOSTA=(By.CLASS_NAME,"hb-AxmsV.gwOB.sfczxnxo358")
EPOSTA_DEVAMET=(By.ID,"btnWithoutMemberShip")



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