from django.db import models

# Create your models here.

class Daily(models.Model):
    date_add = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return str(self.pk)


class Article(models.Model):
    STATUS_CHOICE=(
    ('0','pending'),
    ('1','published'),
    )
    raw_url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='0')
    comment = models.TextField()
    daily = models.ForeignKey(Daily)

    def __unicode__(self):
        return str(self.pk) + ' ' + self.title
