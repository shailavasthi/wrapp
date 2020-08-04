from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, unique=True)
	email = db.Column(db.String, unique=True)
	first_name = db.Column(db.String)
	last_name = db.Column(db.String)
	password_hash = db.Column(db.String)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	projects = db.relationship('Project', backref='author', lazy='dynamic')

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<User {}>'.format(self.username)    

class Project(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	title = db.Column(db.String)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

	def __repr__(self):
		return '<Project {}>'.format(self.title)    

class Idea(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
	title = db.Column(db.String)
	idea_freewrite = db.Column(db.String)
	idea_question = db.Column(db.String)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

	def __repr__(self):
		return '<Idea {}>'.format(self.title)    

class Outline(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

	title = db.Column(db.String)

	topic = db.Column(db.String)


	section_1_title = db.Column(db.String)
	section_2_title = db.Column(db.String)
	section_3_title = db.Column(db.String)
	section_4_title = db.Column(db.String)
	section_5_title = db.Column(db.String)
	section_6_title = db.Column(db.String)
	section_7_title = db.Column(db.String)
	section_8_title = db.Column(db.String)
	section_9_title = db.Column(db.String)
	section_10_title = db.Column(db.String)

	section_1_body = db.Column(db.Text)
	section_2_body = db.Column(db.Text)
	section_3_body = db.Column(db.Text)
	section_4_body = db.Column(db.Text)
	section_5_body = db.Column(db.Text)
	section_6_body = db.Column(db.Text)
	section_7_body = db.Column(db.Text)
	section_8_body = db.Column(db.Text)
	section_9_body = db.Column(db.Text)
	section_10_body = db.Column(db.Text)

	def __repr__(self):
		return '<Outline {}>'.format(self.title)    


class Draft(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
	version = db.Column(db.Integer)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	title = db.Column(db.String)

	topic = db.Column(db.String)

	section_1_title = db.Column(db.String)
	section_2_title = db.Column(db.String)
	section_3_title = db.Column(db.String)
	section_4_title = db.Column(db.String)
	section_5_title = db.Column(db.String)
	section_6_title = db.Column(db.String)
	section_7_title = db.Column(db.String)
	section_8_title = db.Column(db.String)
	section_9_title = db.Column(db.String)
	section_10_title = db.Column(db.String)

	section_1_body = db.Column(db.Text)
	section_2_body = db.Column(db.Text)
	section_3_body = db.Column(db.Text)
	section_4_body = db.Column(db.Text)
	section_5_body = db.Column(db.Text)
	section_6_body = db.Column(db.Text)
	section_7_body = db.Column(db.Text)
	section_8_body = db.Column(db.Text)
	section_9_body = db.Column(db.Text)
	section_10_body = db.Column(db.Text)

	def __repr__(self):
		return '<Draft {}>'.format(self.title)    

