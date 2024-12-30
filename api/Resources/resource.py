
from flask import request
from flask_restful import Resource

from market.models import User, Item
from extensions import db

from api.schemas.user import UserShema
from api.schemas.item import ItemShema

from sqlalchemy import desc

#from flask_query_builder.querying import QueryBuilder

class UserList(Resource):

    def get(self):

        # sorting 

        name_filter = request.args.get("userName")
        budget_filter = request.args.get("budget")
        email_filter = request.args.get("email")
        sorts = request.args.get("sort")

        user_query = User.query

        if name_filter:

            user_query = user_query.filter(User.userName.ilike(f"%{name_filter}%"))

        if budget_filter:

            user_query = user_query.filter(User.budget == budget_filter)

        if email_filter:

            user_query = user_query.filter(User.email_address.in_(email_filter.split(",")))

        if sorts:
            for sort in sorts.split(","):
                descending = sort[0] == "-"
                if descending:
                    field = getattr(User,sort[1:])  
                    user_query = user_query.order_by(desc(field))
                else:
                    field = getattr(User,sort)
                    user_query = user_query.order_by(field)

        # sortin by query builder

        schema = UserShema(many=True)

        users = user_query.all()

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

        name_filter = request.args.get("name")
        price_filter = request.args.get("price")
        sorts = request.args.get("sort")

        item_query = Item.query

        if name_filter:

            item_query = item_query.filter(Item.name.ilike(f"%{name_filter}%"))

        if price_filter:

            item_query = item_query.filter(Item.price == price_filter)

        if sorts:
            for sort in sorts.split(","):
                descending = sort[0] == "-"
                if descending:
                    field = getattr(Item,sort[1:])
                    item_query = item_query.order_by(desc(field))
                else:
                    field = getattr(Item,sort)
                    item_query = item_query.order_by(field)

        schema = ItemShema(many=True)

        items = item_query.all()

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