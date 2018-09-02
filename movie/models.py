from django.db import models
from django.urls.base import reverse
# Create your models here.
class Movie(models.Model):
    lang_choice=(
            ('ENGLISH','English'),
            ('BENGALI','Bengali'),
            ('HINDI','Hindi'),
            ('TAMIL','Tamil'),
            ('TELUGU','Telugu'),
            ('MALAYALAM','Malayalam'),
            ('MARATHI','Marathi'),
            ('FRENCH','French'),
        )
    rating_choice=(
            ('U','U'),
            ('UA','U/A'),
            ('A','A'),
            ('R','R'),
        )    
    name              =     models.CharField(max_length=20)
    cast              =     models.CharField(max_length=100)
    director          =     models.CharField(max_length=20)
    language          =     models.CharField(max_length=10,choices=lang_choice)
    run_length        =     models.IntegerField(help_text='Enter run length in minutes')
    certificate       =     models.CharField(max_length=2,choices=rating_choice)
    popularity_index  =     models.IntegerField(unique=True,null=True,blank=True)
    trailer           =     models.URLField(blank=True)    
    image             =     models.ImageField(null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('movie:detail',kwargs={'movie_id':self.pk})
    
    def __str__(self):
        return self.name