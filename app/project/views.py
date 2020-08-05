from . import project
from flask_login import login_required, current_user
from flask import render_template, redirect, url_for, flash
from .forms import NewProjectForm, DeleteForm
from app.models import User, Project, Idea, Outline, Draft
from werkzeug.security import check_password_hash

from app import db

@project.route('/dashboard')
@login_required
def dashboard():
	projects = current_user.projects.all()
	return render_template('project/dashboard.html', projects=projects, title='Dashboard')

@project.route('/project_dashboard/<id>')
@login_required
def project_dashboard(id):
	project = Project.query.get(int(id))

	if current_user.id != project.user_id:
		return redirect(url_for('project.dashboard'))

	return render_template('project/project_dashboard.html', project=project)

@project.route('/new_project', methods=['GET', 'POST'])
@login_required
def new_project():
	form = NewProjectForm()

	if form.validate_on_submit():
		project = Project(title=form.title.data, user_id=current_user.id)
		db.session.add(project)
		db.session.commit()

		return redirect(url_for('project.dashboard'))

	return render_template('project/new_project.html', form=form)

@project.route('/delete/type=<type>/id=<id>', methods=['GET', 'POST'])
@login_required
def delete(type, id):

	if type == 'project':
		project = Project.query.filter_by(id=id).first()
		if current_user.id != project.user_id:
			return redirect(url_for('project.dashboard'))
		item = Project.query.get(int(id))
	elif type == 'idea':
		idea = Idea.query.get(int(id))
		if current_user.id != idea.user_id:
			return redirect(url_for('project.dashboard'))
		item = Project.query.get(int(id))
	elif type == 'outline':
		outline = Outline.query.get(int(id))
		if current_user.id != outline.user_id:
			return redirect(url_for('project.dashboard'))
		item = Project.query.get(int(id))
	elif type == 'draft':
		draft = Draft.query.get(int(id))
		if current_user.id != draft.user_id:
			return redirect(url_for('project.dashboard'))
		item = Project.query.get(int(id))
	else:
		return redirect(url_for('dashboard'))

	form = DeleteForm()

	if form.validate_on_submit():
		if check_password_hash(current_user.password_hash, form.password.data):
			db.session.delete(item)
			db.session.commit()
			flash('Deleted Successfully', 'info')
			return redirect(url_for('project.dashboard'))

		else:
			flash('Password Incorrect', 'danger')

	return render_template('project/delete.html', item=item, form=form)