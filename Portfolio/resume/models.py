from django.db import models

# Create your models here.
class Initials(models.Model):
    first_name=models.TextField()
    last_name=models.TextField()
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Skill(models.Model):
    name=models.TextField()
    value=models.IntegerField()
    def __str__(self) -> str:
        return f"{self.name} skill value is {self.value} 80 %"
     

class Education(models.Model):
    university_name=models.TextField()
    start_date=models.DateField()
    grade=models.TextField()
    end_date=models.DateField()
    def __str__(self) -> str:
        return f"{self.university_name}  is graduated in {self.end_date}"    
    


class Infos(models.Model):
    type=models.TextField()
    result=models.TextField()
    def __str__(self) -> str:
        return f"{self.type} {self.result}"
    
class For_clients(models.Model):
    emoji=models.ImageField()
    count=models.IntegerField()
    text=models.TextField()
    def __str__(self) -> str:
        return f"{self.text}"

class Summery(models.Model):
    title=models.TextField()
    name_surname=models.TextField()  
    short_cv=models.TextField() 
    phone_number=models.IntegerField()
    adress=models.TextField()
    e_mail=models.TextField()
    def __str__(self) -> str:
        return f"{self.name_surname} {self.phone_number}"   

class Experience(models.Model):
    title=models.TextField()
    position=models.TextField()
    start_date=models.DateField()
    end_date=models.DateField()
    location=models.TextField()
    activity=models.TextField()
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

class Stuff(models.Model):
    img=models.ImageField()
    initials=models.TextField()
    position=models.TextField()
    text=models.TextField()
    def __str__(self) -> str:
        return f"{self.initials}, {self.position}"     

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