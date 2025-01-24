from selenium import webdriver
import pandas as pd
import chromedriver_autoinstaller
import time
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriver'ı otomatik olarak yükle
chromedriver_autoinstaller.install()

# WebDriver'ı başlat
driver = webdriver.Chrome()

# Tablet ve telefon verilerini saklamak için boş listeler oluştur
pc_data = []


# URL ve kategoriye göre veri çekme fonksiyonu
def fetch_data(url, data_list):
    # Her bir URL için benzersiz ürün bağlantılarını saklamak amacıyla bir set oluştur
    visited_links = set()

    # Sayfa numaraları üzerinde döngü (örnek olarak 1'den 20'ye kadar)
    for page in range(1,5):  
        # İlgili sayfa numarasını URL'ye ekle
        page_url = f"{url}?pi={page}"
        driver.get(page_url)
        time.sleep(3)  # Sayfanın tamamen yüklenmesi için bekleyin

        # Ürün linklerini içeren öğeleri bekle
        try:
            product_links = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".p-card-wrppr a"))
            )
            # Yeni ürün linklerini sete ekle
            new_links = {link.get_attribute('href') for link in product_links} - visited_links
            visited_links.update(new_links)
            print(f"{len(new_links)} tane link {page}. sayfadan alındı.")
        except Exception as e:
            print(f"Sayfa {page} yüklenemedi: {e}")
            continue

    # Her bir benzersiz ürün linkini ziyaret et ve detayları çek
    for link in visited_links:
        try:
            driver.get(link)
            time.sleep(2)  # Ürün detaylarının tam olarak yüklenmesi için bekleyin

            # Ürün bilgilerini al
            marka = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.product-brand-name-with-link"))
            ).text
            model = driver.find_element(By.CSS_SELECTOR, "h1.pr-new-br > span").text
            değerlendirme = driver.find_element(By.CSS_SELECTOR, "div.rvw-cnt span.total-review-count").text
            soru_cevap = driver.find_element(By.CSS_SELECTOR, "span.answered-questions-count").text
            değerlendirme_puanı = driver.find_element(By.CSS_SELECTOR, "div.product-rating-score div.value").text
            fiyat = driver.find_element(By.CSS_SELECTOR, "span.prc-dsc").text

            # Ürün bilgilerini sözlük olarak sakla
            ürün_bilgisi = {
                "Marka": marka,
                "Model": model,
                "Değerlendirme Sayısı": değerlendirme,
                "Soru-Cevap Sayısı": soru_cevap,
                "Değerlendirme Puanı": değerlendirme_puanı,
                "Fiyat": fiyat
            }

            # Özellikleri çek
            try:
                feature_elements = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "detail-attr-item"))
                )
                for feature_element in feature_elements:
                    feature_key = feature_element.find_element(By.CLASS_NAME, 'attr-key-name-w').text
                    feature_value = feature_element.find_element(By.CSS_SELECTOR, '.attr-name.attr-value-name-w').text
                    ürün_bilgisi[feature_key] = feature_value

            except Exception as e:
                print(f"Özellikler alınırken hata oluştu: {e}")

            # Ürün verilerini belirtilen listeye ekle
            data_list.append(ürün_bilgisi)

        except Exception as e:
            print(f"Hata: {e} - Ürün linki: {link}")
            continue

# Tablet ve telefon verilerini çek
fetch_data("https://www.trendyol.com/bilgisayar-x-c108656", pc_data) # link ekle


# DataFrame'leri oluştur
pc_df = pd.DataFrame(pc_data)


# Tablet ve telefon verilerini CSV ve Excel dosyalarına kaydet
pc_df.to_csv("Bilgisayarlar.csv", index=False)

# Tarayıcıyı kapat
driver.quit()


