from django.db import models
from phone_field import PhoneField
from datetime import date

# Create your models here.
class AboutSection(models.Model):
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	address = models.TextField(blank=True, null=True)
	phone = PhoneField(blank=True, help_text='Contact phone number')
	email = models.CharField(max_length = 20)
	about = models.TextField(blank=True, null=True)

class ExperienceSection(models.Model):
	post = models.CharField(max_length = 50)
	company_name = models.CharField(max_length = 50)
	description = models.TextField(blank=True, null=True)
	date_from = models.DateField(blank=True, null=True)
	date_to = models.DateField(blank=True, null=True)
	present = models.BooleanField(default=False)

class EducationSection(models.Model):
	school_name = models.CharField(max_length = 100)
	field_of_study = models.CharField(max_length = 100)
	gpa = models.DecimalField(decimal_places=2, max_digits=10)
	date_from = models.DateField(blank=True, null=True)
	date_to = models.DateField(blank=True, null=True)
	present = models.BooleanField(default=False)

class ProjectSection(models.Model):
	name = models.CharField(max_length = 100)
	link = models.CharField(max_length = 500)

class SkillsIconSection(models.Model):
	icon_name = models.CharField(max_length = 20)

class AwardSection(models.Model):
	description = models.CharField(max_length = 200)

class SocialIconsAndLinks(models.Model):
	icon_name = models.CharField(max_length = 200)
	link = models.CharField(max_length = 200)



