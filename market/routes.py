

from market import app,db
from flask import render_template,redirect,url_for,flash,get_flashed_messages,request
from market.models import Item,User
from market.forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')

# /market -> endpoint (usage: GET,POST,PUT,DELETE)
@app.route('/market')
@login_required
def market_page():

    items = Item.query.all() # get all items from db
    '''
    items = [
    {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
    {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
    {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    '''

    return render_template('market.html',items=items)


@app.route('/register',methods=['GET','POST'])
def register_page():

    form = RegisterForm()

    if form.validate_on_submit() and request.method=="POST": # validate when you hit submit button 

        user_to_create = User(userName=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password.data) # password -> property setter => setter=method_argument 
                            # Silvia Pot 987654
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