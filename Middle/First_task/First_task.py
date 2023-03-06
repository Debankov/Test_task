import json
import bs4
import lxml


def get_data(url):
    headers = {
        "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "accept": "*/*"
    }

    with open("kinopoisk.html", encoding='utf8') as file:
        src = file.read()

    soup = bs4.BeautifulSoup(src, "lxml")
    all_premiers = soup.find("div", class_="prem_list").find_all("div", class_="premier_item")

    film_data = {}

    for premier in all_premiers:
        rus_name = premier.find("span", itemprop="name").text

        eng_name = premier.find("span", itemprop="name").findNext("span").text

        film_link = premier.find("span", itemprop="name").findNext("a").get("href")
        film_link = ("https://www.kinopoisk.ru" + film_link)

        # рейтинг ожидания
        rate_wait = premier.find("span", class_="await_rating")
        rate_film = premier.find("span", class_="ajax_rating")
        if rate_wait is not None:
            rate_wait = rate_wait.findNext("u").text
            film_vote = ''.join(rate_wait.split()[1:])
            rate_wait = rate_wait.split()[0]
            rate_film = None

        # рейтинг фильма
        elif rate_film is not None:
            rate_film = rate_film.findNext("u").text
            film_vote = ''.join(rate_film.split()[1:])
            rate_film = rate_film.split()[0]

        date = premier.find("meta", itemprop="startDate").get("content")

        company = [i.text for i in premier.find_all("s", class_="company")]

        genre = premier.find("span", style="margin: 0").findNext("span").text
        genre = ''.join(filter(lambda x: x not in ("(", ")", ".", ","), genre)).split()

        film_data.update({rus_name: {"Название: ": rus_name, 'Название на английском: ': eng_name,
                                     "Ссылка на фильм: ": film_link, "Рейтинг фильма: ": rate_film,
                                     "Рейтинг ожидания: ": rate_wait,
                                     "Количество голосов: ": film_vote, "Дата премьеры: ": date,
                                     "Компания: ": company, "Жанры: ": genre}})

    with open("outfile.json", "w", encoding='utf8') as file:
        json.dump(film_data, file, ensure_ascii=False, sort_keys=True, indent=4)
    file.close()


get_data("https://www.kinopoisk.ru/premiere/ru/")
