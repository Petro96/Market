
from flask import request
from flask_restful import Resource

from market.models import User, Item
from extensions import db

from api.schemas.user import UserShema
from api.schemas.item import ItemShema


class UserList(Resource):

    def get(self):

        schema = UserShema(many=True)

        users = User.query.all()

        return {"results":schema.dump(users)}
    
    
    
    
class UserResource(Resource):

    def get(self, user_id):

        user = User.query.get_or_404(user_id)

        schema = UserShema()

        return {"user":schema.dump(user)}
    
    def put(self,user_id):

        schema = UserShema(partial=True)

        user = User.query.get_or_404(user_id)

        user = schema.load(request.json, instance=user)

        db.session.add(user)
        db.session.commit()

        return {"msg":"User updated", "user":schema.dump(user)}
    
    def delete(self, user_id):

        user = User.query.get(user_id)

        db.session.delete(user)
        db.session.commit()

        return {"msg":"User Deleted"}




class ItemList(Resource):

    def get(self):

        schema = ItemShema(many=True)

        items = Item.query.all()

        return {"results":schema.dump(items)}
    
    def post(self):

        schema = ItemShema()
        validate_data = schema.load(request.json)

        item = Item(name=validate_data.name,
                    price=validate_data.price,
                    barcode=validate_data.barcode,
                    description=validate_data.description
                    )
        db.session.add(item)
        db.session.commit()

        return {"msg":"Item created","item":schema.dump(item)}


class ItemResource(Resource):

    def get(self,item_id):

        item = Item.query.get_or_404(item_id)

        schema = ItemShema()

        return {"item":schema.dump(item)}
    
    def put(self,item_id):

        schema = ItemShema(partial=True)

        item = Item.query.get_or_404(item_id)

        item = schema.load(request.json,instance=item)

        db.session.add(item)
        db.session.commit()

        return {"msg":"Item updated", "Item":schema.dump(item)}
    
    def delete(self,item_id):

        item = Item.query.get_or_404(item_id)

        db.session.delete(item)
        db.session.commit()

        return {"msg":"Item deleted"}