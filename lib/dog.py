from models import Dog

def create_table(base,engine):
    pass

    base.metadata.create_all(engine)    
    
def save(session, dog):
    pass
    session.add(dog)
    session.commit()

def get_all(session):
    pass
    dogs = session.query(Dog)
    return [dog for dog in dogs]

def find_by_name(session, name):
    pass
    query = session.query(Dog).filter(Dog.name.like(f'%{name}%'))
    return query.first()

def find_by_id(session, id):
    pass
    query = session.query(Dog).filter(Dog.id.like(f'%{id}%'))
    return query.first()

def find_by_name_and_breed(session, name, breed):
    pass
    query = session.query(Dog).filter(Dog.name.like(f'%{name}%')).filter(Dog.breed.like(f'%{breed}%'))
    return query.first()

def update_breed(session, dog, breed):
    pass
    dog.breed = breed
    session.commit()