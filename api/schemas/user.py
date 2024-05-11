


from extensions import ma
from market.models import User, Item

from marshmallow.fields import String, Integer
from marshmallow import validate, validates_schema, ValidationError


class UserShema(ma.SQLAlchemyAutoSchema):

    userName = String(required=False, validate=[validate.Length(min=3)],error_messages={
        "invalid":"The name is invalid and needs to be a String!"
    })

    email_address = String(required=False, validate=[validate.Email()],error_messages={
        "invalid":"The email is invalid and needs to be written in email format!"
    })
    
    budget = Integer(validate=[validate.Range(min=0)])

    @validates_schema
    def validate_email(self,data, **kwargs):
        email = data.get("email_address")
        if User.query.filter_by(email_address=email).count():
            raise ValidationError(f"Email {email} already exists!")


    class Meta:

        model = User
        exclude = ["id","password_hash"]
        load_instance = True





