from sqlalchemy import Column, Integer, String, Table
from ..firstapp import meta


apprenants = Table(
    'apprenants', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('nom', String(30)),
    Column('prenom', String(30)),
    Column('age', Integer)
)





    