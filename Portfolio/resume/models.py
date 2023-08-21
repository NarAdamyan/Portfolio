from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

User=get_user_model()

class PersonalInfo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    short_description=models.TextField(max_length=80)

class Initials(models.Model):
    first_name=models.TextField()
    last_name=models.TextField()
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Skill(models.Model):
    name=models.TextField()
    value=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.name} skill value is {self.value} 80 %"
     

class Education(models.Model):
    university_name=models.TextField()
    start_date=models.DateField()
    grade=models.TextField()
    end_date=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.university_name}  is graduated in {self.end_date}"    
    


class Infos(models.Model):
    type=models.TextField()
    result=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.type} {self.result}"
    
class For_clients(models.Model):
    emoji=models.ImageField()
    count=models.IntegerField()
    text=models.TextField()
    def __str__(self) -> str:
        return f"{self.text}"

class Summery(models.Model):
    title=models.TextField(max_length=30)
    name_surname=models.CharField(max_length=50)  
    short_cv=models.CharField(max_length=200) 
    phone_number=models.IntegerField()
    adress=models.CharField(max_length=35)
    e_mail=models.EmailField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.name_surname} {self.phone_number}"   

class Experience(models.Model):
    title=models.CharField(max_length=15)
    position=models.TextField(max_length=15)
    start_date = models.PositiveIntegerField(validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    end_date = models.PositiveIntegerField(validators=[MaxValueValidator(2023), MinValueValidator(1900)])
    location=models.TextField()
    activity=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.position}{self.start_date}-{self.end_date}"


class Header(models.Model):
    title=models.TextField()
    subtitle=models.TextField()
    def __str__(self) -> str:
        return f"{self.title}"
    
class Services(models.Model):
    logo=models.ImageField()
    title=models.TextField()
    text=models.TextField()
    def __str__(self) -> str:
        return f"{self.title}"
    
class Languages(models.Model):
    language=models.CharField(max_length=15)
    level=models.CharField(max_length=20)    
    def __str__(self) -> str:
        return f"{self.language}"
    
class Courses(models.Model):
    type=models.CharField(max_length=15)
    company=models.CharField(max_length=20)    
    def __str__(self) -> str:
        return f"{self.type}"    
     
class Stuff(models.Model):
    img=models.ImageField()
    initials=models.TextField()
    position=models.TextField()
    text=models.TextField()
    def __str__(self) -> str:
        return f"{self.initials}, {self.position}"     
 

class Count_Box(models.Model):
    emojy=models.TextField(blank=True,null=True,max_length=30)
    count=models.IntegerField(blank=True,null=True)
    title=models.TextField()
    subtitle=models.TextField()  
    def __str__(self) -> str:
        return f"{self.title} as head"   

class SocialLinks(models.Model):
    linkname=models.TextField(max_length=50)   
    iconas=models.CharField(max_length=20)  
    def __str__(self):
        return f"{self.linkname}"
    
class PortfolioProject(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    short_description = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    category = models.CharField(max_length=50)
    client = models.CharField(max_length=50)
    date = models.DateField(null=True, blank=True)
    url = models.URLField()


    def __str__(self) -> str:
        return self.name    
    
class Message(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=1000)  
