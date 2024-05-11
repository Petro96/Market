
from flask import Blueprint, jsonify
from flask_restful import Api
from marshmallow import ValidationError

from api.Resources.resource import UserList, ItemList, UserResource, ItemResource

blueprint = Blueprint("api",__name__,url_prefix="/api")

api = Api(blueprint,errors=blueprint.errorhandler)

api.add_resource(UserList,"/users")
api.add_resource(UserResource,"/users/<int:user_id>")

api.add_resource(ItemList,"/items")

@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(exception):
    return jsonify(exception.messages), 400