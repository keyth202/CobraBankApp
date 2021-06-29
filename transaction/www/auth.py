from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

#attempted a login but having issues with the hash so not working on a current user account, just database user_id 
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user= User.query.filter_by(email=email).first()
        print(user.email+ " ")
        print(user.id)
        #if user:
            #if check_password_hash(user.password, password):
                #flash('Logged in successful!', category = 'success')
                #login_user(user, remember=True)
                #return redirect(url_for('views.home'))
            #else:
                #flash('Incorrect password', category = 'error')
        #else:
            #flash('Email does not exist.', category ='error')

    return render_template('login.html', user=current_user)

@auth.route('/logout',methods=['GET','POST'])
def logout():
    return render_template('login.html')

#tested signup to add users to use for the transactions methods
@auth.route('/sign-up',methods=['GET','POST'])
def sign_up():

    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1') 
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        elif len(email)< 4:
            flash('Email must be greater than 4 characters', category='error')
            pass
        elif len(firstName)< 2:
            flash('First Name must be greater than 1 character', category ='error')
            pass
        elif len(password1)< 7:
            pass
        elif password1 != password2:
            flash('Passwords do not match',category='error')
            pass
        else: 
            # add user to database
            new_user = User(email=email, firstName=firstName,lastName=lastName, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            flash('Account Created', category='success')

            return redirect(url_for('views.transactions'))
            pass
    else:
        print('Something happened')
        pass
       
    return render_template('sign_up.html')

    