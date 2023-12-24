# 0) прочитать статью (https://fastapi.tiangolo.com/tutorial/query-params/)
# 1) Напиши функцию которая выводит  n символов стихотворения Бродского (стихотворение выбери сам)
# 2) Друную функцию, выводящую один и тот же текст но на русском (по дефолту), английском (если есть пареметр 'en') или на китайском если любой другой параметр стоит.
# PS: текст можешь перевести через Google Translate вручгую пока
# 3) Функцию выводящую любое прииветственное письмо (пусть AI  напишет его), но с персонализованными обращениями (имя подается как параметр в функцию)
from fastapi import FastAPI
from translater import norris_joke, translate

appilcation = FastAPI()
@appilcation.get("/poem/{n}")
async def get_poem(n: int):
   poem = "Вот мой стих..."
   return {"poem": poem[:n]}


# @app.get("/text/{lang}")
# async def get_text(lang: str):
#    text = "Это мой текст..."
#    if lang == 'en':
#        # use uour own function
#        return {"text": translator.translate(text, dest='en').text}
#    elif lang == 'cn':
#        return {"text": translator.translate(text, dest='zh-cn').text}
#    else:
#        return {"text": text}

@appilcation.get("/welcome/{name}")
async def welcome(name: str):
   message = f"Здравствуйте, {name}! Рад видеть Вас!"
   return {"message": message}