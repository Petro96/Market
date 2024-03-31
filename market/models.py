

from market import db, login_manager
from market import bcrypt
from flask_login import UserMixin

# loader usage =>create session => for managing more pages with the same user 
@login_manager.user_loader # contain UserMixin - methods that must pass before its loaded
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):

    # budget $dollar - private variable

    id = db.Column(db.Integer(),primary_key=True)
    userName = db.Column(db.String(length=30),nullable=False,unique=True)
    email_address = db.Column(db.String(length=50),nullable=False,unique=True)
    password_hash = db.Column(db.String(length=60),nullable=False)
    budget = db.Column (db.Integer(),nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    # constructor

    # getters, setters
    def getUserName(self):
        return self.userName # User.query.filter_by(self.userName).first()
    
    @property
    def prettier_budget(self):

        if len(str(self.budget)) >= 4:
            return f"{str(self.budget)[:-3]},{str(self.budget)[-3:]}$"
        else:
            return f"{self.budget}$" 

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):

        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')


    def check_password_correction(self, attempted_password):

        return bcrypt.check_password_hash(self.password_hash, attempted_password)
            

    def can_purchase(self,item_object):
        return self.budget >= item_object.price 
    
    def can_sell(self, item_obejct):
        return item_obejct in self.items # items => collect owner Items<Object>


    def __repr__(self) -> str:
        return f'User:<{self.userName}>'

class Item(db.Model):

    # counter - if you have the same product counter+1

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12),nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
    owner = db.Column(db.Integer(),db.ForeignKey('user.id'))

    # consturctor

    # geters, setters

    # methods

    def buy(self, user):

        self.owner = user.id
        user.budget -= self.price
        db.session.commit()

    def sell(self, user):

        self.owner = None
        user.budget += self.price
        db.session.commit()

    def __repr__(self) -> str:
        return f'Item: {self.name}'