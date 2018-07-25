from django import forms

from .models import Student
from .models import Review

class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ('name', 'username', 'password')

class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = {'reviewer', 'recipient', 'rating', 'contents'}