from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import MessageForm
from django.shortcuts import get_object_or_404
# Create your views here.

def portfolio(request):
    return render(request,"portfolio.html")
def about_me(request):
    return render(request,"about_me.html")
def home(request):

    status=200

    if request.method=="POST":
        print("POSTED DATA")
        print(request.POST)
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            status=201
        else:
            print("Tell them that data is not valid")

    skills=Skill.objects.all()
    initials=Initials.objects.all()
    header=Header.objects.all()
    infos=Infos.objects.all()
    countBox=Count_Box.objects.all()
    experience=Experience.objects.all()
    education=Education.objects.all()
    summery=Summery.objects.all()
    personal_info=PersonalInfo.objects.get(user__username="narineadamyan")
    social_links=SocialLinks.objects.all()
    message_form=MessageForm()
    data = {"title_about_me" : "Embrace the challenge, unleash your potential, and watch your coding skills soar as a junior Python developer."
            ,"skills":skills,"initials":initials,"header":header,"infos1":infos[:4],"infos2":infos[4:],"countBox1":countBox[:2],"countBox2":countBox[2:],"experience":experience
            ,"education":education,"summery":summery,"personal_info":personal_info,"message_form":message_form, "social_links":social_links}  
    
    return render(request,"index.html",context=data, status=status) 
     
    
