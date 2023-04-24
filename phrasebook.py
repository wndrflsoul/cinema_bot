import typing as tp

WELCOME = "Привет! Я кино-бот! Введи название фильма либо сериала и я покажу тебе всю информацию о нём! А так же, предложу тебе его посмотреть на различных сервисах :) Разработано для Проектной Деятельности 3."
HELP = "Тебе нужно лишь написать название фильма или сериала, а я найду его на кинопоиске!"
FOUND = "Найдено:"
NOT_FOUND = "Попробуй написать по-другому😉"
CANCEL = "Хорошо, найдём что-нибудь другое.."
SOURCES = """Доступно несколько вариантов просмотра:

💰 Платно или по подписке
🆓 Бесплатно, но может понадобится VPN или прокси"""


def construct_description(film_json: tp.Dict[str, tp.Any]) -> str:
    name_ru = film_json['nameRu']
    name_en = film_json['nameEn']
    description = film_json['description']
    year = film_json['year']
    countries = ', '.join([c['country'] for c in film_json['countries']])
    length = film_json['filmLength']
    genres = ', '.join([g['genre'] for g in film_json['genres']])
    rating = film_json['rating']
    
    return f"""{name_ru}, {name_en}

📅 {year}
📈 {rating}
⌛ {length}
🎬 {description}
🗺 {countries}
ℹ️ {genres}"""
