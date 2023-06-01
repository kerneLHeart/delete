######## version 1
# import os
# import time
# # 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
# source = [r'C:\Users\Aleksey\PycharmProjects\otk']
# # Заметьте, что для имён, содержащих пробелы, необходимо использовать
# # двойные кавычки внутри строки.
# # 2. Резервные копии должны храниться в основном каталоге резерва.
# target_dir = r'C:\Users\Aleksey\PycharmProjects\k' # Подставьте ваш путь.
# # 3. Файлы помещаются в zip-архив.
# # 4. Именем для zip-архива служит текущая дата и время.
# target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
# # 5. Используем команду "zip" для помещения файлов в zip-архив
# if not os.path.exists(target_dir):
#     os.mkdir(target_dir)
# zip_command = r'""C:\Program Files\7-Zip\7z.exe" a -tzip -ssw -mx5 -r0 {0} {1}"'.format(target, ' '.join(source))
# # Запускаем создание резервной копии
# if os.system(zip_command) == 0:
#     print('Резервная копия успешно создана в', target)
# else:
#     print('Создание резервной копии НЕ УДАЛОСЬ')


#############version 2
# import os
# import time
# # 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
# source = [r'C:\Users\Aleksey\PycharmProjects\otk']
# # Заметьте, что для имён, содержащих пробелы, необходимо использовать
# # двойные кавычки внутри строки.
# # 2. Резервные копии должны храниться в основном каталоге резерва.
# target_dir = r'C:\Users\Aleksey\PycharmProjects\k' # Подставьте ваш путь.
# # 3. Файлы помещаются в zip-архив.
# # 4. Именем для zip-архива служит текущая дата и время.
# today = target_dir + os.sep + time.strftime('%Y' + '.' + '%m' + '.' + '%d')
# now = time.strftime('%H' + '.' + '%M' + '.' + '%S')
# # 5. Используем команду "zip" для помещения файлов в zip-архив
# if not os.path.exists(today):
#     os.mkdir(today)
#     print("Каталог успешно создан:  " + today)
#
# target = today + os.sep + now + '.zip'
# zip_command = r'""C:\Program Files\7-Zip\7z.exe" a -tzip -ssw -mx5 -r0 {0} {1}"'.format(target, ' '.join(source))
# # Запускаем создание резервной копии
# if os.system(zip_command) == 0:
#     print('Резервная копия успешно создана в', target)
# else:
#     print('Создание резервной копии НЕ УДАЛОСЬ')


#############version 3
import os
import time
# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = [r'C:\Users\Aleksey\PycharmProjects\otk']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.
# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = r'C:\Users\Aleksey\PycharmProjects\k' # Подставьте ваш путь.
# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y' + '.' + '%m' + '.' + '%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H' + '.' + '%M' + '.' + '%S')
# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today) # создание каталога
    print('Каталог успешно создан', today)
# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0: # проверяем, введён ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
        comment.replace(' ', '_') + '.zip'

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = r'""C:\Program Files\7-Zip\7z.exe" a -tzip -ssw -mx5 -r0 {0} {1}"'.format(target, ' '.join(source))
# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
