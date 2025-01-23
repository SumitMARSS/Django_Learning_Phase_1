from django.db import models
#importing timezone
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVarity(models.Model):
    #creating enums
    CHAI_TYPE_CHOICE = [
        ( 'ML', 'MASALA'),
        ( 'GR', 'GINGER'),
        ( 'KL', 'KIWI'),
        ( 'PL', 'PLAIN'),
        ( 'EL', 'ELAICHI'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    # taking choice from enum
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    # keep in smae format as it is python
    def __str__(self):
        return self.name



# one to many

class ChaiReview(models.Model):
    # no need to tell which field is foreign key from chai verity
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    commnet = models.TextField(default="")
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}' 
    

# many to many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varities = models.ManyToManyField(ChaiVarity, related_name="stores")

    def __str__(self):
        return self.name
    
# one to one

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
    certifiate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now())
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name}'
    
