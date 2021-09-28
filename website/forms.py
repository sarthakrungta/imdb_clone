from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from db_models.models import UserReview


# Create your forms here.

class NewUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("username", "password1", "password2")

class ReviewForm():
	class Meta:
		model = UserReview
		fields = ("rating", "review")