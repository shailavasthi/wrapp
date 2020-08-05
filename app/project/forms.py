from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from app.models import User, Project, Idea, Outline, Draft

class NewProjectForm(FlaskForm):
	title = StringField('Project Title', validators=[DataRequired()])
	submit = SubmitField('Submit')

class DeleteForm(FlaskForm):
	password = PasswordField('Enter Your Password', validators=[DataRequired()])
	submit = SubmitField('Delete Project')