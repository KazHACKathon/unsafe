from flask import Blueprint, url_for, render_template, redirect, request
from models import db, Users,Stacks


stacker = Blueprint('stacks', __name__, template_folder='../frontend')
@stacker.route('/stack',methods=['GET','POST'])
def show():
    if request.method == 'POST':
        stack_name = request.form['stack_name']
        stack = Stacks.query.filter_by(stack_name=stack_name).first()
        if stack:
            pass 
        else:
            return redirect(url_for('stacker.show') + '?error=stack name is invalid')
    else:
        stack_get = request.form['stack_get']
        stack = Stacks.query.filter_by(stack_name=stack_get).first()
        if stack:
            pass
        else:
            return redirect(url_for('stacker.show')+'?error=not found')