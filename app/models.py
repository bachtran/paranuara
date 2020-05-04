from app import db

"""SQLAlchemy Models"""


class Company(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))

    def __repr__(self):
        return '<Company %r>' % self.name

    def to_dict(self):
        json_company = {
            'index': self.index,
            'name': self.name,
        }
        return json_company


friendship = db.Table('friendship',
                      db.Column('person_index', db.Integer, db.ForeignKey('person.index'), index=True),
                      db.Column('friend_index', db.Integer, db.ForeignKey('person.index')),
                      db.UniqueConstraint('person_index', 'friend_index', name='unique_friendship'),
                      )

person_food = db.Table('person_food',
                       db.Column('person_index', db.Integer, db.ForeignKey('person.index'), primary_key=True),
                       db.Column('food_index', db.Integer, db.ForeignKey('food.index'), primary_key=True)
                       )


class Person(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    age = db.Column(db.Integer)
    has_died = db.Column(db.Boolean)
    eye_color = db.Column(db.String(60))
    phone = db.Column(db.String(60))
    address = db.Column(db.String(60))
    company_index = db.Column(db.Integer, db.ForeignKey('company.index'))
    company = db.relationship('Company', backref='employees')
    friends = db.relationship('Person', secondary=friendship,
                              primaryjoin=index == friendship.c.person_index,
                              secondaryjoin=index == friendship.c.friend_index,
                              )
    foods = db.relationship('Food', secondary=person_food, lazy='subquery',
                            backref=db.backref('people', lazy=True))

    def befriend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
            friend.friends.append(self)

    def unfriend(self, friend):
        if friend in self.friends:
            self.friends.remove(friend)
            friend.friends.remove(self)

    def to_dict(self):
        json_person = {
            'index': self.index,
            'name': self.name,
            'has_died': self.has_died,
            'age': self.age,
            'eye_color': self.eye_color,
            'phone': self.phone,
            'address': self.address,
        }
        return json_person

    def __repr__(self):
        return '<Person %r>' % self.name


class Food(db.Model):
    VEGETABLE = 'vegetable'
    FRUIT = 'fruit'
    UNKNOWN = 'unknown'

    index = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    type = db.Column(db.String(60))

    def to_dict(self):
        json_food = {
            'index': self.index,
            'name': self.name,
            'type': self.type,
        }
        return json_food

    def __repr__(self):
        return '<Food %r>' % self.name
