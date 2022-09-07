from email.mime import image
from django.db import models

# Create your models here.

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