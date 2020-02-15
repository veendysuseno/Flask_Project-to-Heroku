from app import db

class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    toys = db.relationship('Toy', backref='puppy', lazy='dynamic')

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return 'Puppy {} is {} year/s old'.format(self.name, self.age)

    def __repr__(self):
        return '<Puppy: {}>'.format(self.name)

    def report_toys(self):
        print("Here are my toys:")
        for toy in self.toys:
            print(toy.i_tem_name)

class Toy(db.Model):

    __tablename__ = 'toys'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id