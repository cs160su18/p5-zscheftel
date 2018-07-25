from django.db import models

class Group(models.Model):
	established = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
  
# class Review(models.Model):
#   reviewer = models.CharField(max_length=50)
#   recipient = models.CharField(max_length=50)
#   rating = models.IntegerField(5, 1)
#   contents = models.CharField(max_length=2000)
  
# class Message(models.Model):
#   sender = models.CharField(max_length=50)
#   recipient = models.CharField(max_length=50)
#   contents = models.CharField(max_length=2000)

class Student(models.Model):
  name = models.CharField(max_length=50)
  username = models.CharField(max_length=20)
  password = models.CharField(max_length=20)

class Tutor(models.Model):
  name = models.CharField(max_length=50)
  username = models.CharField(max_length=20)
  password = models.CharField(max_length=20)
  rating = models.IntegerField(default=5)
  # profile pic not supported currently

class Review(models.Model):
  reviewer = models.ForeignKey(Student, on_delete=models.CASCADE)
  recipient = models.ForeignKey(Tutor, on_delete=models.CASCADE)
  rating = models.IntegerField(default=5)
  contents = models.CharField(max_length=2000)