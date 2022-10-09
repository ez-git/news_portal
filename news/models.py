from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True) # Не обязательно к заполнению no need to fill
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# id - int - django will create it auto if primary key not found
# title - varchar
# content text
# created_at
# updated_at - datetime
# photo - image
# is_publish - bool