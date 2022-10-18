from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name="Содержание") # Не обязательно к заполнению no need to fill
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")
    image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name="Изображение", blank=True)
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Категория")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

        ordering = ['-created_at', 'title']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['title']
# id - int - django will create it auto if primary key not found
# title - varchar
# content text
# created_at
# updated_at - datetime
# photo - image
# is_publish - bool