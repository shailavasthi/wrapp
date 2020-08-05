from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from app.models import User, Project, Idea, Outline, Draft

class NewProjectForm(FlaskForm):
	title = StringField('Project Title', validators=[DataRequired()])
	progress = SelectField('Current Progress', choices=[(0,"I haven't started"),
														(25,"I need to write an outline"),
														(50,'I have an outline'),
														(75, 'I have a draft')])
	submit = SubmitField('Create Project')

class DeleteForm(FlaskForm):
	password = PasswordField('Enter Your Password', validators=[DataRequired()])
	submit = SubmitField('Delete Project')

class IdeaEditorForm(FlaskForm):
	title = StringField('Topic', validators=[DataRequired()])
	idea_freewrite = TextAreaField('Freewrite', validators=[DataRequired()])
	idea_question = StringField('Question', validators=[DataRequired()])
	submit = SubmitField('Save Idea')