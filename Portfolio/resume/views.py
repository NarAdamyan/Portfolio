from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def portfolio(request):
    return render(request,"portfolio.html")
def about_me(request):
    return render(request,"about_me.html")
def home(request):
    skills=Skill.objects.all()
    initials=Initials.objects.all()
    header=Header.objects.all()
    infos=Infos.objects.all()
    countBox=Count_Box.objects.all()
    experience=Experience.objects.all()
    education=Education.objects.all()
    summery=Summery.objects.all()
    data = {"title_about_me" : "Embrace the challenge, unleash your potential, and watch your coding skills soar as a junior Python developer."
            ,"skills":skills,"initials":initials,"header":header,"infos1":infos[:4],"infos2":infos[4:],"countBox1":countBox[:2],"countBox2":countBox[2:],"experience":experience
            ,"education":education,"summery":summery}  
    return render(request,"index.html",context=data) 
     
    # context={"first_name":"Narine","last_name":"Adamyan", "deep_drop":["Deep Drop Down 1","Deep Drop Down 2","Deep Drop Down 3","Deep Drop Down 4","Deep Drop Down 5"],    
    # "drop_down":["Drop Down 1", "Drop Down 2","Drop Down 3","Drop Down 4"],"hero":"Code your imagination into reality - Python development for limitless innovation.","navBar":["Home","About","Resume","Services","Portfolio"]
    # ,"infos1":[{"type":"Name","result":" Narine Adamyan"},{"type":"Website","result":"NarAdamyan"},{"type":"Phone","result":"+37498710722"},{"type":"City","result":"Armenia, Sisian"}],"infos2":[{"type":"Age","result":"27"},{"type":"Degree","result":"Bachelor"},{"type":"PhEmailone","result":"naradamyan995@gmail.com"},{"type":"Freelance","result":"Available"}],
    #  "title_about_me":"Embrace the challenge, unleash your potential, and watch your coding skills soar as a junior Python developer."})

