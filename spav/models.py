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