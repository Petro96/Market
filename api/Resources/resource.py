
from flask import request
from flask_restful import Resource

from market.models import User, Item
from extensions import db

from api.schemas.user import UserShema
from api.schemas.item import ItemShema


class UserList(Resource):

    def get(self):

        shema = UserShema(many=True)

        users = User.query.all()

        return {"results":shema.dump(users)}
    
    
    
    
class UserResource(Resource):

    def get(self, user_id):

        user = User.query.get_or_404(user_id)

        shema = UserShema()

        return {"user":shema.dump(user)}
    
    def put(self,user_id):

        shema = UserShema()

        user = User.query.get_or_404(user_id)

        user = shema.load(request.json, instance=user)

        db.session.add(user)
        db.session.commit()

        return {"msg":"User updated", "user":shema.dump(user)}
    
    def delete(self, user_id):

        user = User.query.get(user_id)

        db.session.delete(user)
        db.session.commit()

        return {"msg":"User Deleted"}




class ItemList(Resource):

    def get(self):

        shema = ItemShema(many=True)

        items = Item.query.all()

        return {"results":shema.dump(items)}
    
    def post(self):

        pass


class ItemResource(Resource):

    pass