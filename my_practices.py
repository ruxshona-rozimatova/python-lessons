# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:33:58 2026

@author: user
"""

# otam = {'ism':'Anvar', 't_yil':1972, 'shahar':'Ryazan'}
# onam = {'ism':'Yulduzxon', 't_yil':1979, 'shahar': "Moskva"}
# akam = {'ism': 'Umrzoq', 't_yil':2002, 'shahar': 'Kazan'}
# men = {'ism':"Ruxshona", 't_yil':2005, 'shahar': 'Samarqand'}
# print(f"Otamning ismi {otam['ism']}. {otam['t_yil']}-yilda tug'ilgan.\
#  Hozirda {otam['shahar']}da yashaydi.")
 
 
# taomlar = {'otam':'osh', 'onam':'manti', 'akam':'norin', 'o\'zim':'sho\'rva'}
# print(f'Dadamning sevimli taomi {taomlar['otam']}')
# print(f"Onamning sevimli taomi {taomlar['onam']}")
# print(f"Akamning sevimli taomi {taomlar['akam']}")
# print(f"Mening sevimli taomim {taomlar['o\'zim']}")

python_dict = {'int':'integer, butun son', 'str':'string, matn', \
                'float':'floating number, o\'nli son', 'if':'agar,shart operatori', \
              'dictionary':"lug'at", 'list':"ro'yxat", 'bool':'boolean',\
              'tuple':'o\'zgarmas ro\'yxat', 'type':"o'zgaruvchi turini aniqlovchi funksiya",\
            'for':'uchun, shart operatori', 'while':'sikl,takrorlash operatori', 'loop':'sikl'
                }
# print(python_dict)

atama = input("Pythonga oid biror atama so'rang:")
if atama in python_dict:
    print(f"{atama}- {python_dict.get(atama, "Bu so'z mavjud emas")}")
else:
    print("Kechirasiz, bu so'z lug'atda mavjud emas")
