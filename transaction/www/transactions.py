from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from .models import Accounts
from flask_sqlalchemy import SQLAlchemy
from os import path
from . import db 


transactions = Blueprint('transactions', __name__)

@transactions.route('/withdrawal', methods=['GET','POST'])
def withdrawal():
    # retrieve money from database -> will need to change this to the current user id or email when logged in
    acct = Accounts.query.filter_by(user_id=4).first()
    
    print(acct.checkings)

    if request.method == 'POST':
        inputAmt = request.form.get('InputAmount')
        #print(inputAmt)
        if (acct.checkings > float(inputAmt)):
            newBal = acct.checkings-float(inputAmt)
            #print(newBal) 
            acct.checkings = newBal
            db.session.commit()
        else:
            flash('OverDraft Alert -$20 if you continue', category ='error')
            newBal = acct.checkings-float(inputAmt)-20
            #print(newBal) 
            acct.checkings = newBal
            db.session.commit()
        
        
        #newBalance = Accounts.query.filter_by(user_id=4).first()
        #print(newBalance.checkings)

        balance = 4
    return render_template('transactions.html')

@transactions.route('/deposit', methods=['GET','POST'])
def deposit():
    # find account by id -> will need to change this to the current user id or email when logged in
    acct = Accounts.query.filter_by(user_id=4).first()
    
    print(acct.checkings)

    if request.method == 'POST':
        inputAmt = request.form.get('InputAmount')
        #print(inputAmt)
        newBal = acct.checkings+float(inputAmt)
        #print(newBal) 
        acct.checkings = newBal
        db.session.commit()
        newBalance = Accounts.query.filter_by(user_id=4).first()
        
        #print(newBalance.checkings)

        balance = 4
    
    return render_template('transactions.html')

@transactions.route('/showbalance', methods=['GET','POST'])
def showBalance(): 
    #pull both accounts from database
    balance = 4
    return render_template('transactions.html')

@transactions.route('/transfer', methods=['GET','POST'])
def transfer(): 
    # transfer money between accounts 
    balance = 4 
    return render_template('transactions.html')
