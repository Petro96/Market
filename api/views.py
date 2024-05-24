
from flask import Blueprint, jsonify
from flask_restful import Api
from marshmallow import ValidationError
from flask_cors import cross_origin

from api.resources.resource import UserList, ItemList, UserResource, ItemResource

blueprint = Blueprint("api",__name__,url_prefix="/api")

api = Api(blueprint,errors=blueprint.errorhandler)

api.add_resource(UserList,"/users")
api.add_resource(UserResource,"/users/<int:user_id>")

api.add_resource(ItemList,"/items")
api.add_resource(ItemResource,"/items/<int:item_id>")


@blueprint.route("/cors")
@cross_origin()
def test_cors():
    return {}

@blueprint.errorhandler(ValidationError)
def handle_marshmallow_error(exception):
    return jsonify(exception.messages), 400