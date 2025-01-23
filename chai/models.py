from django.db import models
#importing timezone
from django.utils import timezone

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

