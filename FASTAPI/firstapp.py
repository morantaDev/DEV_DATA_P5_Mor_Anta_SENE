from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Table
from fastapi import FastAPI, Request
from sqlalchemy import MetaData
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

meta = MetaData()

materials = Table(
    'materials', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('nom', String(30)), 
    Column('description', String(255)),
    Column('prix', Integer)
)

class Material(BaseModel):
    nom: str
    description: str
    prix: int
    
pgDatabase = create_engine("postgresql://moranta21:Wizzle21#@localhost:5432/fastapidb")
    
meta.create_all(pgDatabase)
pgconnection = pgDatabase.connect()

# @app.get('/')
# async def greetings():
#     return{'message': 'Hello, World'}

@app.get('/materials/{id}')
async def get_oneMaterial(id:int):
    result=pgconnection.execute(materials.select().where(materials.c.id==id))
    # result = pgconnection.execute(materials.select()).fetchall()
    materials_list=[dict(row._asdict()) for row in result] 
    return materials_list

@app.get('/materials')
async def get_materials():
    result = pgconnection.execute(materials.select()).fetchall()
    materials_list=[dict(row._asdict()) for row in result] 
    return materials_list

@app.post('/insert')
async def add_materials(material: Material):
    pgconnection.execute(materials.insert().values(
        nom = material.nom,
        description = material.description,
        prix = material.prix
    ))
    pgconnection.commit()
    result = pgconnection.execute(materials.select()).fetchall()
    materials_list = [dict(row._asdict()) for row in result]
    return materials_list

@app.put("/update/{id}")
async def update_materials(id: int, material: Material):
    pgconnection.execute(materials.update().values(
        nom = material.nom,
        prenom = material.description,
        age = material.prix
        ).where(materials.c.id ==id))
    pgconnection.commit()
    result = pgconnection.execute(materials.select()).fetchall()
    apprenants_list = [dict(row._asdict()) for row in result]
    return apprenants_list

@app.get('/delete/{id}')
async def delete_materials(id: int):
    pgconnection.execute(materials.delete().where(materials.c.id==id))
    pgconnection.commit()
    result = pgconnection.execute(materials.select()).fetchall()
    materials_list = [dict(row._asdict()) for row in result]
    return materials_list


# apprenants = Table(
#     'apprenants', meta,
#     Column('id', Integer, primary_key=True, autoincrement=True),
#     Column('nom', String(30)),
#     Column('prenom', String(30)),
#     Column('age', Integer)
# )


# class Apprenant(BaseModel):
#     # id: int
#     nom: str
#     prenom : str
#     age: int
    
# database = create_engine("mysql+pymysql://phpmyadmin:Wizzle21#@127.0.0.1:3306/fastapidb")


# meta.create_all(database)

# connection = database.connect()

# @app.post("/add")
# async def add_apprenant(apprenant: Apprenant):
#     connection.execute(apprenants.insert().values(
#         nom = apprenant.nom,
#         prenom = apprenant.prenom,
#         age = apprenant.age
#     ))
#     connection.commit()
#     result = connection.execute(apprenants.select()).fetchall()
#     apprenants_list = [dict(row._asdict()) for row in result]
#     return apprenants_list

# @app.get("/{id}")
# async def get_apprenant(id: int):
#     result = connection.execute(apprenants.select().where(apprenants.c.id==id))
#     # result = connection.execute(apprenants.select()).fetchall()
#     apprenants_list = [dict(row._asdict()) for row in result]
#     return apprenants_list

# @app.put("/{id}")
# async def update_apprenant(id: int, apprenant: Apprenant):
#     connection.execute(apprenants.update().values(
#         nom = apprenant.nom,
#         prenom = apprenant.prenom,
#         age = apprenant.age
#         ).where(apprenants.c.id ==id))
#     connection.commit()
#     result = connection.execute(apprenants.select()).fetchall()
#     apprenants_list = [dict(row._asdict()) for row in result]
#     return apprenants_list

# @app.delete('/{id}')
# async def delete_apprenant(id: int):
#     connection.execute(apprenants.delete().where(apprenants.c.id==id))
#     result = connection.execute(apprenants.select()).fetchall()
#     apprenants_list = [dict(row._asdict()) for row in result]
#     return apprenants_list



# templates = Jinja2Templates(directory="templates/index.html")

# @app.get("/index", response_class=HTMLResponse)
# async def index(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})


# @app.get("/")
# def read_message():
#     return{"message": "Hello World"}




# from typing import Union
# from models.Apprenants import Apprenant
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
