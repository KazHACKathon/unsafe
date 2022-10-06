from flask import Blueprint, session, request
from flask_login import login_required
from models import db, Users,Stacks


stacker = Blueprint('stacks', __name__, template_folder='../frontend')

@stacker.route('/stack',methods=['GET', 'POST'])
@login_required
def show():
    if request.method == 'POST':
        stack_name = request.form['stack']
        user_name = session['user_id']
        new_user = db.session.query(Users).filter(Users.username == user_name)
        user = new_user[0]
        new_stack = db.session.query(Stacks).all()
        stacks = []
        for i in new_stack:
            stacks.append(i.stack_name)
            
        if stack_name not in stacks:
            ns = Stacks(
                stack_name=stack_name,
                last_cve=stack_name
            )
            db.session.add(ns)
            db.session.commit()
        
        stack_to_append = db.session.query(Stacks).filter(Stacks.stack_name==stack_name)
        x = stack_to_append[0]
        user.following.append(x)
        db.session.commit()
        print(user)
        print(x)
            
        return ""
    else:
        user_name = session['user_id']
        new_user = db.session.query(Users).filter(Users.username == user_name)
        temp = []
        for els in new_user[0].following:
            temp.append(els.stack_name)

        return " ".join(temp)

# @stacker.route('/stack',methods=['POST'])
# @login_required
# def update():
    
@stacker.route('/stack_delete',methods=['POST'])
@login_required
def delete():
    stack_name = request.form['delete']
    user_name = session['user_id']
    new_user = db.session.query(Users).filter(Users.username == user_name)
    user = new_user[0]
    new_stack = db.session.query(Stacks).all()
    stacks = []
    for i in new_stack:
        stacks.append(i.stack_name)
    
    if stack_name not in stacks:
        return "You dont have this stack"
    
    stack_to_delete = db.session.query(Stacks).filter(Stacks.stack_name==stack_name)
    x = stack_to_delete[0]
    user.following.remove(x)
    db.session.commit()
    return "Successfull delete"