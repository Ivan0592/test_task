from fastapi import FastAPI
import fastapi
# app = FastAPI(debug=True)
#
#
# import fastapi
#
# app = fastapi.FastAPI()
#
# @app.get("/")
# async def root():
#     return {"message": "Hello world", "Name": "Ivan"}


from fastapi import FastAPI
from enum import Enum
import logging


app = FastAPI(debug=True)

#TODO: Вынести логирование в отдельный файл
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class Role(str, Enum):
    admin = 'admin'
    user = 'user'
    owner = 'owner'


@app.get("/user/ivan")
async def root_admin():
    logger.info('You are enter as admin')
    return {"msg": "You are enter as admin"}


@app.get("/user/{name}")
async def user_name(name: str):
    """
    Function return name of user
    :param name:
    :return:
    """
    return {"msg": f"Hello, {name}"}


@app.get("/{role}/{name}")
async def read_role(role: Role, name: str):
    return {"msg": f"{name}, you are enter as {role}"}

# Функцию возвращающую 127.0.0.1/<num>/<name>  в  name num раз


@app.get("/output/{num}/{name}")
async def output_name_num_time(num: int, name: str):
    name = name * num
    print(num, type(num), name, type(name))
    return {"msg": f"{name}"}



@app.get("/")
async def root():
    return {'Hello!'}

from pydantic import BaseModel
from datetime import date

class Contact(BaseModel):
    name: str
    surname: str
    age: int
    registration_data: date
    phone_number: str

@app.post('/')
async def root_get_contacts(contact: Contact):
    logger.info(contact)
    return contact