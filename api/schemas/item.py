
from extensions import ma
from market.models import Item


class ItemShema(ma.SQLAlchemyAutoSchema):

    class Meta:

        model = Item
        exclude = ["id"]