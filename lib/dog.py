from models import Dog
from sqlalchemy.orm import sessionmaker

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)

def get_all(session):
    return [dog for dog in session.query(Dog)]

def find_by_name(session, name):
    return session.query(Dog.name, Dog.breed).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name).filter(Dog.breed == breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.add(dog)
    session.commit()
    # return session.query(dog).update({dog.breed: breed})