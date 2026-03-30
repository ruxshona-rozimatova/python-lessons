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
# Hozirda {otam['shahar']}da yashaydi.")
 
 
# taomlar = {'otam':'osh', 'onam':'manti', 'akam':'norin', 'o\'zim':'sho\'rva'}
# print(f'Dadamning sevimli taomi {taomlar['otam']}')
# print(f"Onamning sevimli taomi {taomlar['onam']}")
# print(f"Akamning sevimli taomi {taomlar['akam']}")
# print(f"Mening sevimli taomim {taomlar['o\'zim']}")

# python_dict = {'int':'integer, butun son', 'str':'string, matn', \
#                 'float':'floating number, o\'nli son', 'if':'agar,shart operatori', \
#               'dictionary':"lug'at", 'list':"ro'yxat", 'bool':'boolean',\
#               'tuple':'o\'zgarmas ro\'yxat', 'type':"o'zgaruvchi turini aniqlovchi metod",\
#             'for':'uchun, shart operatori', 'while':'sikl,takrorlash operatori', 'loop':'sikl'
#               }
# print(python_dict)

# atama = input("Pythonga oid biror atama so'rang:")
# if atama in python_dict:
#     print(f"{atama}- {python_dict.get(atama, "Bu so'z mavjud emas")}")
# else:
#     print("Kechirasiz, bu so'z lug'atda mavjud emas")


#sorted() metodi
# print("python_dict lug'ati ichidagi atamalar alifbo tartibida:")
# for key, value in sorted(python_dict.items()):
#     print(f"{key} - {value}.")
    

# davlatlar = {'Buyuk Britaniya':'London', "AQSH":'Washington',\
#              'Turkiya':'Istanbul', 'Fransiya':'Parij', 'Hindiston':'Dehli',\
#                  "O'zbekiston":"Toshkent", "Rossiya":"Moskva"
#     }
# print("Davlatlar:")   #Davlat va poytaxt nomlarini alohida tartiblash
# for davlat in sorted(davlatlar.keys()):
#     print(davlat)
# print("Poytaxtlar:")
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt)


# country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
# capital = davlatlar.get(country)
# for key in davlatlar:
#     if key.lower() == country:
#         print(f"{key}ning poytaxti {davlatlar[key].title()} shahri")
#         break
# else:
#     print("Kechirasiz, bizda bu haqida ma'lumot yo'q")


# menu = {
#         'osh':50000,
#         "lag'mon":22000,
#         'non':4000,
#         'shi':30000,
#         'borsh':45000,
#         'chechevitsa sup':30000,
#         'choy':5000,
#         'shashlik':25000,
#         'somsa':10000,
#         'tabaka':15000
#         }
# print("Taom buyurtma bering:")
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom:").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} {menu[buyurtma]} so'm.")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q.")

#NESTING
adabiyot = {
        'ism':'Alisher Navoiy',
        't_yil':1441,
        'vaf_yil':1501,
        'tillar':'fors va arab',
        'shahar':'Hirot',
        'faoliyat':'g\'azalshunos, vazirlik'
        }

sanat = {
        'ism':'Obid Asomov',
        't_yil':1963,
        'vaf_yil':2018,
        'shahar':'Toshkent',
        'faoliyat':'so\'z ustasi, aktyorlik'
        }

internet = {
        'ism':'Bill Gates',
        'shahar':'Washington',
        't_yil':1955,
        'kapital': 102.1,
        'faoliyat':'entrepreneurship'
        }
shaxslar = [adabiyot, sanat, internet]
for shaxs in shaxslar:
    print(f"{shaxs['ism']} {shaxs['t_yil']}-yilda tug'ilgan.")
    print(f"{shaxs['shahar']}da tug'ilgan.")
    print(f"U {shaxs['faoliyat']} sohasida faoliyat olib borgan.\n")







