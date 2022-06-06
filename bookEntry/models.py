from django.db import models

# Create your models here.
from django.db import models  
class BookEntry(models.Model):  
    code = models.CharField(max_length=20)  
    title = models.CharField(max_length=100)  
    author = models.CharField(max_length=50)  
    language = models.CharField(max_length=15) 
    edition = models.CharField(max_length=15) 

    class Meta:  
        db_table = "bookEntry" 