# Test_task
<h3>
Тестовое задание на производственную практику Софт Инжиниринг
</h3>
Для запуска заданий потребуется установленная IDE PyCharm

<h3>
Условия задач
</h3>

<h2>
Junior
</h2>
    Задача 1:
    Написать консольное приложение, которое выводит фамилию и имя пользователя с id 10, данные взять из публичного API

    Задача 2:
    Необходимо сгруппировать сотрудников по отделу из представленного JSON. 
        *В каждый отдел необходимо добавить поле count, содержащее количество сотрудников в отделе
        *В каждый отдел необходимо добавить поле avg_hours, содержащее среднюю выработку сотрудников по отделу
        *Если у сотрудника отсутствует поле hours, то такого сотрудника необходимо исключить из подсчета средней выработки
        *Округление до целого по правилам математики
        *Поле dept необходимо убрать (значение полей dept должны стать ключами выходного json)
        *Вывести сотрудников сгруппированных по отделу
 
    Задача 3:
        1. Докеризировать оба приложения
        2. Если программа содержит этап компиляции, то сделать двухэтапную сборку
        3. Описать docker-compose file, в котором должен вызываться написанный вами Dockerfile
    
    
<h2>
Middle
</h2
    Задача 1
    Написать парсер, получающий список премьер недели
    Сформировать json, содержащий данные о фильмах
    *name - название фильма
    *name_eng - название фильма на английском
    *film_link - ссылка на страницу фильма
    *film_rating - рейтинг фильма (если есть)
    *wait_rating - рейтинг ожидания (если есть)
    *votes - количество голосов
    *date - дата премьеры
    *company - компания, выпускающая фильм
    *genres - жанры фильма (массив)
    
<h2>
Инструкция по запуску кода
</h2>
    Что-бы запустить скрипт задания Junior(1), нужно:
            открыть скрипт с помощью PyCharm и нажать сочетание клавиш "Shift + F10", для запуска скрипта. 
            (вывод информации будет в консоли)    
        
    Что-бы запустить скрипт задания Junior(2), нужно:
            открыть скрипт с помощью PyCharm и нажать сочетание клавиш "Shift + F10", для запуска скрипта.
            (отсортированный файл json, будет создан в той же директории, где находится сам скрипт)
            (отсортированный файл будет иметь название "outfile.json")
       
    Задание Junior(3):
        1. оба докеризованных приложения находятся на Dockerhub
            Для Linux:
                Для запуска первого приложения, нужно ввести в командную строку Linux - docker pull debankov/firstpj:latest
                Для запуска второго приложения, нужно ввести в командную строку Linux - docker pull debankov/secondpj:latest
                    Отсотированный файл будет находиться в той же директории в который был запущен образ, 
                    для того что-бы просмотреть отсортированный файл нужно ввести в командную строку Linux следующую команду:
                    docker run -it debankov/secondpj:latest /bin/bash
                    после ввода вы будете находится в директории со всеми файлами образа
                    для просмотра всех файлов в директории нужно ввести команду - ls
                    отсортированный файл будет иметь название "outfile.json"

            
        2. Программы не содержат этапа компиляции.
        3.
    
    
    Что-бы запустить скрипт задания Middle(1), нужно:
            открыть скрипт с помощью PyCharm и нажать сочетание клавиш "Shift + F10", для запуска скрипта.
            (файл json, будет создан в той же директории, где находится сам скрипт)
            (отсортированный файл будет иметь название "outfile.json")
    
    




