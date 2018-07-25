from django.shortcuts import render
from django.core import serializers
from life.models import *

def index(request):
    all_groups = Group.objects.all()
    all_reviews = Review.objects.all()
    all_students = Student.objects.all()
    all_tutors = Tutor.objects.all()
    return render(request, 'life/index.html', {"groups": all_groups, "reviews": all_reviews, "students": all_students, "tutors": all_tutors})

def groups(request):
    if request.method == 'POST':
        print('hi')