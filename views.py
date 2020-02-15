from flask import abort, request, render_template, redirect, url_for, \
    session, flash
from forms import NameForm, PuppiesForm, DeleteForm
from app import app, db
from model import Puppy, Toy

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

@app.route('/puppies')
def list_puppies():
    puppies = Puppy.query.all()

    return render_template('puppies/list_puppies.html', puppies=puppies)

@app.route('/puppies/add', methods=['GET', 'POST'])
def add_puppies():
    form = PuppiesForm()
    if form.validate_on_submit():
        current_puppies = Puppy(
                name=form.name.data,
                age=form.age.data,
                breed=form.breed.data
            )
        db.session.add(current_puppies)
        db.session.commit()
        flash('Your Puppies has been added!')
        return redirect(url_for('list_puppies'))
    return render_template('puppies/add_puppies.html', form=form, title='Add')

@app.route('/puppies/edit/<int:id>', methods=['GET', 'POST'])
def edit_puppies(id):
    current_puppies = Puppy.query.get_or_404(id)
    form = PuppiesForm(
        name=current_puppies.name, 
        age=current_puppies.age,
        breed=current_puppies.breed
    )
    if form.validate_on_submit():
        current_puppies.name = form.name.data
        current_puppies.age = form.age.data
        current_puppies.breed = form.breed.data

        db.session.add(current_puppies)
        db.session.commit()
        flash('Your Puppies has been updated!')
        return redirect(url_for('list_puppies'))
    return render_template('puppies/add_puppies.html', form=form, title='Edit')


@app.route('/puppies/delete/<int:id>', methods=['GET','POST'])
def delete_puppies(id):
    current_puppies = Puppy.query.get_or_404(id)
    form = DeleteForm()
    if form.validate_on_submit():
        db.session.delete(current_puppies)
        db.session.commit()
        flash('Your Puppies has been deleted!')
        return redirect(url_for('list_puppies'))
    return render_template('puppies/del_puppies.html', form=form, title='Delete')