from unicodedata import name
from django.db import models
from django .contrib.auth.models import AbstractUser
import uuid
# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=50)
    id = models.UUIDField(primary_key=True, editable=False,default=uuid.uuid4)#changing the id using uuid for more securiy
    re_password = models.CharField(max_length=30)
    
    

    
    def __str__(self):
        return self.username


