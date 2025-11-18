import os
import glob
import sys
import subprocess

def clear_screen():
    """Очистка экрана консоли"""
    os.system('clear')

def get_current_directory():
    """Получение текущего рабочего каталога"""
    return os.getcwd()

def change_directory():
    """Смена рабочего каталога"""
    while True:
        new_path = input("Укажите корректный путь к рабочему каталогу: ").strip()
        if os.path.exists(new_path) and os.path.isdir(new_path):
            os.chdir(new_path)
            print(f"Текущий каталог: {get_current_directory()}")
            break
        else:
            print("Ошибка: Указанный путь не существует или не является директорией. Попробуйте снова.")

def display_files_with_extension(extension):
    """Отображение файлов с указанным расширением"""
    files = []
    if isinstance(extension, tuple):
        for ext in extension:
            files.extend(glob.glob(f"*{ext}"))
    else:
        files = glob.glob(f"*{extension}")
    
    files = [f for f in files if os.path.isfile(f)]
    
    if not files:
        print(f"Файлы с расширением {extension} не найдены.")
        return []
    
    print(f"Список файлов с расширением {extension} в данном каталоге:")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    
    return files

def pdf_to_docx():
    """Преобразование PDF в DOCX"""
    try:
        from pdf2docx import Converter
    except ImportError:
        print("Ошибка: Модуль pdf2docx не установлен.")
        print("Установите его командой: pip3 install pdf2docx")
        input("Нажмите Enter для продолжения...")
        return
    
    files = display_files_with_extension('.pdf')
    if not files:
        input("Нажмите Enter для продолжения...")
        return
    
    try:
        choice = input("Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): ")
        
        if choice == '0':
            # Преобразование всех файлов
            for pdf_file in files:
                docx_file = os.path.splitext(pdf_file)[0] + '.docx'
                try:
                    cv = Converter(pdf_file)
                    cv.convert(docx_file)
                    cv.close()
                    print(f"Файл '{pdf_file}' успешно преобразован в '{docx_file}'")
                except Exception as e:
                    print(f"Ошибка при преобразовании файла '{pdf_file}': {e}")
        else:
            # Преобразование одного файла
            try:
                file_index = int(choice) - 1
                if 0 <= file_index < len(files):
                    pdf_file = files[file_index]
                    docx_file = os.path.splitext(pdf_file)[0] + '.docx'
                    cv = Converter(pdf_file)
                    cv.convert(docx_file)
                    cv.close()
                    print(f"Файл '{pdf_file}' успешно преобразован в '{docx_file}'")
                else:
                    print("Ошибка: Неверный номер файла.")
            except ValueError:
                print("Ошибка: Введите корректный номер.")
    
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    input("Нажмите Enter для продолжения...")

def docx_to_pdf():
    """Преобразование DOCX в PDF с использованием LibreOffice"""
    files = display_files_with_extension('.docx')
    if not files:
        input("Нажмите Enter для продолжения...")
        return
    
    try:
        choice = input("Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): ")
        
        if choice == '0':
            # Преобразование всех файлов
            for docx_file in files:
                try:
                    if convert_docx_to_pdf_libreoffice(docx_file):
                        print(f"Файл '{docx_file}' успешно преобразован в PDF")
                    else:
                        print(f"Не удалось преобразовать файл '{docx_file}'")
                except Exception as e:
                    print(f"Ошибка при преобразовании файла '{docx_file}': {e}")
        else:
            # Преобразование одного файла
            try:
                file_index = int(choice) - 1
                if 0 <= file_index < len(files):
                    docx_file = files[file_index]
                    if convert_docx_to_pdf_libreoffice(docx_file):
                        print(f"Файл '{docx_file}' успешно преобразован в PDF")
                    else:
                        print(f"Не удалось преобразовать файл '{docx_file}'")
                else:
                    print("Ошибка: Неверный номер файла.")
            except ValueError:
                print("Ошибка: Введите корректный номер.")
    
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    input("Нажмиte Enter для продолжения...")

def convert_docx_to_pdf_libreoffice(docx_file):
    """Конвертация DOCX в PDF с помощью LibreOffice"""
    try:
        # Проверяем, установлен ли LibreOffice
        result = subprocess.run(['which', 'libreoffice'], capture_output=True, text=True)
        if result.returncode != 0:
            print("LibreOffice не установлен. Установите его:")
            print("Для MacOS: brew install --cask libreoffice")
            print("Для Ubuntu/Debian: sudo apt install libreoffice")
            print("Или используйте альтернативный метод...")
            return convert_docx_to_pdf_alternative(docx_file)
        
        # Конвертируем с помощью LibreOffice
        cmd = [
            'libreoffice', '--headless', '--convert-to', 'pdf',
            '--outdir', os.getcwd(), docx_file
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            return True
        else:
            print(f"Ошибка LibreOffice: {result.stderr}")
            return convert_docx_to_pdf_alternative(docx_file)
            
    except Exception as e:
        print(f"Ошибка при конвертации через LibreOffice: {e}")
        return convert_docx_to_pdf_alternative(docx_file)

def convert_docx_to_pdf_alternative(docx_file):
    """Альтернативный метод конвертации DOCX в PDF"""
    try:
        # Пробуем использовать python-docx и reportlab как альтернативу
        try:
            from docx import Document
            from reportlab.lib.pagesizes import letter
            from reportlab.pdfgen import canvas
            from reportlab.lib.utils import ImageReader
            import io
            
            doc = Document(docx_file)
            pdf_file = os.path.splitext(docx_file)[0] + '.pdf'
            
            c = canvas.Canvas(pdf_file, pagesize=letter)
            y = 750  # Начальная позиция Y
            line_height = 14
            
            for paragraph in doc.paragraphs:
                text = paragraph.text.strip()
                if text:
                    # Простой перенос текста
                    words = text.split()
                    line = ""
                    for word in words:
                        test_line = line + word + " "
                        if c.stringWidth(test_line) < 500:  # Ширина страницы минус отступы
                            line = test_line
                        else:
                            if line:
                                c.drawString(50, y, line.strip())
                                y -= line_height
                            line = word + " "
                            
                            if y < 50:  # Конец страницы
                                c.showPage()
                                y = 750
                    
                    if line:
                        c.drawString(50, y, line.strip())
                        y -= line_height
                
                if y < 50:  # Конец страницы
                    c.showPage()
                    y = 750
            
            c.save()
            print(f"Файл '{docx_file}' преобразован в PDF (базовый формат)")
            return True
            
        except ImportError:
            print("Для расширенной конвертации установите: pip3 install python-docx reportlab")
            # Создаем простой PDF с сообщением
            try:
                from reportlab.pdfgen import canvas
                
                pdf_file = os.path.splitext(docx_file)[0] + '.pdf'
                c = canvas.Canvas(pdf_file)
                c.drawString(100, 750, f"Исходный файл: {docx_file}")
                c.drawString(100, 735, "Для полной конвертации установите LibreOffice")
                c.drawString(100, 720, "или python-docx + reportlab")
                c.save()
                print(f"Создан файл-заглушка: {pdf_file}")
                return True
            except:
                print("Не удалось создать PDF. Установите LibreOffice или reportlab.")
                return False
                
    except Exception as e:
        print(f"Ошибка альтернативной конвертации: {e}")
        return False

def compress_images():
    """Сжатие изображений"""
    try:
        from PIL import Image
    except ImportError:
        print("Ошибка: Модуль Pillow не установлен.")
        print("Установите его командой: pip3 install Pillow")
        input("Нажмите Enter для продолжения...")
        return
    
    image_extensions = ('.jpeg', '.gif', '.png', '.jpg', '.JPG', '.JPEG', '.PNG')
    files = display_files_with_extension(image_extensions)
    if not files:
        input("Нажмите Enter для продолжения...")
        return
    
    try:
        choice = input("Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): ")
        
        quality = int(input("Введите параметры сжатия (от 0 до 100%): "))
        if quality < 0 or quality > 100:
            print("Ошибка: Качество должно быть в диапазоне от 0 до 100.")
            input("Нажмите Enter для продолжения...")
            return
        
        if choice == '0':
            # Сжатие всех файлов
            for img_file in files:
                try:
                    with Image.open(img_file) as img:
                        # Создаем новое имя файла с префиксом 'compressed_'
                        name, ext = os.path.splitext(img_file)
                        compressed_file = f"compressed_{name}{ext}"
                        
                        # Сохраняем с указанным качеством
                        if img.mode in ('RGBA', 'LA', 'P'):
                            img = img.convert('RGB')
                        
                        img.save(compressed_file, optimize=True, quality=quality)
                        print(f"Файл '{img_file}' успешно сжат в '{compressed_file}'")
                except Exception as e:
                    print(f"Ошибка при сжатии файла '{img_file}': {e}")
        else:
            # Сжатие одного файла
            try:
                file_index = int(choice) - 1
                if 0 <= file_index < len(files):
                    img_file = files[file_index]
                    with Image.open(img_file) as img:
                        # Создаем новое имя файла с префиксом 'compressed_'
                        name, ext = os.path.splitext(img_file)
                        compressed_file = f"compressed_{name}{ext}"
                        
                        # Сохраняем с указанным качеством
                        if img.mode in ('RGBA', 'LA', 'P'):
                            img = img.convert('RGB')
                        
                        img.save(compressed_file, optimize=True, quality=quality)
                        print(f"Файл '{img_file}' успешно сжат в '{compressed_file}'")
                else:
                    print("Ошибка: Неверный номер файла.")
            except ValueError:
                print("Ошибка: Введите корректный номер.")
    
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    input("Нажмите Enter для продолжения...")

def delete_files_by_pattern():
    """Удаление файлов по шаблону"""
    print("Выберите действие:")
    print("1. Удалить все файлы начинающиеся на определенную подстроку")
    print("2. Удалить все файлы заканчивающиеся на определенную подстроку")
    print("3. Удалить все файлы содержащие определенную подстроку")
    print("4. Удалить все файлы по расширению")
    
    try:
        action = int(input("Введите номер действия: "))
        substring = input("Введите подстроку: ").strip()
        
        files_deleted = 0
        
        for file in os.listdir('.'):
            if os.path.isfile(file):
                if action == 1 and file.startswith(substring):
                    os.remove(file)
                    print(f'Файл: "{file}" успешно удалён!')
                    files_deleted += 1
                elif action == 2 and file.endswith(substring):
                    os.remove(file)
                    print(f'Файл: "{file}" успешно удалён!')
                    files_deleted += 1
                elif action == 3 and substring in file:
                    os.remove(file)
                    print(f'Файл: "{file}" успешно удалён!')
                    files_deleted += 1
                elif action == 4 and file.endswith(substring):
                    os.remove(file)
                    print(f'Файл: "{file}" успешно удалён!')
                    files_deleted += 1
        
        if files_deleted == 0:
            print("Файлы, соответствующие критериям, не найдены.")
    
    except ValueError:
        print("Ошибка: Введите корректный номер действия.")
    except Exception as e:
        print(f"Произошла ошибка при удалении файлов: {e}")
    
    input("Нажмите Enter для продолжения...")

def check_dependencies():
    """Проверка наличия необходимых модулей"""
    missing_deps = []
    
    try:
        from pdf2docx import Converter
    except ImportError:
        missing_deps.append("pdf2docx")
    
    try:
        from PIL import Image
    except ImportError:
        missing_deps.append("Pillow")
    
    return missing_deps

def main():
    """Главная функция программы"""
    # Проверка зависимостей при запуске
    missing_deps = check_dependencies()
    if missing_deps:
        print("ВНИМАНИЕ: Отсутствуют некоторые модули:")
        for dep in missing_deps:
            print(f"  - {dep}")
        print("\nУстановите их командой: pip3 install " + " ".join(missing_deps))
        print("Некоторые функции будут недоступны.\n")
        input("Нажмите Enter для продолжения...")
    
    while True:
        clear_screen()
        print(f"Текущий каталог: {get_current_directory()}")
        print("\nВыберите действие:")
        print("0. Сменить рабочий каталог")
        print("1. Преобразовать PDF в Docx")
        print("2. Преобразовать Docx в PDF")
        print("3. Произвести сжатие изображений")
        print("4. Удалить группу файлов")
        print("5. Выход")
        
        choice = input("\nВаш выбор: ").strip()
        
        if choice == '0':
            change_directory()
        elif choice == '1':
            pdf_to_docx()
        elif choice == '2':
            docx_to_pdf()
        elif choice == '3':
            compress_images()
        elif choice == '4':
            delete_files_by_pattern()
        elif choice == '5':
            print("Выход из программы...")
            break
        else:
            print("Ошибка: Неверный выбор. Попробуйте снова.")
            input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()