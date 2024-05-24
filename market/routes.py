

from market import app,db
from flask import render_template,redirect,url_for,flash,get_flashed_messages,request
from market.models import Item,User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from flask_login import login_user, logout_user, login_required,current_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')


# /market -> endpoint (usage: GET,POST,PUT,DELETE)
@app.route('/market', methods=['GET','POST'])
@login_required
def market_page():

    purchase_form = PurchaseItemForm()
    
    selling_form = SellItemForm()

    """ if purchase_form.validate_on_submit():

        #print(purchase_form.__dict__) # return dict of purchasing items
        # <input id="submit" name="submit" type="submit" value="Purchase Item">
        print(request.form.get['purchased_item']) # return ipnut tag html code -> represend it in modals file like an hidden
 """

    if request.method == "POST":
        # -------------------  Purchase Items ---------------------
        purchased_item = request.form.get('purchased_item') # get(name_of_input) return Object name , that object is load into curren_user variable by flask_login library

        p_item_object = Item.query.filter_by(name=purchased_item).first()
        # if object exists start purchasing
        
        if p_item_object:
            # check do you have enough money 
            if current_user.can_purchase(p_item_object):
                # method : p_item_object.buy(current_user) # current_user -> return User object wich is log in 
                p_item_object.buy(current_user)

                flash(f"Congratulations! You purchased {p_item_object.name} for {p_item_object.price}$ price.",category="success")
            else:
                flash(f"Unfortunately, you don't have enough money to purchase {p_item_object.name}.",category="danger")
        # ------------------- Selling Items -----------------------
        sold_item = request.form.get('sold_item')

        s_item_object = Item.query.filter_by(name=sold_item).first()

        if s_item_object:

            if current_user.can_sell(s_item_object):

                s_item_object.sell(current_user)  

                flash(f"Congratulations! You sold {s_item_object.name} for {s_item_object.price}$ price. Its returned to Market.",category="success")      
            else:
                 flash(f"Something went wrong selling this item {s_item_object.name}.",category="danger")

        return redirect(url_for('market_page'))
    
    if request.method == "GET":

        # show items that doesnt have owner
        items = Item.query.filter_by(owner=None)

        # grab owned items for logged in user
        owned_items = Item.query.filter_by(owner=current_user.id) # grab items by ID of user because you create relatioship with user_id

        return render_template('market.html',items=items, purchase_form=purchase_form, owned_items=owned_items, selling_form=selling_form)

    #items = Item.query.all() # get all items from db

   
   
@app.route('/register',methods=['GET','POST'])
def register_page():

    form = RegisterForm()

    if form.validate_on_submit() and request.method=="POST": # validate when you hit submit button 

        user_to_create = User(userName=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password.data) # password -> property setter => setter=method_argument 
                            # Silvia Pot 987654
                            # Julia Moor 012345
        #user_to_create.getUserName() # calling User getter
        db.session.add(user_to_create)
        db.session.commit()

        # --------------- After registration you are logged in --------
        login_user(user_to_create)

        flash(f'Account created successfully! You are now logged in as {user_to_create.userName}',category='success')
        # -------------------------------------------------------------
        return redirect(url_for('market_page'))
    
    if form.errors != {}: # if dictionary is not  empty! It meens that exist some errors -> if theres no errors from validator

        for err_msg in form.errors.values(): # form.errors -> is dictionary

            flash(f'Theres was an error with creating a user: {err_msg}', category='danger')
    #flash_message = get_flashed_messages()

    return render_template('register.html',form=form)


@app.route('/login', methods=['GET','POST'])
def login_page():

    login = LoginForm()

    if login.validate_on_submit():

        attempted_user = User.query.filter_by(userName=login.username.data).first()

        if attempted_user and attempted_user.check_password_correction(attempted_password=login.password.data):

            login_user(attempted_user)

            flash(f'Success! You are logged as: {attempted_user.userName}',category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again!',category='danger')

    return render_template('login.html',login=login)

@app.route('/logout_page', methods=['GET','POST'])
def logout_page():

    logout_user()

    flash("You have been logged out!", category="info")

    return redirect(url_for('home_page'))