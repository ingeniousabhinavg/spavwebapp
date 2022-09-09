from email.mime import image
import profile
from pyexpat import model
from unicodedata import name
from django.db import models
from djrichtextfield.models import RichTextField
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

# finance commitee #
class Fc(models.Model):
    name = models.CharField(max_length=50)
    DESIG_CHOICES = (
            ('Chairperson Finance Commitee','Chairperson Finance Commitee'),
            ('Secoratry Finance Commitee','Secoratry Finance Commitee'),
    )
    designation = models.CharField(max_length=50, choices=DESIG_CHOICES)
    # profile_Pic = models.ImageField(upload_to='profiles', max_length=254)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.name
# finance commitee #

# bwc commitee #
class Bwc(models.Model):
    name = models.CharField(max_length=50)
    DESIG_CHOICES = (
            ('Chairperson BWC Commitee','Chairperson BWC Commitee'),
            ('Secoratry BWC Commitee','Secoratry BWC Commitee'),
    )
    designation = models.CharField(max_length=50, choices=DESIG_CHOICES)
    # profile_Pic = models.ImageField(upload_to='profiles', max_length=254)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.name
# bwc commitee #

# bwc commitee #
class Senate(models.Model):
    name = models.CharField(max_length=50)
    DESIG_CHOICES = (
            ('Chairman Senate','Chairman Senate'),
            ('Dy Senate','Dy Senate'),
    )
    designation = models.CharField(max_length=50, choices=DESIG_CHOICES)
    # profile_Pic = models.ImageField(upload_to='profiles', max_length=254)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.name
# bwc commitee #

# bwc commitee #
class Deans(models.Model):
    name = models.CharField(max_length=50)
    DESIG_CHOICES = (
            ('Dean Academics','Dean Academics'),
            ('Dean Planning and Development','Dean Planning and Development'),
            ('Dean Students Affair','Dean Students Affair'),
            ('Dean Faculty Welfare','Dean Faculty Welfare'),
            ('Dean Research','Dean Research'),
    )
    designation = models.CharField(max_length=50, choices=DESIG_CHOICES)
    profile_Pic = models.ImageField(upload_to='profiles', max_length=254)
    email = models.EmailField(max_length=254, null=False, default='cv')
    phone = models.CharField(max_length=14, default=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    duties = models.TextField(null=False, default="Duties and Responsibilities of Deans")

    def __str__(self) -> str:
        return self.name
# bwc commitee #

# administration #
class Administration(models.Model):
    name = models.CharField(max_length=50)
    DESIG_CHOICES = (
            ('Registrar','Registrar'),
            ('Assistant Registrar','Assistant Registrar'),
            ('DY. Librarian','DY. Librarian'),
            ('System Administrator','System Administrator'),
            ('Assistant Librarian','Assistant Librarian'),
            ('Technical Officer','Technical Officer'),
            ('Assistant Engineer Cum Project Officer','Assistant Engineer Cum Project Officer'),
            ('Accountant, Accounts Section','Accountant, Accounts Section'),
            ('Multi-Skill Assistant, Director`s Office','Multi-Skill Assistant, Director`s Office'),
            ('Multi Skill Assistant','Multi Skill Assistant'),
            ('Junior Engineer Civil','Junior Engineer Civil'),
            ('Junior Engineer Electrical','Junior Engineer Electrical'),
            ('Accountant','Accountant'),
            ('Library Assistant','Library Assistant'),
            ('Lab Attendant','Lab Attendant'),
    )
    designation = models.CharField(max_length=50, choices=DESIG_CHOICES)
    profile_Pic = models.ImageField(upload_to='profiles', max_length=254)
    email = models.EmailField(max_length=254, null=False, default='cv')
    phone = models.CharField(max_length=14, default=True)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return self.name
# administration #

# comitees #
class Faculty2(models.Model):
    full_name = models.CharField(max_length=30)
    commitee_CHOICES = (
            ('Professor','Professor'),
            ('Assistant Professorr','Assistant Professorr'),
    )
    designation = models.CharField(max_length=50, choices=commitee_CHOICES)
    DEPT_CHOICES =(
        ('Architecture','Architecture'),
        ('Planning','Planning')
    )
    department = models.CharField(max_length=50, choices=DEPT_CHOICES)
    profile_Pic = models.ImageField(upload_to='profiles', max_length=254)
    email = models.EmailField(max_length=254, null=False, default='cv')
    phone = models.CharField(max_length=14, default=True)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return "%s %s" % (self.full_name, self.designation)

class Commitee(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']

# comitees #

# fic #
class FIC(models.Model):
    name = models.CharField(max_length=50)
    RESP_CHOICES = (
            ('Grievance Cell','Grievance Cell'),
            ('Sexual Harassment of Women at workplace','Sexual Harassment of Women at workplace'),
            ('Art Lab','Art Lab'),
            ('Climatology/Energy Studies/Acoustic Lab','Climatology/Energy Studies/Acoustic Lab'),
            ('Structures lab/Material Testing Lab & Survey Lab','Structures lab/Material Testing Lab & Survey Lab'),
            ('Conservation Lab','Conservation Lab'),
            ('Landscape Lab','Landscape Lab'),
            ('Material and Construction Lab','Material and Construction Lab'),
            ('Computer Labs (Architecture , GIS )','Computer Labs (Architecture , GIS )'),
            ('Construction Yard','Construction Yard'),
            ('Model Making and Carpentry Workshop','Model Making and Carpentry Workshop'),
            ('Transportation Lab','Transportation Lab'),
            ('Environmental Lab','Environmental Lab'),
            ('Cultural Committee Head','Cultural Committee Head'),
            ('Nodal Office, Student Scholarships','Nodal Office, Student Scholarships'),
    )
    responsibility = models.CharField(max_length=50, choices=RESP_CHOICES)
    email = models.EmailField(max_length=254, null=False, default='cv')
    phone = models.CharField(max_length=14, default=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    duties = models.TextField(null=False, default="Duties and Responsibilities of Deans")

    def __str__(self) -> str:
        return self.name
# fic #