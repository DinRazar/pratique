# pratique
**1. Исследование структуры пакета**
а. Дополните схему дерева файлов и модулей пакета calculator, указав, какие модули и функции в них содержатся.<br>
В пакете basic: addition.py функция add(a, b) - сложение двух чисел subtraction.py функция subtract(a, b) - вычитание двух чисел<br>
В пакете advanced: exponentiation.py функция power(a, b) - возведение в степень (a^b) root.py функция square_root(a) - квадратный корень числа<br>
б. Объясните, какую роль играют файлы __init__.py в каждом каталоге пакета. Почему без них пакет не будет работать правильно?<br>
Файлы init.py содержат инструкции импорта, которые делают функции доступными непосредственно из пакетов<br>
**2. Работа с __init__.py**
а. Обратите внимание на использование переменной __all__ в файле calculator/__init__.py. Объясните, как она влияет на импорт пакета.<br>
Это обозначает, что будут экспортированы только модули ["basic", "advanced"]<br>
б. Удалите или закомментируйте строку __all__ = ["basic", "advanced"] в файле calculator/__init__.py. Попробуйте импортировать пакет снова:<br>
from calculator import basic<br>
Что произошло? Объясните причину возникшей проблемы.<br>
Если честно, ничего не поменялось<br>
в. Верните строку __all__ обратно. Попробуйте выполнить команду:<br>
from calculator import *<br>
Какие модули будут импортированы? Как можно управлять импортируемыми модулями с помощью __all__?<br>
Импортированы модули "basic" и "advanced"<br>
**3. Абсолютный и относительный импорт**<br>
а. В файле calculator/basic/__init__.py замените относительные импорты на абсолютные:<br>
from calculator.basic.addition import add<br>
from calculator.basic.subtraction import subtract<br>
Проверьте работоспособность пакета. Объясните разницу между относительным и абсолютным импортом. Какие преимущества и недостатки каждого из них?<br>
Всё работает без изменений!<br>
Указывает полный путь от корневого пакета<br>
Относительный от текущего пакета<br>
б. Предположим, что структура пакета изменилась, и папка basic была переименована в simple. Объясните, как это повлияет на абсолютные и относительные импорты. Какой импорт легче поддерживать при реорганизации структуры пакета?<br>
Абсолютные пути перестанут работать, но относительные остнаутся полностью работоспособными. Это делает из наиболее предпочтительным вариантом :)<br>
**4. Добавление новых модулей**<br>
а. Добавьте в пакет calculator/basic новый модуль multiplication.py с функцией multiply(a, b), которая возвращает произведение a и b.<br>
def multiply(a, b):<br>
    return a * b<br>
б. Обновите файл calculator/basic/__init__.py, чтобы функция multiply была доступна при импорте пакета.<br>
from .addition import add<br>
from .subtraction import subtract<br>
from .multiplication import multiply<br>
в. В файле main.py импортируйте новую функцию и протестируйте ее.<br>
from calculator.basic import multiply<br>
print(multiply(4, 5))        # Вывод: 20<br>
from calculator.basic import add, subtract, multiply<br>
from calculator.advanced import power, square_root<br>
print(add(2, 3))             # Вывод: 5<br>
print(subtract(5, 2))        # Вывод: 3<br>
print(power(2, 3))           # Вывод: 8<br>
print(square_root(16))       # Вывод: 4.0<br>
print(multiply(4, 5))<br>
**5. Исследование переменной __name__**<br>
а. В файле calculator/advanced/exponentiation.py добавьте следующий код:<br>
if __name__ == "__main__":<br>
    print(power(2, 5))<br>
б. Запустите файл exponentiation.py напрямую. Что произошло? Какой вывод вы получили?<br>
При запуске exponentiation.py код внутри блока if name == "main": выполняется, так как переменная name получает значение "main". В результате функция power(2, 5) вычисляется и выводится число 32. Это позволяет использовать файл как самостоятельную программу при прямом запуске, но не выполнять тестовый код при импорте модуля в другие программы.<br>
в. Импортируйте функцию power в main.py и запустите main.py. Выполняется ли код внутри блока if __name__ == "__main__": в файле exponentiation.py при импорте? Объясните, почему.<br>
При импорте функции power в main.py код внутри блока if name == "main" в файле exponentiation.py выполняется, потому что при импорте модуля переменная name получает значение имени модуля ("calculator.advanced.exponentiation"), а не "main". В противном же случае будет некоректный вывод, потомучто print(power(2, 5)) выполнится еще самостоятельно<br>
**6. Изучение путей поиска модулей**<br>
а. Выведите переменную sys.path в main.py:<br>
import sys<br>
print(sys.path)<br>
Ввод суса: ['/Users/dinrazar/Desktop/proj', '/Library/Frameworks/Python.framework/Versions/3.13/lib/python313.zip', '/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13', '/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages']<br>
В ней содержаться полные пути до рабочей директории, питону и его библиотекам<br>
б. Попробуйте переместить папку calculator в другую директорию, которая не входит в sys.path. Можете ли вы теперь импортировать пакет? Что нужно сделать, чтобы Python мог найти ваш пакет?<br>
Импорты не будут работать. Можно добавить путь sys.path.append()<br>
**7. Создание подпакетов**<br>
а. Внутри calculator/advanced создайте подпакет trigonometry с функциями sin, cos и tan. Структура должна выглядеть так:<br>
б. Реализуйте функции в соответствующих модулях, используя модуль math из стандартной библиотеки Python.<br>
в. Обновите __init__.py файлы, чтобы обеспечить корректный импорт функций.<br>
г. Импортируйте функции в main.py и протестируйте их.<br>
**8. Практика с относительным импортом**<br>
а. В файле calculator/advanced/trigonometry/sine.py попробуйте импортировать функцию square_root из модуля root.py двумя способами:<br>
Используя относительный импорт.<br>
Используя абсолютный импорт.<br>
б. Объясните, какой способ импорта сработал, а какой нет, и почему.<br>
Оба варината сработали. (from ..root import square_root) поднимается на выше и ищет файл root. (from calculator.advanced.root import square_root )прописывает полный путь до него.<br>

