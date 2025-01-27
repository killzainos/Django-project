from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    phone_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=150,verbose_name='موضوع')
    message = models.TextField(verbose_name='متن پیام')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده / نشده توسط ادمین',null=True,blank=True,default=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'ارتباط با ما'
        verbose_name_plural = 'تماس با ما'