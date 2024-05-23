
from extensions import ma
from market.models import Item

from marshmallow.fields import String, Integer
from marshmallow import validate, validates_schema, ValidationError


class ItemShema(ma.SQLAlchemyAutoSchema):

    name = String(required=False,validate=[validate.Length(min=3)],error_messages={
        "invalid":"This name is invalid and needs to be a String!"
    })

    price = Integer(required=False,validate=[validate.Range(min=0)])

    barcode = String(required=False,validate=[validate.Length(min=12)],error_messages={
        "invalid":"This barcode is invalid and needs to be a String type!"
    })

    description = String(required=False,validate=[validate.Length(min=3,max=1024)],error_messages={
        "invalid":"This description is invalid, needs to be a String type!"
    })

    owner = Integer()

    @validates_schema
    def validate_barcode(self,data,**kwargs):
        barcode = data.get("barcode")
        if Item.query.filter_by(barcode=barcode).count():
            raise ValidationError(f"This {barcode} already exists!")

    class Meta:

        model = Item
        load_instance = True
        #exclude = ["id"]