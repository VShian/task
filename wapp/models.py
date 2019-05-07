from django.db import models

GENDER_CHOICES=(
    ('male','MALE'),
    ('female', 'FEMALE'),
    ('other','OTHER'),
)

class User(models.Model):
	name=models.CharField(max_length=255)
	gender=models.CharField(max_length=6, choices=GENDER_CHOICES, default='other')
	email=models.EmailField(max_length=255)
	password=models.CharField(max_length=255)