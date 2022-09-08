from email.mime import image
import profile
from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.

class Slider(models.Model):
    altText = models.CharField(max_length=100)
    images = models.ImageField(upload_to='slider')
    link = models.URLField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.altText

class Alert(models.Model):
    alertTitle = models.CharField(max_length=100)
    alertFile = models.FileField(upload_to='alert', max_length=100)
    alertDate = models.DateField(auto_now=False, auto_now_add=False)
    ALERT_CHOICES = (
        ('danger', 'danger'),
        ('warning','warning'),
        ('primary','primary'),
        ('light','light'),
    )
    alertIntensity = models.CharField( max_length=50, choices=ALERT_CHOICES)

    def __str__(self) -> str:
        return self.alertTitle

class Noticeboard(models.Model):
    noticeTitle = models.CharField(max_length=200)
    noticeFile = models.FileField(upload_to='noticeboard', max_length=100)
    noticeUrl = models.URLField(max_length=200, null=True)
    noticeDate = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.noticeTitle

class UpcomingLect(models.Model):
    lectureTitle = models.CharField(max_length=200)
    lectureFile = models.FileField(upload_to='ulect', max_length=100)
    lectureUrl = models.URLField(max_length=200, null=True)
    lectureDate =  models.DateTimeField( auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.lectureTitle

# model for featured logo #
class FeaturedLogo(models.Model):
    altText = models.CharField(max_length=50, null=True)
    logoLink = models.URLField(max_length=200, null=False)
    logoImage = models.FileField(upload_to='flogo', max_length=100, null=False)
    date = models.DateTimeField(auto_now=False, auto_now_add=False, null=False)

    def __str__(self) -> str:
        return self.altText
# model for featured logo #

# students work #
class GlimpseSW(models.Model):
    altText = models.CharField(max_length=100)
    image = models.ImageField(upload_to='studentsglimplse')
    date =  models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.altText
# students work #

## models for permanent positions ##
class SystemAdmin(models.Model):
    name = models.CharField(max_length=50) 
    qualifications = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=14)
    profile_Pic = models.ImageField(upload_to='profiles', max_length=254)
    date =  models.DateField(auto_now=True, auto_now_add=False)


    def __str__(self) -> str:
        return self.name

class TechanicalOfficer(models.Model):
    name = models.CharField(max_length=50) 
    qualifications = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=14,default=True)
    profile_Pic = models.ImageField(upload_to='profiles', max_length=254)
    date =  models.DateField(auto_now=True, auto_now_add=False)


    def __str__(self) -> str:
        return self.name
## models for permanent positions ## 

# faculty database #
class Faculty(models.Model):
    name = models.CharField(max_length=50) 
    DESIG_CHOICES = (
        ('Professor','Professor'),
        ('Associate Professor','Associate Professor'),
        ('Assistant Professor','Assistant Professor'),
    )
    designation = models.CharField(max_length=50, choices=DESIG_CHOICES) 
    qualifications = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=14,default=True)
    profile_Pic = models.ImageField(upload_to='profiles', max_length=254)
    date =  models.DateField(auto_now=True, auto_now_add=False)
    cv = models.FileField(upload_to='cv', max_length=100, default='cv')
    Publications = models.URLField(max_length=200)

    def __str__(self) -> str:
        return self.name

# faculty database #

# chairperson #
class Chairperson(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    DESIG_CHOICES = (
        ('Chairperson','Chairperson'),
        ('Chairperson in Charge ','Chairperson in Charge '),
    )
    designation = models.CharField(max_length=50, choices=DESIG_CHOICES)
    date = models.DateField(auto_now=False, auto_now_add=False)
    profile_Pic = models.ImageField(upload_to='profiles', max_length=254)
    email = models.EmailField(max_length=254, null=False, default='cv')
    phone = models.CharField(max_length=14, default=True)
    cv = models.FileField(upload_to='cv', max_length=100, default='None')

    def __str__(self) -> str:
        return self.name
# chairperson #

# chairperson #
class Director(models.Model):
    name = models.CharField(max_length=50)
    about = models.TextField()
    DESIG_CHOICES = (
        ('Director','Director'),
        ('Director in Charge ','Director in Charge '),
    )
    designation = models.CharField(max_length=50, choices=DESIG_CHOICES)
    date = models.DateField(auto_now=False, auto_now_add=False)
    profile_Pic = models.ImageField(upload_to='profiles', max_length=254)
    email = models.EmailField(max_length=254, null=False)
    phone = models.CharField(max_length=14)
    cv = models.FileField(upload_to='cv', max_length=100, default=None ,null=False)
    Publications = models.URLField(max_length=200)

    def __str__(self) -> str:
        return self.name
# chairperson #

# bog #
class BOG(models.Model):
    name = models.CharField(max_length=50)
    DESIG_CHOICES = (
            ('Chairperson','Chairperson'),
            ('Director SPAV - Ex-Officio - Member','Director SPAV - Ex-Officio - Member'),
            ('Pr. Secretary - GoAP - Member','Pr. Secretary - GoAP - Member'),
            ('Rep. from ITPI - Member','Rep. from ITPI - Member'),
            ('Rep. from AICTE- Member','Rep. from AICTE- Member'),
            ('Rep. from UGC- Member','Rep. from UGC- Member'),
            ('Rep. from CoA- Member','Rep. from CoA- Member'),
            ('JS &FA, MoE - Member','JS &FA, MoE - Member'),
            ('Nominee of MoE - Member','Nominee of MoE - Member'),
            ('Nominee of MoUD- Member','Nominee of MoUD- Member'),
            ('Senate Nominee - 1 (DoA) - Member','Senate Nominee - 1 (DoA) - Member'),
            ('Senate Nominee - 2 (DoP) - Member','Senate Nominee - 2 (DoP) - Member'),
            ('Registrar SPAV - Ex-Officio - Secretary','Registrar SPAV - Ex-Officio - Secretary'),
        )
    designation = models.CharField(max_length=50, choices=DESIG_CHOICES)
    # profile_Pic = models.ImageField(upload_to='profiles', max_length=254)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.name
# bog #