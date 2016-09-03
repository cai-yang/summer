from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

def __unicode__(self):
    return str(self.name)

class Daily(models.Model):
    STATUS_CHOICE=(
    ('0','unpulblished'),
    ('1','published'),
    )
    date_add = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICE,default='0')

    def __unicode__(self):
        return 'daily' + str(self.pk)


class Article(models.Model):
    STATUS_CHOICE=(
    ('0','pending'),
    ('1','published'),
    )
    raw_url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now=True)
    #status = models.CharField(max_length=2, choices=STATUS_CHOICE, default='0')
    comment = models.TextField(blank=True)
    daily = models.ForeignKey(Daily, null=True, blank=True)
    category = models.ManyToManyField(Category,blank=True)

    def __unicode__(self):
        return str(self.pk) + ' ' + self.title
