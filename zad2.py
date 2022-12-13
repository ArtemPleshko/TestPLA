"""
Задача 2
Создать локальный json файл, формата:
{ "id": [
"name":"Имя" ,
"number":"укр моб номер телефона"
] }
наполнить пару значений
Реализовать чтения json файла,
вывод данных файла на экран,
функцию, которая  возвращают номер абонента без кода страны и кода оператора"
функцию которая возращает имя оператора в зависимости от кода номера (используем ток киевстар 096, водафон 050, лайф 093 в данных)  мо
"""

import json

with open('test2.json', 'r', encoding='utf-8') as f:
    templates = json.load(f)

print(templates)


  def is_complex(objct):
    if '__complex__' in objct:
      return complex(objct['real'], objct['img'])
    return objct



