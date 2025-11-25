# import os
# import glob
# import sys
# import subprocess

# def clear_screen():
#     """Очистка экрана консоли"""
#     os.system('clear')

# def get_current_directory():
#     """Получение текущего рабочего каталога"""
#     return os.getcwd()

# def change_directory():
#     """Смена рабочего каталога"""
#     while True:
#         new_path = input("Укажите корректный путь к рабочему каталогу: ").strip()
#         if os.path.exists(new_path) and os.path.isdir(new_path):
#             os.chdir(new_path)
#             print(f"Текущий каталог: {get_current_directory()}")
#             break
#         else:
#             print("Ошибка: Указанный путь не существует или не является директорией. Попробуйте снова.")

# def display_files_with_extension(extension):
#     """Отображение файлов с указанным расширением"""
#     files = []
#     if isinstance(extension, tuple):
#         for ext in extension:
#             files.extend(glob.glob(f"*{ext}"))
#     else:
#         files = glob.glob(f"*{extension}")
    
#     files = [f for f in files if os.path.isfile(f)]
    
#     if not files:
#         print(f"Файлы с расширением {extension} не найдены.")
#         return []
    
#     print(f"Список файлов с расширением {extension} в данном каталоге:")
#     for i, file in enumerate(files, 1):
#         print(f"{i}. {file}")
    
#     return files

# def pdf_to_docx():
#     """Преобразование PDF в DOCX"""
#     try:
#         from pdf2docx import Converter
#     except ImportError:
#         print("Ошибка: Модуль pdf2docx не установлен.")
#         print("Установите его командой: pip3 install pdf2docx")
#         input("Нажмите Enter для продолжения...")
#         return
    
#     files = display_files_with_extension('.pdf')
#     if not files:
#         input("Нажмите Enter для продолжения...")
#         return
    
#     try:
#         choice = input("Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): ")
        
#         if choice == '0':
#             # Преобразование всех файлов
#             for pdf_file in files:
#                 docx_file = os.path.splitext(pdf_file)[0] + '.docx'
#                 try:
#                     cv = Converter(pdf_file)
#                     cv.convert(docx_file)
#                     cv.close()
#                     print(f"Файл '{pdf_file}' успешно преобразован в '{docx_file}'")
#                 except Exception as e:
#                     print(f"Ошибка при преобразовании файла '{pdf_file}': {e}")
#         else:
#             # Преобразование одного файла
#             try:
#                 file_index = int(choice) - 1
#                 if 0 <= file_index < len(files):
#                     pdf_file = files[file_index]
#                     docx_file = os.path.splitext(pdf_file)[0] + '.docx'
#                     cv = Converter(pdf_file)
#                     cv.convert(docx_file)
#                     cv.close()
#                     print(f"Файл '{pdf_file}' успешно преобразован в '{docx_file}'")
#                 else:
#                     print("Ошибка: Неверный номер файла.")
#             except ValueError:
#                 print("Ошибка: Введите корректный номер.")
    
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
    
#     input("Нажмите Enter для продолжения...")

# def docx_to_pdf():
#     """Преобразование DOCX в PDF с использованием LibreOffice"""
#     files = display_files_with_extension('.docx')
#     if not files:
#         input("Нажмите Enter для продолжения...")
#         return
    
#     try:
#         choice = input("Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): ")
        
#         if choice == '0':
#             # Преобразование всех файлов
#             for docx_file in files:
#                 try:
#                     if convert_docx_to_pdf_libreoffice(docx_file):
#                         print(f"Файл '{docx_file}' успешно преобразован в PDF")
#                     else:
#                         print(f"Не удалось преобразовать файл '{docx_file}'")
#                 except Exception as e:
#                     print(f"Ошибка при преобразовании файла '{docx_file}': {e}")
#         else:
#             # Преобразование одного файла
#             try:
#                 file_index = int(choice) - 1
#                 if 0 <= file_index < len(files):
#                     docx_file = files[file_index]
#                     if convert_docx_to_pdf_libreoffice(docx_file):
#                         print(f"Файл '{docx_file}' успешно преобразован в PDF")
#                     else:
#                         print(f"Не удалось преобразовать файл '{docx_file}'")
#                 else:
#                     print("Ошибка: Неверный номер файла.")
#             except ValueError:
#                 print("Ошибка: Введите корректный номер.")
    
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
    
#     input("Нажмиte Enter для продолжения...")

# def convert_docx_to_pdf_libreoffice(docx_file):
#     """Конвертация DOCX в PDF с помощью LibreOffice"""
#     try:
#         # Проверяем, установлен ли LibreOffice
#         result = subprocess.run(['which', 'libreoffice'], capture_output=True, text=True)
#         if result.returncode != 0:
#             print("LibreOffice не установлен. Установите его:")
#             print("Для MacOS: brew install --cask libreoffice")
#             print("Для Ubuntu/Debian: sudo apt install libreoffice")
#             print("Или используйте альтернативный метод...")
#             return convert_docx_to_pdf_alternative(docx_file)
        
#         # Конвертируем с помощью LibreOffice
#         cmd = [
#             'libreoffice', '--headless', '--convert-to', 'pdf',
#             '--outdir', os.getcwd(), docx_file
#         ]
        
#         result = subprocess.run(cmd, capture_output=True, text=True)
#         if result.returncode == 0:
#             return True
#         else:
#             print(f"Ошибка LibreOffice: {result.stderr}")
#             return convert_docx_to_pdf_alternative(docx_file)
            
#     except Exception as e:
#         print(f"Ошибка при конвертации через LibreOffice: {e}")
#         return convert_docx_to_pdf_alternative(docx_file)

# def convert_docx_to_pdf_alternative(docx_file):
#     """Альтернативный метод конвертации DOCX в PDF"""
#     try:
#         # Пробуем использовать python-docx и reportlab как альтернативу
#         try:
#             from docx import Document
#             from reportlab.lib.pagesizes import letter
#             from reportlab.pdfgen import canvas
#             from reportlab.lib.utils import ImageReader
#             import io
            
#             doc = Document(docx_file)
#             pdf_file = os.path.splitext(docx_file)[0] + '.pdf'
            
#             c = canvas.Canvas(pdf_file, pagesize=letter)
#             y = 750  # Начальная позиция Y
#             line_height = 14
            
#             for paragraph in doc.paragraphs:
#                 text = paragraph.text.strip()
#                 if text:
#                     # Простой перенос текста
#                     words = text.split()
#                     line = ""
#                     for word in words:
#                         test_line = line + word + " "
#                         if c.stringWidth(test_line) < 500:  # Ширина страницы минус отступы
#                             line = test_line
#                         else:
#                             if line:
#                                 c.drawString(50, y, line.strip())
#                                 y -= line_height
#                             line = word + " "
                            
#                             if y < 50:  # Конец страницы
#                                 c.showPage()
#                                 y = 750
                    
#                     if line:
#                         c.drawString(50, y, line.strip())
#                         y -= line_height
                
#                 if y < 50:  # Конец страницы
#                     c.showPage()
#                     y = 750
            
#             c.save()
#             print(f"Файл '{docx_file}' преобразован в PDF (базовый формат)")
#             return True
            
#         except ImportError:
#             print("Для расширенной конвертации установите: pip3 install python-docx reportlab")
#             # Создаем простой PDF с сообщением
#             try:
#                 from reportlab.pdfgen import canvas
                
#                 pdf_file = os.path.splitext(docx_file)[0] + '.pdf'
#                 c = canvas.Canvas(pdf_file)
#                 c.drawString(100, 750, f"Исходный файл: {docx_file}")
#                 c.drawString(100, 735, "Для полной конвертации установите LibreOffice")
#                 c.drawString(100, 720, "или python-docx + reportlab")
#                 c.save()
#                 print(f"Создан файл-заглушка: {pdf_file}")
#                 return True
#             except:
#                 print("Не удалось создать PDF. Установите LibreOffice или reportlab.")
#                 return False
                
#     except Exception as e:
#         print(f"Ошибка альтернативной конвертации: {e}")
#         return False

# def compress_images():
#     """Сжатие изображений"""
#     try:
#         from PIL import Image
#     except ImportError:
#         print("Ошибка: Модуль Pillow не установлен.")
#         print("Установите его командой: pip3 install Pillow")
#         input("Нажмите Enter для продолжения...")
#         return
    
#     image_extensions = ('.jpeg', '.gif', '.png', '.jpg', '.JPG', '.JPEG', '.PNG')
#     files = display_files_with_extension(image_extensions)
#     if not files:
#         input("Нажмите Enter для продолжения...")
#         return
    
#     try:
#         choice = input("Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): ")
        
#         quality = int(input("Введите параметры сжатия (от 0 до 100%): "))
#         if quality < 0 or quality > 100:
#             print("Ошибка: Качество должно быть в диапазоне от 0 до 100.")
#             input("Нажмите Enter для продолжения...")
#             return
        
#         if choice == '0':
#             # Сжатие всех файлов
#             for img_file in files:
#                 try:
#                     with Image.open(img_file) as img:
#                         # Создаем новое имя файла с префиксом 'compressed_'
#                         name, ext = os.path.splitext(img_file)
#                         compressed_file = f"compressed_{name}{ext}"
                        
#                         # Сохраняем с указанным качеством
#                         if img.mode in ('RGBA', 'LA', 'P'):
#                             img = img.convert('RGB')
                        
#                         img.save(compressed_file, optimize=True, quality=quality)
#                         print(f"Файл '{img_file}' успешно сжат в '{compressed_file}'")
#                 except Exception as e:
#                     print(f"Ошибка при сжатии файла '{img_file}': {e}")
#         else:
#             # Сжатие одного файла
#             try:
#                 file_index = int(choice) - 1
#                 if 0 <= file_index < len(files):
#                     img_file = files[file_index]
#                     with Image.open(img_file) as img:
#                         # Создаем новое имя файла с префиксом 'compressed_'
#                         name, ext = os.path.splitext(img_file)
#                         compressed_file = f"compressed_{name}{ext}"
                        
#                         # Сохраняем с указанным качеством
#                         if img.mode in ('RGBA', 'LA', 'P'):
#                             img = img.convert('RGB')
                        
#                         img.save(compressed_file, optimize=True, quality=quality)
#                         print(f"Файл '{img_file}' успешно сжат в '{compressed_file}'")
#                 else:
#                     print("Ошибка: Неверный номер файла.")
#             except ValueError:
#                 print("Ошибка: Введите корректный номер.")
    
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")
    
#     input("Нажмите Enter для продолжения...")

# def delete_files_by_pattern():
#     """Удаление файлов по шаблону"""
#     print("Выберите действие:")
#     print("1. Удалить все файлы начинающиеся на определенную подстроку")
#     print("2. Удалить все файлы заканчивающиеся на определенную подстроку")
#     print("3. Удалить все файлы содержащие определенную подстроку")
#     print("4. Удалить все файлы по расширению")
    
#     try:
#         action = int(input("Введите номер действия: "))
#         substring = input("Введите подстроку: ").strip()
        
#         files_deleted = 0
        
#         for file in os.listdir('.'):
#             if os.path.isfile(file):
#                 if action == 1 and file.startswith(substring):
#                     os.remove(file)
#                     print(f'Файл: "{file}" успешно удалён!')
#                     files_deleted += 1
#                 elif action == 2 and file.endswith(substring):
#                     os.remove(file)
#                     print(f'Файл: "{file}" успешно удалён!')
#                     files_deleted += 1
#                 elif action == 3 and substring in file:
#                     os.remove(file)
#                     print(f'Файл: "{file}" успешно удалён!')
#                     files_deleted += 1
#                 elif action == 4 and file.endswith(substring):
#                     os.remove(file)
#                     print(f'Файл: "{file}" успешно удалён!')
#                     files_deleted += 1
        
#         if files_deleted == 0:
#             print("Файлы, соответствующие критериям, не найдены.")
    
#     except ValueError:
#         print("Ошибка: Введите корректный номер действия.")
#     except Exception as e:
#         print(f"Произошла ошибка при удалении файлов: {e}")
    
#     input("Нажмите Enter для продолжения...")

# def check_dependencies():
#     """Проверка наличия необходимых модулей"""
#     missing_deps = []
    
#     try:
#         from pdf2docx import Converter
#     except ImportError:
#         missing_deps.append("pdf2docx")
    
#     try:
#         from PIL import Image
#     except ImportError:
#         missing_deps.append("Pillow")
    
#     return missing_deps

# def main():
#     """Главная функция программы"""
#     # Проверка зависимостей при запуске
#     missing_deps = check_dependencies()
#     if missing_deps:
#         print("ВНИМАНИЕ: Отсутствуют некоторые модули:")
#         for dep in missing_deps:
#             print(f"  - {dep}")
#         print("\nУстановите их командой: pip3 install " + " ".join(missing_deps))
#         print("Некоторые функции будут недоступны.\n")
#         input("Нажмите Enter для продолжения...")
    
#     while True:
#         clear_screen()
#         print(f"Текущий каталог: {get_current_directory()}")
#         print("\nВыберите действие:")
#         print("0. Сменить рабочий каталог")
#         print("1. Преобразовать PDF в Docx")
#         print("2. Преобразовать Docx в PDF")
#         print("3. Произвести сжатие изображений")
#         print("4. Удалить группу файлов")
#         print("5. Выход")
        
#         choice = input("\nВаш выбор: ").strip()
        
#         if choice == '0':
#             change_directory()
#         elif choice == '1':
#             pdf_to_docx()
#         elif choice == '2':
#             docx_to_pdf()
#         elif choice == '3':
#             compress_images()
#         elif choice == '4':
#             delete_files_by_pattern()
#         elif choice == '5':
#             print("Выход из программы...")
#             break
#         else:
#             print("Ошибка: Неверный выбор. Попробуйте снова.")
#             input("Нажмите Enter для продолжения...")

# if __name__ == "__main__":
#     main()


# # import os
# # import glob
# # import shutil
# # from pathlib import Path
# # import sys

# # # Для конвертации PDF в DOCX
# # try:
# #     from pdf2docx import Converter
# # except ImportError:
# #     print("Библиотека pdf2docx не установлена. Установите: pip install pdf2docx")

# # # Для конвертации DOCX в PDF
# # try:
# #     from docx2pdf import convert
# # except ImportError:
# #     print("Библиотека docx2pdf не установлена. Установите: pip install docx2pdf")

# # # Для работы с изображениями
# # try:
# #     from PIL import Image
# # except ImportError:
# #     print("Библиотека Pillow не установлена. Установите: pip install Pillow")


# # class OfficeTweaks:
# #     def __init__(self):
# #         self.current_dir = os.getcwd()
    
# #     def clear_screen(self):
# #         """Очистка экрана консоли"""
# #         os.system('cls' if os.name == 'nt' else 'clear')
    
# #     def display_menu(self):
# #         """Отображение главного меню"""
# #         print(f"\nТекущий каталог: {self.current_dir}")
# #         print("\nВыберите действие:")
# #         print("0. Сменить рабочий каталог")
# #         print("1. Преобразовать PDF в DOCX")
# #         print("2. Преобразовать DOCX в PDF")
# #         print("3. Произвести сжатие изображений")
# #         print("4. Удалить группу файлов")
# #         print("5. Выход")
    
# #     def change_directory(self):
# #         """Смена рабочего каталога"""
# #         new_path = input("Укажите корректный путь к рабочему каталогу: ").strip()
        
# #         if os.path.exists(new_path) and os.path.isdir(new_path):
# #             self.current_dir = new_path
# #             os.chdir(new_path)
# #             print(f"Рабочий каталог изменен на: {self.current_dir}")
# #         else:
# #             print("Ошибка: указанный путь не существует или не является директорией!")
    
# #     def get_files_by_extension(self, extensions):
# #         """Получить файлы по расширениям"""
# #         files = []
# #         for ext in extensions:
# #             pattern = os.path.join(self.current_dir, f"*{ext}")
# #             files.extend(glob.glob(pattern))
        
# #         # Фильтруем только файлы (не директории)
# #         files = [f for f in files if os.path.isfile(f)]
        
# #         # Получаем только имена файлов
# #         file_names = [os.path.basename(f) for f in files]
# #         return file_names, files
    
# #     def display_file_list(self, files, title):
# #         """Отображение списка файлов"""
# #         print(f"\n{title}:")
# #         if not files:
# #             print("Файлы не найдены.")
# #             return False
        
# #         for i, file in enumerate(files, 1):
# #             print(f"{i}. {file}")
# #         return True
    
# #     def pdf_to_docx(self):
# #         """Конвертация PDF в DOCX"""
# #         try:
# #             pdf_files, pdf_paths = self.get_files_by_extension(['.pdf'])
            
# #             if not self.display_file_list(pdf_files, "Список файлов с расширением .pdf в данном каталоге"):
# #                 return
            
# #             choice = input("\nВведите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): ")
            
# #             if choice == '0':
# #                 # Конвертировать все файлы
# #                 for pdf_path in pdf_paths:
# #                     self.convert_single_pdf_to_docx(pdf_path)
# #             else:
# #                 # Конвертировать один файл
# #                 try:
# #                     index = int(choice) - 1
# #                     if 0 <= index < len(pdf_paths):
# #                         self.convert_single_pdf_to_docx(pdf_paths[index])
# #                     else:
# #                         print("Ошибка: неверный номер файла!")
# #                 except ValueError:
# #                     print("Ошибка: введите корректный номер!")
                    
# #         except Exception as e:
# #             print(f"Ошибка при конвертации PDF в DOCX: {e}")
    
# #     def convert_single_pdf_to_docx(self, pdf_path):
# #         """Конвертация одного PDF файла в DOCX"""
# #         try:
# #             docx_path = pdf_path.replace('.pdf', '.docx')
# #             cv = Converter(pdf_path)
# #             cv.convert(docx_path, start=0, end=None)
# #             cv.close()
# #             print(f"Файл '{os.path.basename(pdf_path)}' успешно преобразован в DOCX!")
# #         except Exception as e:
# #             print(f"Ошибка при конвертации файла '{os.path.basename(pdf_path)}': {e}")
    
# #     def docx_to_pdf(self):
# #         """Конвертация DOCX в PDF"""
# #         try:
# #             docx_files, docx_paths = self.get_files_by_extension(['.docx'])
            
# #             if not self.display_file_list(docx_files, "Список файлов с расширением .docx в данном каталоге"):
# #                 return
            
# #             choice = input("\nВведите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): ")
            
# #             if choice == '0':
# #                 # Конвертировать все файлы
# #                 for docx_path in docx_paths:
# #                     self.convert_single_docx_to_pdf(docx_path)
# #             else:
# #                 # Конвертировать один файл
# #                 try:
# #                     index = int(choice) - 1
# #                     if 0 <= index < len(docx_paths):
# #                         self.convert_single_docx_to_pdf(docx_paths[index])
# #                     else:
# #                         print("Ошибка: неверный номер файла!")
# #                 except ValueError:
# #                     print("Ошибка: введите корректный номер!")
                    
# #         except Exception as e:
# #             print(f"Ошибка при конвертации DOCX в PDF: {e}")
    
# #     def convert_single_docx_to_pdf(self, docx_path):
# #         """Конвертация одного DOCX файла в PDF"""
# #         try:
# #             pdf_path = docx_path.replace('.docx', '.pdf')
# #             convert(docx_path, pdf_path)
# #             print(f"Файл '{os.path.basename(docx_path)}' успешно преобразован в PDF!")
# #         except Exception as e:
# #             print(f"Ошибка при конвертации файла '{os.path.basename(docx_path)}': {e}")
    
# #     def compress_images(self):
# #         """Сжатие изображений"""
# #         try:
# #             image_extensions = ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff']
# #             image_files, image_paths = self.get_files_by_extension(image_extensions)
            
# #             if not self.display_file_list(image_files, "Список файлов с изображениями в данном каталоге"):
# #                 return
            
# #             choice = input("\nВведите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): ")
            
# #             if choice == '0':
# #                 # Сжать все изображения
# #                 quality = self.get_compression_quality()
# #                 for img_path in image_paths:
# #                     self.compress_single_image(img_path, quality)
# #             else:
# #                 # Сжать одно изображение
# #                 try:
# #                     index = int(choice) - 1
# #                     if 0 <= index < len(image_paths):
# #                         quality = self.get_compression_quality()
# #                         self.compress_single_image(image_paths[index], quality)
# #                     else:
# #                         print("Ошибка: неверный номер файла!")
# #                 except ValueError:
# #                     print("Ошибка: введите корректный номер!")
                    
# #         except Exception as e:
# #             print(f"Ошибка при сжатии изображений: {e}")
    
# #     def get_compression_quality(self):
# #         """Получение параметра сжатия от пользователя"""
# #         while True:
# #             try:
# #                 quality = int(input("Введите параметры сжатия (от 0 до 100%): "))
# #                 if 0 <= quality <= 100:
# #                     return quality
# #                 else:
# #                     print("Ошибка: введите число от 0 до 100!")
# #             except ValueError:
# #                 print("Ошибка: введите целое число!")
    
# #     def compress_single_image(self, image_path, quality):
# #         """Сжатие одного изображения"""
# #         try:
# #             img = Image.open(image_path)
            
# #             # Сохраняем с новым качеством
# #             if image_path.lower().endswith(('.jpg', '.jpeg')):
# #                 img.save(image_path, 'JPEG', quality=quality, optimize=True)
# #             elif image_path.lower().endswith('.png'):
# #                 # Для PNG используем оптимизацию вместо качества
# #                 img.save(image_path, 'PNG', optimize=True)
# #             else:
# #                 # Для других форматов просто пересохраняем
# #                 img.save(image_path)
            
# #             print(f"Изображение '{os.path.basename(image_path)}' успешно сжато!")
            
# #         except Exception as e:
# #             print(f"Ошибка при сжатии изображения '{os.path.basename(image_path)}': {e}")
    
# #     def delete_files_menu(self):
# #         """Меню удаления файлов"""
# #         print("\nВыберите действие:")
# #         print("1. Удалить все файлы начинающиеся на определенную подстроку")
# #         print("2. Удалить все файлы заканчивающиеся на определенную подстроку")
# #         print("3. Удалить все файлы содержащие определенную подстроку")
# #         print("4. Удалить все файлы по расширению")
        
# #         try:
# #             action = int(input("Введите номер действия: "))
# #             substring = input("Введите подстроку: ").strip()
            
# #             if action == 1:
# #                 self.delete_files_by_pattern(lambda x: x.startswith(substring), f"начинающиеся на '{substring}'")
# #             elif action == 2:
# #                 self.delete_files_by_pattern(lambda x: x.endswith(substring), f"заканчивающиеся на '{substring}'")
# #             elif action == 3:
# #                 self.delete_files_by_pattern(lambda x: substring in x, f"содержащие '{substring}'")
# #             elif action == 4:
# #                 # Добавляем точку если её нет
# #                 if not substring.startswith('.'):
# #                     substring = '.' + substring
# #                 self.delete_files_by_pattern(lambda x: x.endswith(substring), f"с расширением '{substring}'")
# #             else:
# #                 print("Ошибка: неверный номер действия!")
                
# #         except ValueError:
# #             print("Ошибка: введите корректный номер!")
    
# #     def delete_files_by_pattern(self, pattern_func, description):
# #         """Удаление файлов по шаблону"""
# #         try:
# #             deleted_count = 0
# #             for filename in os.listdir(self.current_dir):
# #                 filepath = os.path.join(self.current_dir, filename)
                
# #                 # Проверяем, что это файл (не директория) и соответствует шаблону
# #                 if os.path.isfile(filepath) and pattern_func(filename):
# #                     os.remove(filepath)
# #                     print(f"Файл: '{filename}' успешно удалён!")
# #                     deleted_count += 1
            
# #             if deleted_count == 0:
# #                 print(f"Файлы {description} не найдены.")
# #             else:
# #                 print(f"Удалено файлов: {deleted_count}")
                
# #         except Exception as e:
# #             print(f"Ошибка при удалении файлов: {e}")
    
# #     def run(self):
# #         """Запуск основной программы"""
# #         self.clear_screen()
        
# #         while True:
# #             self.display_menu()
# #             choice = input("\nВаш выбор: ").strip()
            
# #             if choice == '0':
# #                 self.change_directory()
# #             elif choice == '1':
# #                 self.pdf_to_docx()
# #             elif choice == '2':
# #                 self.docx_to_pdf()
# #             elif choice == '3':
# #                 self.compress_images()
# #             elif choice == '4':
# #                 self.delete_files_menu()
# #             elif choice == '5':
# #                 print("Выход из программы...")
# #                 break
# #             else:
# #                 print("Ошибка: неверный выбор! Попробуйте снова.")
            
# #             input("\nНажмите Enter для продолжения...")
# #             self.clear_screen()


# # if __name__ == "__main__":
# #     # Проверка доступности необходимых библиотек
# #     try:
# #         from pdf2docx import Converter
# #         from docx2pdf import convert
# #         from PIL import Image
# #     except ImportError as e:
# #         print(f"Ошибка: Не все необходимые библиотеки установлены: {e}")
# #         print("Установите их с помощью команд:")
# #         print("pip install pdf2docx docx2pdf Pillow")
# #         sys.exit(1)
    
# #     app = OfficeTweaks()
# #     app.run()


import os
import glob
import sys
import subprocess
import argparse
from pathlib import Path

def clear_screen():
    """Очистка экрана консоли"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_current_directory():
    """Получение текущего рабочего каталога"""
    return os.getcwd()

def change_directory(path=None):
    """Смена рабочего каталога"""
    if path:
        if os.path.exists(path) and os.path.isdir(path):
            os.chdir(path)
            print(f"Текущий каталог: {get_current_directory()}")
            return True
        else:
            print(f"Ошибка: Путь '{path}' не существует или не является директорией.")
            return False
    else:
        while True:
            new_path = input("Укажите корректный путь к рабочему каталогу: ").strip()
            if os.path.exists(new_path) and os.path.isdir(new_path):
                os.chdir(new_path)
                print(f"Текущий каталог: {get_current_directory()}")
                break
            else:
                print("Ошибка: Указанный путь не существует или не является директорией. Попробуйте снова.")

def display_files_with_extension(extension, directory=None):
    """Отображение файлов с указанным расширением"""
    if directory:
        original_dir = os.getcwd()
        os.chdir(directory)
    
    files = []
    if isinstance(extension, tuple):
        for ext in extension:
            files.extend(glob.glob(f"*{ext}"))
    else:
        files = glob.glob(f"*{extension}")
    
    files = [f for f in files if os.path.isfile(f)]
    
    if directory:
        os.chdir(original_dir)
    
    return files

def display_files_interactive(extension, description):
    """Отображение файлов в интерактивном режиме с нумерацией"""
    files = display_files_with_extension(extension)
    
    if not files:
        print(f"{description} не найдены.")
        return []
    
    print(f"Список файлов с расширением {extension} в данном каталоге:")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    print()
    
    return files

def pdf_to_docx_single(pdf_file):
    """Преобразование одного PDF файла в DOCX"""
    try:
        from pdf2docx import Converter
        
        if not os.path.exists(pdf_file):
            print(f"Ошибка: Файл '{pdf_file}' не найден.")
            return False
        
        docx_file = os.path.splitext(pdf_file)[0] + '.docx'
        cv = Converter(pdf_file)
        cv.convert(docx_file)
        cv.close()
        print(f"Файл '{pdf_file}' успешно преобразован в '{docx_file}'")
        return True
        
    except ImportError:
        print("Ошибка: Модуль pdf2docx не установлен.")
        print("Установите его командой: pip install pdf2docx")
        return False
    except Exception as e:
        print(f"Ошибка при преобразовании файла '{pdf_file}': {e}")
        return False

def pdf_to_docx_all(directory):
    """Преобразование всех PDF файлов в директории в DOCX"""
    files = display_files_with_extension('.pdf', directory)
    if not files:
        print(f"PDF файлы в директории '{directory}' не найдены.")
        return False
    
    success_count = 0
    for pdf_file in files:
        if pdf_to_docx_single(os.path.join(directory, pdf_file)):
            success_count += 1
    
    print(f"Успешно преобразовано {success_count} из {len(files)} файлов.")
    return success_count > 0

def convert_docx_to_pdf_libreoffice(docx_file):
    """Конвертация DOCX в PDF с помощью LibreOffice"""
    try:
        # Проверяем, установлен ли LibreOffice
        result = subprocess.run(['which', 'libreoffice'], capture_output=True, text=True)
        if result.returncode != 0:
            print("LibreOffice не установлен. Установите его:")
            print("Для MacOS: brew install --cask libreoffice")
            print("Для Ubuntu/Debian: sudo apt install libreoffice")
            return False
        
        # Конвертируем с помощью LibreOffice
        cmd = [
            'libreoffice', '--headless', '--convert-to', 'pdf',
            '--outdir', os.path.dirname(docx_file), docx_file
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            return True
        else:
            print(f"Ошибка LibreOffice: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"Ошибка при конвертации через LibreOffice: {e}")
        return False

def docx_to_pdf_single(docx_file):
    """Преобразование одного DOCX файла в PDF"""
    try:
        if not os.path.exists(docx_file):
            print(f"Ошибка: Файл '{docx_file}' не найден.")
            return False
        
        if convert_docx_to_pdf_libreoffice(docx_file):
            print(f"Файл '{docx_file}' успешно преобразован в PDF")
            return True
        else:
            print(f"Не удалось преобразовать файл '{docx_file}'")
            return False
            
    except Exception as e:
        print(f"Ошибка при преобразовании файла '{docx_file}': {e}")
        return False

def docx_to_pdf_all(directory):
    """Преобразование всех DOCX файлов в директории в PDF"""
    files = display_files_with_extension('.docx', directory)
    if not files:
        print(f"DOCX файлы в директории '{directory}' не найдены.")
        return False
    
    success_count = 0
    for docx_file in files:
        if docx_to_pdf_single(os.path.join(directory, docx_file)):
            success_count += 1
    
    print(f"Успешно преобразовано {success_count} из {len(files)} файлов.")
    return success_count > 0

def compress_image_single(image_file, quality=75):
    """Сжатие одного изображения"""
    try:
        from PIL import Image
        
        if not os.path.exists(image_file):
            print(f"Ошибка: Файл '{image_file}' не найден.")
            return False
        
        with Image.open(image_file) as img:
            # Создаем новое имя файла с префиксом 'compressed_'
            name, ext = os.path.splitext(image_file)
            compressed_file = f"{name}_compressed{ext}"
            
            # Сохраняем с указанным качеством
            if img.mode in ('RGBA', 'LA', 'P'):
                img = img.convert('RGB')
            
            img.save(compressed_file, optimize=True, quality=quality)
            print(f"Файл '{image_file}' успешно сжат в '{compressed_file}'")
            return True
            
    except ImportError:
        print("Ошибка: Модуль Pillow не установлен.")
        print("Установите его командой: pip install Pillow")
        return False
    except Exception as e:
        print(f"Ошибка при сжатии файла '{image_file}': {e}")
        return False

def compress_images_all(directory, quality=75):
    """Сжатие всех изображений в директории"""
    image_extensions = ('.jpeg', '.gif', '.png', '.jpg', '.JPG', '.JPEG', '.PNG')
    files = display_files_with_extension(image_extensions, directory)
    if not files:
        print(f"Изображения в директории '{directory}' не найдены.")
        return False
    
    success_count = 0
    for img_file in files:
        if compress_image_single(os.path.join(directory, img_file), quality):
            success_count += 1
    
    print(f"Успешно сжато {success_count} из {len(files)} изображений.")
    return success_count > 0

def delete_files_by_pattern(directory, mode, pattern):
    """Удаление файлов по шаблону"""
    if not os.path.exists(directory) or not os.path.isdir(directory):
        print(f"Ошибка: Директория '{directory}' не существует.")
        return False
    
    original_dir = os.getcwd()
    os.chdir(directory)
    
    files_deleted = 0
    
    try:
        for file in os.listdir('.'):
            if os.path.isfile(file):
                if mode == 'startswith' and file.startswith(pattern):
                    os.remove(file)
                    print(f'Файл: "{file}" успешно удалён!')
                    files_deleted += 1
                elif mode == 'endswith' and file.endswith(pattern):
                    os.remove(file)
                    print(f'Файл: "{file}" успешно удалён!')
                    files_deleted += 1
                elif mode == 'contains' and pattern in file:
                    os.remove(file)
                    print(f'Файл: "{file}" успешно удалён!')
                    files_deleted += 1
                elif mode == 'extension' and file.endswith(pattern):
                    os.remove(file)
                    print(f'Файл: "{file}" успешно удалён!')
                    files_deleted += 1
        
        if files_deleted == 0:
            print("Файлы, соответствующие критериям, не найдены.")
        else:
            print(f"Удалено файлов: {files_deleted}")
            
    except Exception as e:
        print(f"Произошла ошибка при удалении файлов: {e}")
        return False
    finally:
        os.chdir(original_dir)
    
    return files_deleted > 0

def interactive_pdf_to_docx():
    """Интерактивное преобразование PDF в DOCX"""
    files = display_files_interactive('.pdf', 'PDF файлы')
    if not files:
        input("Нажмите Enter для продолжения...")
        return
    
    try:
        choice = input("Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): ")
        
        if choice == '0':
            success_count = 0
            for pdf_file in files:
                if pdf_to_docx_single(pdf_file):
                    success_count += 1
            print(f"Успешно преобразовано {success_count} из {len(files)} файлов.")
        else:
            try:
                file_index = int(choice) - 1
                if 0 <= file_index < len(files):
                    pdf_to_docx_single(files[file_index])
                else:
                    print("Ошибка: Неверный номер файла.")
            except ValueError:
                print("Ошибка: Введите корректный номер.")
    
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    input("Нажмите Enter для продолжения...")

def interactive_docx_to_pdf():
    """Интерактивное преобразование DOCX в PDF"""
    files = display_files_interactive('.docx', 'DOCX файлы')
    if not files:
        input("Нажмите Enter для продолжения...")
        return
    
    try:
        choice = input("Введите номер файла для преобразования (чтобы преобразовать все файлы из данного каталога введите 0): ")
        
        if choice == '0':
            success_count = 0
            for docx_file in files:
                if docx_to_pdf_single(docx_file):
                    success_count += 1
            print(f"Успешно преобразовано {success_count} из {len(files)} файлов.")
        else:
            try:
                file_index = int(choice) - 1
                if 0 <= file_index < len(files):
                    docx_to_pdf_single(files[file_index])
                else:
                    print("Ошибка: Неверный номер файла.")
            except ValueError:
                print("Ошибка: Введите корректный номер.")
    
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    input("Нажмите Enter для продолжения...")

def interactive_compress_images():
    """Интерактивное сжатие изображений"""
    image_extensions = ('.jpeg', '.gif', '.png', '.jpg', '.JPG', '.JPEG', '.PNG')
    files = display_files_interactive(image_extensions, 'Изображения')
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
            success_count = 0
            for img_file in files:
                if compress_image_single(img_file, quality):
                    success_count += 1
            print(f"Успешно сжато {success_count} из {len(files)} изображений.")
        else:
            try:
                file_index = int(choice) - 1
                if 0 <= file_index < len(files):
                    compress_image_single(files[file_index], quality)
                else:
                    print("Ошибка: Неверный номер файла.")
            except ValueError:
                print("Ошибка: Введите корректный номер.")
    
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
    input("Нажмите Enter для продолжения...")

def interactive_delete_files():
    """Интерактивное удаление файлов"""
    print("Выберите действие:")
    print("1. Удалить все файлы начинающиеся на определенную подстроку")
    print("2. Удалить все файлы заканчивающиеся на определенную подстроку")
    print("3. Удалить все файлы содержащие определенную подстроку")
    print("4. Удалить все файлы по расширению")
    
    try:
        action = int(input("Введите номер действия: "))
        mode_map = {1: 'startswith', 2: 'endswith', 3: 'contains', 4: 'extension'}
        
        if action not in mode_map:
            print("Ошибка: Неверный номер действия.")
            return
        
        substring = input("Введите подстроку: ").strip()
        delete_files_by_pattern(os.getcwd(), mode_map[action], substring)
    
    except ValueError:
        print("Ошибка: Введите корректный номер действия.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    
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

def interactive_mode():
    """Интерактивный режим работы"""
    # Проверка зависимостей при запуске
    missing_deps = check_dependencies()
    if missing_deps:
        print("ВНИМАНИЕ: Отсутствуют некоторые модули:")
        for dep in missing_deps:
            print(f"  - {dep}")
        print("\nУстановите их командой: pip install " + " ".join(missing_deps))
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
            interactive_pdf_to_docx()
        elif choice == '2':
            interactive_docx_to_pdf()
        elif choice == '3':
            interactive_compress_images()
        elif choice == '4':
            interactive_delete_files()
        elif choice == '5':
            print("Выход из программы...")
            break
        else:
            print("Ошибка: Неверный выбор. Попробуйте снова.")
            input("Нажмите Enter для продолжения...")

def setup_argparse():
    """Настройка парсера аргументов командной строки"""
    parser = argparse.ArgumentParser(
        description='Office_Tweaks - инструмент для работы с файлами различных форматов',
        epilog='Примеры использования:\n'
               '  python office_tweaks.py --pdf2docx "document.pdf"\n'
               '  python office_tweaks.py --docx2pdf all --workdir "C:\\Documents"\n'
               '  python office_tweaks.py --compress-images "photo.jpg" --quality 50\n'
               '  python office_tweaks.py --delete --delete-mode extension --delete-pattern ".tmp" --delete-dir "C:\\Temp"',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Основные аргументы
    parser.add_argument('--pdf2docx', 
                       help='Конвертировать PDF в DOCX (указать путь к файлу или "all" для всех файлов в папке)')
    
    parser.add_argument('--docx2pdf', 
                       help='Конвертировать DOCX в PDF (указать путь к файлу или "all" для всех файлов в папке)')
    
    parser.add_argument('--compress-images', 
                       help='Сжать изображения (указать путь к файлу или "all" для всех файлов в папке)')
    
    parser.add_argument('--quality', type=int, choices=range(1, 101), default=75,
                       help='Качество сжатия изображений (1-100, по умолчанию 75)')
    
    parser.add_argument('--workdir', 
                       help='Рабочая директория (используется с "all" для операций)')
    
    # Аргументы для удаления файлов
    parser.add_argument('--delete', action='store_true',
                       help='Удалить файлы по шаблону')
    
    parser.add_argument('--delete-mode', choices=['startswith', 'endswith', 'contains', 'extension'],
                       help='Режим удаления файлов')
    
    parser.add_argument('--delete-pattern',
                       help='Шаблон для удаления файлов')
    
    parser.add_argument('--delete-dir',
                       help='Директория для удаления файлов')
    
    # Интерактивный режим
    parser.add_argument('-i', '--interactive', action='store_true',
                       help='Запустить интерактивный режим')
    
    return parser

def main():
    """Главная функция программы"""
    parser = setup_argparse()
    args = parser.parse_args()
    
    # Проверяем, есть ли какие-либо аргументы (кроме interactive)
    has_cli_args = any([
        args.pdf2docx, args.docx2pdf, args.compress_images, 
        args.delete, args.workdir, args.quality != 75
    ])
    
    # Если нет аргументов или указан interactive, запускаем интерактивный режим
    if not has_cli_args or args.interactive:
        interactive_mode()
        return
    
    # Обработка аргументов командной строки
    
    # Конвертация PDF в DOCX
    if args.pdf2docx:
        if args.pdf2docx == 'all':
            workdir = args.workdir or os.getcwd()
            pdf_to_docx_all(workdir)
        else:
            pdf_to_docx_single(args.pdf2docx)
    
    # Конвертация DOCX в PDF
    if args.docx2pdf:
        if args.docx2pdf == 'all':
            workdir = args.workdir or os.getcwd()
            docx_to_pdf_all(workdir)
        else:
            docx_to_pdf_single(args.docx2pdf)
    
    # Сжатие изображений
    if args.compress_images:
        if args.compress_images == 'all':
            workdir = args.workdir or os.getcwd()
            compress_images_all(workdir, args.quality)
        else:
            compress_image_single(args.compress_images, args.quality)
    
    # Удаление файлов
    if args.delete:
        if not args.delete_mode or not args.delete_pattern:
            print("Ошибка: Для удаления файлов необходимо указать --delete-mode и --delete-pattern")
            return
        
        directory = args.delete_dir or os.getcwd()
        delete_files_by_pattern(directory, args.delete_mode, args.delete_pattern)

if __name__ == "__main__":
    main()