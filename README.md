# pratique
## 1. Исследование структуры пакета
а. Дополните схему дерева файлов и модулей пакета calculator, указав, какие модули и функции в них содержатся.

        calculator/
        ├── __init__.py
        ├── basic/
        │   ├── __init__.py
        │   ├── addition.py
        │   └── subtraction.py
        └── advanced/
            ├── __init__.py
            ├── exponentiation.py
            └── root.py
В пакете basic: addition.py функция add(a, b) - сложение двух чисел subtraction.py функция subtract(a, b) - вычитание двух чисел

В пакете advanced: exponentiation.py функция power(a, b) - возведение в степень (a^b) root.py функция square_root(a) - квадратный корень числа

б. Объясните, какую роль играют файлы __init__.py в каждом каталоге пакета. Почему без них пакет не будет работать правильно? <br>
## 2. Работа с __init__.py

Файлы init.py содержат инструкции импорта, которые делают функции доступными непосредственно из пакетов

а. Обратите внимание на использование переменной __all__ в файле calculator/__init__.py. Объясните, как она влияет на импорт пакета.

Это обозначает, что будут экспортированы только модули ["basic", "advanced"]

б. Удалите или закомментируйте строку __all__ = ["basic", "advanced"] в файле calculator/__init__.py. Попробуйте импортировать пакет снова:

Что произошло? Объясните причину возникшей проблемы.

Если честно, ничего не поменялось
в. Верните строку __all__ обратно. Попробуйте выполнить команду:

Какие модули будут импортированы? Как можно управлять импортируемыми модулями с помощью __all__?

Импортированы модули "basic" и "advanced" <br>

## 3. Абсолютный и относительный импорт

а. В файле calculator/basic/__init__.py замените относительные импорты на абсолютные:



                from calculator.basic.addition import add
                from calculator.basic.subtraction import subtract
Проверьте работоспособность пакета. Объясните разницу между относительным и абсолютным импортом. Какие преимущества и недостатки каждого из них?

Всё работает без изменений!

Указывает полный путь от корневого пакета

Относительный от текущего пакета

б. Предположим, что структура пакета изменилась, и папка basic была переименована в simple. Объясните, как это повлияет на абсолютные и относительные импорты. Какой импорт легче поддерживать при реорганизации структуры пакета?

Абсолютные пути перестанут работать, но относительные остнаутся полностью работоспособными. Это делает из наиболее предпочтительным вариантом :)

## 4. Добавление новых модулей
а. Добавьте в пакет calculator/basic новый модуль multiplication.py с функцией multiply(a, b), которая возвращает произведение a и b.

                def multiply(a, b):
                    return a * b
б. Обновите файл calculator/basic/__init__.py, чтобы функция multiply была доступна при импорте пакета.


                from .addition import add
                from .subtraction import subtract
                from .multiplication import multiply
в. В файле main.py импортируйте новую функцию и протестируйте ее.



                from calculator.basic import multiply
                print(multiply(4, 5))        # Вывод: 20

                from calculator.basic import add, subtract, multiply
                from calculator.advanced import power, square_root

                print(add(2, 3))             # Вывод: 5
                print(subtract(5, 2))        # Вывод: 3
                print(power(2, 3))           # Вывод: 8
                print(square_root(16))       # Вывод: 4.0
                print(multiply(4, 5))
## 5. Исследование переменной __name__
а. В файле calculator/advanced/exponentiation.py добавьте следующий код:

                if __name__ == "__main__":
                    print(power(2, 5))
б. Запустите файл exponentiation.py напрямую. Что произошло? Какой вывод вы получили?

При запуске exponentiation.py код внутри блока if name == "main": выполняется, так как переменная name получает значение "main". В результате функция power(2, 5) вычисляется и выводится число 32. Это позволяет использовать файл как самостоятельную программу при прямом запуске, но не выполнять тестовый код при импорте модуля в другие программы.

в. Импортируйте функцию power в main.py и запустите main.py. Выполняется ли код внутри блока if __name__ == "__main__": в файле exponentiation.py при импорте? Объясните, почему.

При импорте функции power в main.py код внутри блока if name == "main" в файле exponentiation.py выполняется, потому что при импорте модуля переменная name получает значение имени модуля ("calculator.advanced.exponentiation"), а не "main". В противном же случае будет некоректный вывод, потомучто print(power(2, 5)) выполнится еще самостоятельно

## 6. Изучение путей поиска модулей
а. Выведите переменную sys.path в main.py:

                import sys
                print(sys.path)
   
Ввод суса: <br>
['/Users/dinrazar/Desktop/proj', '/Library/Frameworks/Python.framework/Versions/3.13/lib/python313.zip', '/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13', '/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages']

В ней содержаться полные пути до рабочей директории, питону и его библиотекам

б. Попробуйте переместить папку calculator в другую директорию, которая не входит в sys.path. Можете ли вы теперь импортировать пакет? Что нужно сделать, чтобы Python мог найти ваш пакет?

Импорты не будут работать. Можно добавить путь sys.path.append()

## 7. Создание подпакетов
а. Внутри calculator/advanced создайте подпакет trigonometry с функциями sin, cos и tan. Структура должна выглядеть так:


        [ ]
        calculator/
        └── advanced/
            ├── trigonometry/
            │   ├── __init__.py
            │   ├── sine.py
            │   ├── cosine.py
            │   └── tangent.py
б. Реализуйте функции в соответствующих модулях, используя модуль math из стандартной библиотеки Python.

в. Обновите __init__.py файлы, чтобы обеспечить корректный импорт функций.

г. Импортируйте функции в main.py и протестируйте их.

## 8. Практика с относительным импортом
а. В файле calculator/advanced/trigonometry/sine.py попробуйте импортировать функцию square_root из модуля root.py двумя способами:

Используя относительный импорт.
Используя абсолютный импорт.
б. Объясните, какой способ импорта сработал, а какой нет, и почему.

Оба варината сработали. (from ..root import square_root) поднимается на выше и ищет файл root. (from calculator.advanced.root import square_root )прописывает полный путь до него.
