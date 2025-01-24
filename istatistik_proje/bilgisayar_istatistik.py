import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


# Veriyi yükleme
try:
    data = pd.read_csv("data.csv", on_bad_lines='skip')
    print("Veri başarıyla yüklendi.")
except Exception as e:
    print("Veri yüklenirken hata oluştu:", e)

# 'Fiyat' sütununu temizleme ve sayısal hale getirme
if 'data' in locals():  # data'nın tanımlı olup olmadığını kontrol et
    try:
        # Geçersiz karakterleri temizle
        data['Fiyat'] = data['Fiyat'].replace('[^0-9,]', '', regex=True)
        
        # Boş değerleri kontrol et ve temizle
        data['Fiyat'] = data['Fiyat'].replace('', None)  # Boş stringleri None ile değiştir
        
        # Sayısal formata dönüştür
        data['Fiyat'] = data['Fiyat'].str.replace(',', '.').astype(float)
    except Exception as e:
        print("Fiyat sütunu temizlenirken hata oluştu:", e)

    # Boş değerleri kontrol et
    if data['Fiyat'].isnull().sum() > 0:
        print("Boş değerler var, bunları dolduruyoruz.")
        data['Fiyat'] = data['Fiyat'].fillna(data['Fiyat'].mean())  # Ortalamayla doldurma

    try:
        # Geçersiz karakterleri temizle
        data['Ram (Sistem Belleği)'] = data['Ram (Sistem Belleği)'].replace('[^0-9,]', '', regex=True)
        
        # Boş değerleri kontrol et ve temizle
        data['Ram (Sistem Belleği)'] = data['Ram (Sistem Belleği)'].replace('', None)  # Boş stringleri None ile değiştir
        
        # Sayısal formata dönüştür
        data['Ram (Sistem Belleği)'] = data['Ram (Sistem Belleği)'].str.replace(',', '.').astype(float)
    except Exception as e:
        print("Ram sütunu temizlenirken hata oluştu:", e)

    # Boş değerleri kontrol et
    if data['Ram (Sistem Belleği)'].isnull().sum() > 0:
        print("Boş değerler var, bunları dolduruyoruz.")
        data['Ram (Sistem Belleği)'] = data['Ram (Sistem Belleği)'].fillna(data['Ram (Sistem Belleği)'].mean())  # Ortalamayla doldurma


    try:
        # Geçersiz karakterleri temizle
        data['SSD Kapasitesi'] = data['SSD Kapasitesi'].replace('[^0-9,]', '', regex=True)
        
        # Boş değerleri kontrol et ve temizle
        data['SSD Kapasitesi'] = data['SSD Kapasitesi'].replace('', None)  # Boş stringleri None ile değiştir
        
        # Sayısal formata dönüştür
        data['SSD Kapasitesi'] = data['SSD Kapasitesi'].str.replace(',', '.').astype(float)
    except Exception as e:
        print("SSD Kapasitesi sütunu temizlenirken hata oluştu:", e)

    # Boş değerleri kontrol et
    if data['SSD Kapasitesi'].isnull().sum() > 0:
        print("Boş değerler var, bunları dolduruyoruz.")
        data['SSD Kapasitesi'] = data['SSD Kapasitesi'].fillna(data['SSD Kapasitesi'].mean())  # Ortalamayla doldurma

    try:
        # Geçersiz karakterleri temizle
        data['İşlemci Tipi'] = data['İşlemci Tipi'].replace('[^0-9,]', '', regex=True)
        
        # Boş değerleri kontrol et ve temizle
        data['İşlemci Tipi'] = data['İşlemci Tipi'].replace('', None)  # Boş stringleri None ile değiştir
        
        # Sayısal formata dönüştür
        data['İşlemci Tipi'] = data['İşlemci Tipi'].str.replace(',', '.').astype(float)
    except Exception as e:
        print("İşlemci Tipi sütunu temizlenirken hata oluştu:", e)
    # Boş değerleri kontrol et
    if data['İşlemci Tipi'].isnull().sum() > 0:
        print("Boş değerler var, bunları dolduruyoruz.")
        data['İşlemci Tipi'] = data['İşlemci Tipi'].fillna(data['İşlemci Tipi'].mean())  # Ortalamayla doldurma


    try:
        # Geçersiz karakterleri temizle
        data['Değerlendirme Sayısı'] = data['Değerlendirme Sayısı'].replace('[^0-9,]', '', regex=True)
        
        # Boş değerleri kontrol et ve temizle
        data['Değerlendirme Sayısı'] = data['Değerlendirme Sayısı'].replace('', None)  # Boş stringleri None ile değiştir
        
        # Sayısal formata dönüştür
        data['Değerlendirme Sayısı'] = data['Değerlendirme Sayısı'].str.replace(',', '.').astype(float)
    except Exception as e:
        print("Değerlendirme Sayısı sütunu temizlenirken hata oluştu:", e)

    # Boş değerleri kontrol et
    if data['Değerlendirme Sayısı'].isnull().sum() > 0:
        print("Boş değerler var, bunları dolduruyoruz.")
        data['Değerlendirme Sayısı'] = data['Değerlendirme Sayısı'].fillna(data['Değerlendirme Sayısı'].mean())  # Ortalamayla doldurma
    try:
        # Geçersiz karakterleri temizle
        data['Değerlendirme Puanı'] = data['Değerlendirme Puanı'].replace('[^0-9,]', '', regex=True)
        
        # Boş değerleri kontrol et ve temizle
        data['Değerlendirme Puanı'] = data['Değerlendirme Puanı'].replace('', None)  # Boş stringleri None ile değiştir
        
        # Sayısal formata dönüştür
        data['Değerlendirme Puanı'] = data['Değerlendirme Puanı'].str.replace(',', '.').astype(float)
    except Exception as e:
        print("Değerlendirme Puanı sütunu temizlenirken hata oluştu:", e)

    # Boş değerleri kontrol et
    if data['Değerlendirme Puanı'].isnull().sum() > 0:
        print("Boş değerler var, bunları dolduruyoruz.")
        data['Değerlendirme Puanı'] = data['Değerlendirme Puanı'].fillna(data['Değerlendirme Puanı'].mean())  # Ortalamayla doldurma



    # İstatistiksel değerleri hesaplama ve yazdırma
    columns_to_analyze = ['Fiyat', 'Ram (Sistem Belleği)', 'SSD Kapasitesi']
    
    for column in columns_to_analyze:
        if column in data.columns:
            mean_value = data[column].mean()
            mode_value = data[column].mode()[0] if not data[column].mode().empty else None
            median_value = data[column].median()
            std_dev_value = data[column].std()
            variance_value = data[column].var()
    
            # İstatistiksel değerleri yazdırma
            print(f"{column} için İstatistiksel Değerler:")
            print("Ortalama (Mean):", mean_value)
            print("Mod (Mode):", mode_value)
            print("Medyan (Median):", median_value)
            print("Standart Sapma (Standard Deviation):", std_dev_value)
            print("Varyans (Variance):", variance_value)
            print("\n")  # Yeni bir satır ekleyerek çıktıyı daha okunabilir hale getir
    
    # Fiyat dağılımını görselleştirme

    # Histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Fiyat'], bins=30, kde=True, color='blue')
    plt.title('Fiyat Dağılımı')
    plt.xlabel('Fiyat')
    plt.ylabel('Frekans')
    plt.grid(True)
    plt.show()
    
    # Kutu grafiği (Box Plot)
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=data['Fiyat'], color='lightgreen')
    plt.title('Fiyat Dağılımı - Kutu Grafiği')
    plt.xlabel('Fiyat')
    plt.grid(True)
    plt.show()

    # Ram (Sistem Belleği) kapasitesine göre fiyat değişimi
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Ram (Sistem Belleği)', y='Fiyat', data=data, palette='Set3')
    plt.title('Ram (Sistem Belleği) Göre Fiyat Dağılımı')
    plt.xlabel('Ram (Sistem Belleği) (GB)')
    plt.ylabel('Fiyat')
    plt.show()

    # SSD kapasitesine göre fiyat değişimi
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='SSD Kapasitesi', y='Fiyat', data=data, palette='Set2')
    plt.title('SSD Kapasitesine Göre Fiyat Dağılımı')
    plt.xlabel('SSD Kapasitesi (GB)')
    plt.ylabel('Fiyat')
    plt.show()

# Fiyatın RAM kapasitesine göre ortalaması
ram_price_mean = data.groupby('Ram (Sistem Belleği)')['Fiyat'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Ram (Sistem Belleği)', y='Fiyat', data=ram_price_mean, palette='Set1')
plt.title('Ram (Sistem Belleği) Göre Fiyat Ortalaması')
plt.xlabel('Ram (Sistem Belleği) (GB)')
plt.ylabel('Fiyat Ortalaması')
plt.show()

# Fiyatın SSD kapasitesine göre ortalaması
ssd_price_mean = data.groupby('SSD Kapasitesi')['Fiyat'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='SSD Kapasitesi', y='Fiyat', data=ssd_price_mean, palette='Set1')
plt.title('SSD Kapasitesine Göre Fiyat Ortalaması')
plt.xlabel('SSD Kapasitesi (GB)')
plt.ylabel('Fiyat Ortalaması')
plt.show()

# Değerlendirme puanı ile fiyat arasındaki ilişki
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Değerlendirme Puanı', y='Fiyat', data=data, color='purple', alpha=0.6)
plt.title('Değerlendirme Puanı ile Fiyat Arasındaki İlişki')
plt.xlabel('Değerlendirme Puanı')
plt.ylabel('Fiyat')
plt.show()


if "İşlemci Tipi" in data.columns:
    cpu_price_mean = data.groupby("İşlemci Tipi")["Fiyat"].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x="İşlemci Tipi", y="Fiyat", data=cpu_price_mean, palette="Set1")
    plt.title("İşlemci Çekirdek Sayısına Göre Fiyat Ortalaması")
    plt.xlabel("İşlemci Çekirdek Sayısı")
    plt.ylabel("Fiyat Ortalaması")
    plt.show()

# İşlemci Tipi Görselleştirmesi
if "İşlemci Tipi" in data.columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(x="İşlemci Tipi", data=data, palette="Set2", order=data["İşlemci Tipi"].value_counts().index)
    plt.title("İşlemci Çekirdek Sayısı")
    plt.xlabel("İşlemci Çekirdek Sayısı")
    plt.ylabel("Adet")
    plt.show()

    # İşletim Sistemi ve Fiyat Analizi
if "İşletim Sistemi" in data.columns:
    os_price_mean = data.groupby("İşletim Sistemi")["Fiyat"].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x="İşletim Sistemi", y="Fiyat", data=os_price_mean, palette="Set1")
    plt.title("İşletim Sistemine Göre Fiyat Ortalaması")
    plt.xlabel("İşletim Sistemi")
    plt.ylabel("Fiyat Ortalaması")
    plt.show()

if "İşletim Sistemi" in data.columns:
    plt.figure(figsize=(10, 6))
    sns.countplot(x="İşletim Sistemi", data=data, palette="Set3", order=data["İşletim Sistemi"].value_counts().index)
    plt.title("İşletim Sistemlerinin Dağılımı")
    plt.xlabel("İşletim Sistemi")
    plt.ylabel("Adet")
    plt.show()

# Korelasyon analizi
correlation = data[['Fiyat', 'Değerlendirme Puanı']].corr().iloc[0, 1]
print("Fiyat ve Değerlendirme Puanı Korelasyon Katsayısı:", correlation)

# Bağımlı ve bağımsız değişkenleri belirleme
X = data['Değerlendirme Puanı']  # Bağımsız değişken
y = data['Fiyat']  # Bağımlı değişken

# X değişkenini sabit terim ile genişletme
X = sm.add_constant(X)

# Modeli oluşturma
model = sm.OLS(y, X).fit()

# Sonuçları yazdırma
print(model.summary())

# Regresyon doğrusunu çizme
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Değerlendirme Puanı', y='Değerlendirme Sayısı', data=data, color='purple', alpha=0.6)
plt.plot(data['Değerlendirme Puanı'], model.predict(X), color='red', linewidth=2, label='Regresyon Doğrusu')
plt.title('Değerlendirme Puanı ile Değerlendirme Sayısı Arasındaki İlişki ve Regresyon Doğrusu')
plt.xlabel('Değerlendirme Puanı')
plt.ylabel('Değerlendirme Sayısı')
plt.legend()
plt.show()

# İstatistiksel testler
group1 = data[data['Fiyat']]