# Телефонная книга

Это тестовое задание. В нем реализовано консольное приложение для взаимодействия с телефонной книгой.
Приложение может отображать контакты из книги, удалять, изменять и добавлять новые.
Данные о контактах находятся в виде csv-файла.

## Установка и запуск

1. Убедитесь, что у вас установлен Docker.
2. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/nowtiloos/phonebook.git
    ```

3. Соберите Docker-образ:
    ```bash
    docker build -t phonebook .
   ```
4. Запустите контейнер с помощью следующей команды:
    ```bash
    docker run -i phonebook   
   ```
## Переменные окружения
В проекте используются следующие переменные окружения:

- \ `FILE_NAME`: Имя CSV файла (по умолчанию "test_data.csv").
- \ `PAGE_SIZE`: Размер страницы (по умолчанию 10).
- \ `SORT_BY`: Поле для сортировки (по умолчанию "surname").

### Примечание
Для демонстрации возможностей приложения данные в файле `test_data.csv` сгенерированы с помощью скрипта написанном с помощью библиотеки `faker`