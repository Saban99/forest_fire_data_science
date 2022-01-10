#Paket Kurulumları

import sys
import pandas as pd
import googletrans
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()


pd.set_option("display.max_rows", None, "display.max_columns", None) #pandas opsiyonu bütün satır ve sütunlar gelsin diye

data = pd.read_csv("amazon.csv",thousands = '.') #csv dosyasını okuyoruz

durum = int(input("İşlem yapmak istediğiniz numarayı girin: ")) #işlem koşul bloğu hazırlama

if durum == 1:
    print(data.head())  # dosyanın başını okuyoruz
elif durum == 2:
    print(data.describe(include="all"))  # dosya ile ilgili analiz edebilecğeimiz verileri alıyoruz
elif durum == 3:
    print(data.isna().sum()) #missing value(kayıp değer) varsa buna bakılır
elif durum == 4:
    print(data.info())


