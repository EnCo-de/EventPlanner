from django.conf import settings
from django.db import models
# from customauth.models import ClientUserModel

# Create your models here.
class Order(models.Model):
    EVENT_CATEGORIES = (
        ('a','այլ, ստորև նշեք մանրամասները'),
        ('n','ամանորյա երեկույթ'),
        ('b','ծնունդ'),
        ('e','նշանադրություն'),
        ('h','հարսանեկան խնջույք'),
        ('w','հարսանյաց արարողություն'),
        ('c','մկրտություն, կնունք'),
        ('t','տուրիզմ, զբոսաշրջություն'),
        ('x','էքսկուրսիա'),
        ('m','այցելություն թանգարան'),
        ('s','շոու ծրագիր'),
        ('z','concert ծրագիր'),
        ('y','room decoration'),
        ('p','product expo'),
        ('l','conference'),
        ('k','կորպորատիվ'),
        ('f','ֆուրշետ քեյթրինգ'),
    )
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    shows = models.ManyToManyField('Entertainment', verbose_name='Բաղադրիչներ', help_text='Սեղմած պահեք «Control» Windows-ում կամ «Command» Mac-ում՝ մեկից ավելի ընտրելու համար:')
    # event
    category = models.CharField(verbose_name='Իրադարձություն', max_length=1, choices=EVENT_CATEGORIES)
    venue = models.CharField(max_length=150, verbose_name='Անցկացման վայր')
    date = models.DateTimeField(verbose_name='Ամսաթիվ 21/09/2023 12:34')
    # validate budget_min <= budget_max
    budget_min = models.PositiveSmallIntegerField(verbose_name='նվազագույն բյուջե', help_text='հազար դրամ')
    budget_max = models.PositiveSmallIntegerField(verbose_name='առավելագույն բյուջե', help_text='հազար դրամ')
    participants = models.PositiveSmallIntegerField(verbose_name='մասնակիցների թիվը')
    children = models.BooleanField(default=False, verbose_name='երեխայի, բալիկի համար է')
    corporate = models.BooleanField(default=False, verbose_name='կորպորատիվ է')
    company = models.CharField(max_length=150, verbose_name='Ընկերության Անվանումը', blank=True, null=True)
    details = models.TextField(max_length=500, verbose_name='լրացուցիչ պահանջներ, մանրամասներ, հատուկ ցանկություններ', blank=True, null=True)
    real = models.BooleanField(default=False, 
        verbose_name='Կայքը ներկայումս զուգահեռաբար փորձարկվում է ծրագրավորողների կողմից։ Ընտրեք համապատասխան տարբերակը կազմակերպիչ ընկերությանը փաստացի միջոցառման կազմակերպման հայտարարություն ներկայացնելու և կազմակերպիչների հետ կապվելու համար', 
        choices=(
            (True,'Դա իրական պատվեր է այն միջոցառման համար, որը ցանկանում ենք անցկացնել: Կապվեք կազմակերպիչների հետ:'),
            (False,'Փորձարկում')
            ))
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