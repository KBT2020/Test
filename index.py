# import requests
# from bs4 import BeautifulSoup as BS
# import json
# import csv
 
# # pip install lxml

# url = 'https://health-diet.ru/table_calorie/'
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 YaBrowser/21.8.1.468 Yowser/2.5 Safari/537.36'
# }
# with open('all_categories.json', encoding='utf-8') as file:
#     all_categories = json.load(file)

# count = 0
# for category_name, category_href in all_categories.items():
#     if count == 0:
#         rep = [' ', ',', '-', "'", '"']
#         for item in rep:
#             if item in category_name:
#                 category_name = category_name.replace(item, '_')
#         req = requests.get(url=category_href, headers=headers)
#         src = req.text

#         with open(f"{category_name}.html", 'w', encoding='utf-8') as file:
#             file.write(src)
        
#         with open(f"{category_name}.html",encoding='utf-8') as file:
#             src = file.read()

#         soup = BS(src, 'lxml')

#         # проверка на таблицы
#         alert_block = soup.find(class_='uk-alert-danger')
#         if alert_block is not None:
#             continue
    
#         #собираем заголовки таблиц
#         table_head = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')
#         product = table_head[0].text
#         calories = table_head[1].text
#         proteins = table_head[2].text
#         fats = table_head[3].text
#         carbohydrates = table_head[4].text
        
#         with open(f"data/{category_name}.csv", 'w', encoding='utf-8') as file:
#             writer = csv.writer(file)
#             writer.writerow(
#                 (
#                     product,
#                     calories,
#                     proteins,
#                     fats,
#                     carbohydrates
#                 )
#             )
#         #sobiraem dannie
#         table_head = soup.find(class_='mzr-tc-group-table').find('tr').find_all('th')

#        for item in product_data:
#            product_data = item.find_all('td')
       
#         title = table_head[0].text
#         calories = table_head[1].text
#         proteins = table_head[2].text
#         fats = table_head[3].text
#         carbohydrates = table_head[4].text

#        with open(f"data/{category_name}.csv", 'a', 
#        encoding='utf-8') as file:
#             writer = csv.writer(file)
#             writer.writerow( 
#                 (
#                     title,
#                     calories,
#                     proteins,
#                     fats,
#                     carbohydrates
#                 )

#     count +=  




# from abc import ABC, abstractclassmethod 
 
# class AbstarchClass(ABC): 
     
#     @abstractclassmethod 
#     def hello(self): 
#         print("Я абстракный класс и чо сделаешь") 
 
# class Hello(AbstarchClass): 
#     def __init__(self, value): 
#         self.value = value 
 
#     def hello(self): 
#         super().hello() 
#         print(self.value) 
 
# hello = Hello("hi") 
# hello.hello()

# ###############################################
# from __future__ import ABC, abstractclassmethod

# class ChessPiece(ABC):
#     def draw(self):
#         print("Narisoval shahmatnuu figuru")

# @abstractclassmethod
# def move(self):
#     print("")



# class Baiel:
#     name = "Baiel"
#     age = 15

#     def info_about_human():
#         return f'{self.name}, {self.age}'


# class Baiel:
#     name = "Baiel"
#      age = 15

#      def__init__(self, name, age)
#          return f'{self.name}, {self.age}'

# baiel = Baiel("Baiel", ""15")
# print(baiel.info_about_human()











































