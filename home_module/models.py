from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class WeAreDeconsultOptions(models.Model):
     title = models.CharField(max_length=50, db_index=True, verbose_name='عنوان')
     text = models.TextField(max_length=150,verbose_name='متن توضیحات')
    
     def __str__(self):
        return self.title
   
     class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

class WeAreDeconsult(models.Model):
     title = models.TextField(max_length=150,verbose_name='متن  توضیحات')
     options = models.ManyToManyField(WeAreDeconsultOptions, verbose_name='گزینه ها')
    
     def __str__(self):
        return self.title
     
     class Meta:
        verbose_name = 'عدم مشاوره'
        verbose_name_plural = 'عدم مشورت'

class OurServiceQuestion(models.Model):
     title = models.CharField(max_length=200,verbose_name='عنوان پرسش')
     question = models.CharField(max_length=250,verbose_name='سوالات')
     response = models.CharField(max_length=400,verbose_name='پاسخ سوالات')
     
     def __str__(self):
        return self.title
   
     class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوالات'

class Services(models.Model):
     title = models.CharField(max_length=150,verbose_name='عنوان سرویس')
     
     def __str__(self):
        return self.title
     
     class Meta:
        verbose_name = 'سرویس'
        
class Sentences(models.Model):
     text = models.TextField(max_length=150,verbose_name='متن جمله')
     
     def __str__(self):
        return self.text
   
     class Meta:
        verbose_name = 'جمله'
        verbose_name_plural = 'جملات'  
        
class OurService(models.Model):
     # main_title = models.TextField(max_length=150,verbose_name='متن')
     icon = models.ImageField(upload_to='Ourservice/logo')
     title = models.TextField(max_length=150,verbose_name='عنوان')
     short_desc = models.TextField(max_length=150,verbose_name='متن توضیحات کوتاه')
     main_desc = models.TextField(max_length=350,verbose_name='متن توضیحات')
     image = models.ImageField(upload_to='Ourservice/image', verbose_name='تصویر محصول')
     blue_part_desc = models.TextField(max_length=350,verbose_name='توضیحات قسمت آبی')
     sentences = models.ManyToManyField(Sentences,verbose_name='جملات')
     questions = models.ManyToManyField(OurServiceQuestion,verbose_name='سوالات')
     service = models.ManyToManyField(Services,verbose_name='سرویس ها')
     slug = models.SlugField(default="",null=False,db_index=True,blank=True,max_length=200,unique=True,verbose_name='عنوان در url')
     
     def get_absolute_url(self):
         return reverse('service-detail', args=[self.slug])
     
     def save(self,*args,**kwargs):
        # self.slug = slugify(self.title)
          super().save(*args,**kwargs)
          
     def __str__(self):
        return self.title

     class Meta:
        verbose_name = 'سرویس ما'
        verbose_name_plural = 'سرویس های ما'