from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/transactions',methods=['GET','POST'])
def transactions():
    return render_template('transactions.html')

