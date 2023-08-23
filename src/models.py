from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

user_intereses = Table(
    'user_intereses',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id'), primary_key=True),
    Column('profile_id', Integer,  ForeignKey('profile.id'), primary_key=True),
    Column('planet_id', Integer, ForeignKey('planet.id'), primary_key=True),
    Column('character_id', Integer, ForeignKey('character.id'), primary_key=True),
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(120), nullable=False, unique=True)
    user_password = Column(String(120), nullable=False, unique=True)  
    user_firstname = Column(String(120), nullable=False, unique=True)
    user_lastname = Column(String(120), nullable=False, unique=True)
    email = Column(String(120), nullable=False, unique=True)
    profile = relationship('Profile', uselist=False, backref="user")
    follower = relationship('Follower', uselist=False, backref="user")
    post = relationship('Post', uselist=False, backref="user")
    comment = relationship('Comment', uselist=False, backref="user")

class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    profile_picture = Column(String(120))
    profile_first_name = Column(String(120), nullable=False, unique=True)
    profile_last_name = Column(String(120), nullable=False, unique=True)
    profile_phone_number = Column(Integer)
    profile_country = Column(String(120))
    profile_description = Column(String(120))
    profile_facebook = Column(String(120))
    profile_instagram = Column(String(120))
    profile_threads = Column(String(120))
    profile_twitter = Column(String(120))
    profile_linkedin = Column(String(120))


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    intereses_id = Column(Integer, ForeignKey('intereses.id'), primary_key=True)
    planet_name = Column(String(120), nullable=False, unique=True)
    planet_solar_system = Column(String(120), nullable=False, unique=True)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    intereses_id = Column(Integer, ForeignKey('intereses.id'), primary_key=True)
    character_first_name = Column(String(120), nullable=False, unique=True)
    character_last_name = Column(String(120), nullable=False, unique=True)
    character_race = Column(String(120), nullable=False, unique=True)
    character_occupation = Column(String(120), nullable=False, unique=True)

""" class Intereses(Base):
    __tablename__ = 'intereses'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    profile_id = Column(Integer, ForeignKey('profile.id'), primary_key=True)
    planet = Column(String)
    character = Column(String)
    planet = relationship('Planet', uselist=False, backref="intereses")
    character = relationship('Character', uselist=False, backref="intereses") """

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    comment_text = Column(String(400), nullable=True)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    media_header = Column(String(120), nullable=False, unique=True)
    media_body = Column(String(120), nullable=False, unique=True)
    media_footer = Column(String(120), nullable=False, unique=True)
    media_type = Column(String(120), nullable=False, unique=True)
    media_url = Column(String(120), nullable=False, unique=True)


def to_dict(self):
    return {}

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')