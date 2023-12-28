from django.conf import settings
from django.db import models
# from customauth.models import ClientUserModel

# Create your models here.
class Order(models.Model):
    EVENT_CATEGORIES = (
        ('n','new year'),
        ('c','ծնունդ'),
        ('h','wdngg'),
        ('k','knnq'),
        ('f','furshette'),
        ('x','exkurs'),
    )
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    shows = models.ManyToManyField('Entertainment', verbose_name='show')
    # event
    category = models.CharField(verbose_name='tesak, inch?', max_length=1, choices=EVENT_CATEGORIES)
    venue = models.CharField(max_length=150, verbose_name='wortegh?')
    date = models.DateTimeField(verbose_name='erb?')
    # validate budget_min <= budget_max
    budget_min = models.PositiveSmallIntegerField(verbose_name='bjuge1')
    budget_max = models.PositiveSmallIntegerField(verbose_name='bjuge2')
    participants = models.PositiveSmallIntegerField(verbose_name='tiv')
    children = models.BooleanField(default=False, verbose_name='երեխայի, բալիկի համար')
    corporate = models.BooleanField(default=False, verbose_name='korporativ?')
    company = models.CharField(max_length=150, verbose_name='work', blank=True, null=True)
    details = models.TextField(max_length=500, verbose_name='lracucich pahanjner, manramasner, hatuk cankutyunner', blank=True, null=True)
    real = models.BooleanField(default=False, verbose_name='is not test?', choices=((True,'real'),(False,'test')))
    pending = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True) 
    modified = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ['-modified']


class Entertainment(models.Model):
    category = models.CharField(max_length=150)
    description = models.TextField(max_length=500, blank=True, null=True)

    SHOWS = (
        ('d','dance'),
        ('h','host'),
        ('s','sing'),
        ('f','fun'),
        ('m','music'),
        ('k','kostume'),
    )

    def __str__(self):
        return self.category