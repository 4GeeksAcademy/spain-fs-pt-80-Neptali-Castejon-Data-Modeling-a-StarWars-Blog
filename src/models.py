import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

# Tabla intermedia para la relación Muchos-a-Muchos entre Usuarios y Favoritos
user_favorites = Table(
    'user_favorites',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('favorite_id', Integer, ForeignKey('favorites.id'))
)

# Tabla Usuario
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String(128), nullable=False)
    date_joined = Column(DateTime, nullable=False)
    favorites = relationship('Favorites', secondary=user_favorites, back_populates='users')
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
    
# Tabla de Planetas
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    population = Column(String(50), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population,
        }

# Tabla de Personajes
class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(50), nullable=True)
    birth_year = Column(String(50), nullable=True)
    height = Column(String(50), nullable=True)
    skin_color = Column(String(50), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birth_year": self.birth_year,
            "height": self.height,
            "skin_color": self.skin_color,
        }
    
# Tabla Favoritos
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    type = Column(String(50), nullable=False)
    reference_id = Column(Integer, nullable=False)
    users = relationship('Users', secondary=user_favorites, back_populates='favorites')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "reference_id": self.reference_id,
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
