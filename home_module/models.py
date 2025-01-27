from django.db import models
from .validators import validate_pdf
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
# Create your models here.
class PersonalInformation(models.Model):
    name = models.CharField(max_length=150,verbose_name='Name and surname')
    job = models.CharField(max_length=500,verbose_name='Job title')
    personal_background_image = models.ImageField(upload_to='Background-Personal/',verbose_name='Personal background image')
    main_profile = models.ImageField(upload_to='Main-Profile/',verbose_name='Profile picture')
    about_me = models.TextField(verbose_name='About')
    years_experience = models.IntegerField(verbose_name='Years experience')
    curriculum_vitae = models.FileField(upload_to='pdfs/',validators=[validate_pdf],verbose_name='Curriculum vitae') 
    uploaded_at = models.DateTimeField(auto_now_add=True)
    services_main_description = models.TextField(verbose_name='Services main description')
    
    # Our Customer Feedback
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.name
    
class PersonalServices(models.Model):
    logo = models.ImageField(upload_to='PersonalServices/logo/',verbose_name='Logo')
    title = models.CharField(max_length=150,verbose_name='Title')
    description = models.TextField(verbose_name='Services description')
    person = models.ForeignKey(PersonalInformation,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title    
     
class PersonalSkills(models.Model):
    title = models.CharField(max_length=150,verbose_name='Title')
    percentage = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],verbose_name='Percentage')
    person = models.ForeignKey(PersonalInformation,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title     
    
class PersonalLastestWork(models.Model):
    title = models.CharField(max_length=150,verbose_name='Title')
    image = models.ImageField(upload_to='Lastes-work/',verbose_name='Image')
    person = models.ForeignKey(PersonalInformation,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title     


        
class OurCustomerFeedback(models.Model):
    profile = models.ImageField(upload_to='PersonalServices/Opinionprofile/',verbose_name='Profile')
    name = models.CharField(max_length=150,verbose_name='Name and surname')
    job = models.CharField(max_length=500,verbose_name='Job title')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(PersonalInformation, related_name='comments', on_delete=models.CASCADE)  
    
    def __str__(self):
        return self.name
        