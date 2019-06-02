from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
	objAboutSection= AboutSection.objects.get(id=1)
	objExperienceSection = ExperienceSection.objects.all()
	objEducationSection = EducationSection.objects.all()
	objProjectSection = ProjectSection.objects.all()
	objSkillsIconSection = SkillsIconSection.objects.all()
	objAwardSection = AwardSection.objects.all()
	objSocialIconsAndLinks = SocialIconsAndLinks.objects.all()
	context = {

		"objAbout" : objAboutSection ,
		"objExperience" : objExperienceSection,
		"objEducation" : objEducationSection,
		"objProject" : objProjectSection,
		"objSkillsIcon" : objSkillsIconSection,
		"objAward" : objAwardSection,
		"objSocialIconsAndLinks" : objSocialIconsAndLinks
	} 
	return render(request,"index.html",context)
