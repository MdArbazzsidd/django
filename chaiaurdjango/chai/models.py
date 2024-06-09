from django.db import models 
from django.utils import timezone 

from django.contrib.auth.models import User

# Create your models here.
class chaiverity(models.Model):

    chai_option=[
        ('PC','PLANE CHAI'),
        ('RC','RED CHAI'),
        ('MC','MASALA CHAI'),
        ('ZC','ZINGER CHAI'),
        ('LC','LEMON CHAI '),
    ]

    CHAI_PRICES = {
        'PC': 20,  # Plane Chai price
        'RC': 50,  # Red Chai price
        'MC': 60,  # Masala Chai price
        'ZC': 100, # Zinger Chai price
        'LC': 160, # Lemon Chai price
    }
    name= models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais/')
    date_added= models.DateTimeField(default=timezone.now)
    chai_type=models.CharField(max_length=2, choices=chai_option)
    price= models.IntegerField(default=0)
    description= models.TextField(default='')

    def __str__(self):
        return f"{self.name} - {self.get_chai_type_display()} - {self.price}"

# one to many relation

class chaiReview(models.Model):
    chai = models.ForeignKey(chaiverity, on_delete= models.CASCADE , related_name='Review')

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    ratting_Choices = [
        (1,'1 star'),
        (2, '2 star'),
        (3, '3 star'),
        (4, '4 star'),
        (5, '5 star'),
    ]

    ratting= models.IntegerField(choices=ratting_Choices)

    comment =  models.TextField(default='give us your fells')

    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self) :
        return f'{self.user.username} review for {self.chai.name} and ratting got {self.ratting}'



# many to many realtion 

class store(models.Model):

    name = models.CharField(max_length=100)

    location = models.CharField(max_length=100)

    chai_varaities = models.ManyToManyField(chaiverity, related_name='stores')

    def __str__(self):
        return f'{self.name}'
    
# one to one realtionship

class chaiCertificate(models.Model):
    chai = models.OneToOneField(chaiverity, on_delete=models.CASCADE, related_name='certificate')

    certificate_no = models.CharField(max_length=100)

    issued_date = models.DateTimeField(default=timezone.now)

    valid_date = models.DateTimeField()

    def __str__(self):
        return f'Certificate for : {self.chai.name}'
    
