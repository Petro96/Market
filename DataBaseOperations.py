from market import app
from market import db
from market.models import Item,User

# -> * because of database configuration you can
# add only one unique item 
# can not generate(insert into database) the same objects twice

# create db

# from app import app
# from app import db / from market import db
# db.create_all()

# create  Item object 
item1 = Item(name="Iphone 14", price=500, barcode='341365789341',description='desc')
item2 = Item(name="Laptop", price=600, barcode='091237865981', description='description about')
item3 = Item(name="Speaker Sony 60W",price=300,barcode='345127689014',description='About Speakers')
item4 = Item(name="Samsung A53", price=550,barcode='893412345678', description='phone for recomendation')
item5 = Item(name="Laptop Lenovo T540", price=460, barcode='908761234567', description='Laptop is great for learning and administration')
item6 = Item(name="Fender Squier Guitar", price=250, barcode='561209876512', description='Guitar is used, doesnt have demage,it is very high quality. ')
item7 = Item(name="Mouse GameMouse Scorpion",price=34, barcode='341209876543',description='Game-Mouse, Best for Gaming.')
# adding to database

#db.session.add(item1)
#db.session.commit()

#db.session.add(item2)
#db.session.commit()

#db.session.add(item3)
#db.session.commit()

""" db.session.add(item4)
db.session.commit()

db.session.add(item5)
db.session.commit()

db.session.add(item6)
db.session.commit()

db.session.add(item7)
db.session.commit() """


# print out database items object
print(Item.query.all())

# create User object

user1 = User(userName='Jozef Mithell',password_hash='123456',email_address='jozefmitchell@gmail.com')


#db.session.add(user1)
#db.session.commit()

# print out database user object
print(User.query.all())


# Obejct relational data base management - owner selector

i1 = Item.query.filter_by(name='Iphone 14').first()
i1.owner = User.query.filter_by(userName='Jozef Mithell').first().id
db.session.add(i1)
db.session.commit()
print("Owned Item ID:",i1.owner)

item_owned_by = Item.query.filter_by(name='Iphone 14').first()
print("Item Owned By: ",item_owned_by.owned_user)


# ---------------------------------------
# methods

def insertIntoDb(item):

    try:

        db.session.add(item)
        db.session.commit()
    except:
        print("Theres some error to push this item")

# filtering object by

""" filtered = Item.query.filter_by(price=500)
for item in filtered:
    print(f'item:{item.name}, price: {item.price}') """




