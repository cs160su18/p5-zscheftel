from django.shortcuts import render
from django.core import serializers
from life.models import *
from .forms import StudentForm
from .forms import ReviewForm

def index(request):
    all_groups = Group.objects.all()
    all_reviews = Review.objects.all()
    all_students = Student.objects.all()
    all_tutors = Tutor.objects.all()
    return render(request, 'life/index.html', {"groups": all_groups, "reviews": all_reviews, "students": all_students, "tutors": all_tutors})

def groups(request):
    if request.method == 'POST':
        print('hi')

def formpage(request):
    if request.method == "POST":
      s = StudentForm(request.POST)
      post = s.save(commit=False)
      post.save()
    else:
      s = StudentForm()
    return render(request, 'life/formpage.html', {'form': s})
  
def review(request):
    if request.method == "POST":
      r = ReviewForm(request.POST)
      post = r.save(commit=False)
      post.save()
    else:
      r = ReviewForm()
    return render(request, 'life/review.html', {'form': r})