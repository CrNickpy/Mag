from django.db import models
from django.urls import reverse


class Stech(models.Model):
    title = models.CharField('Марка',max_length=50 )
    mod = models.CharField('Модель',max_length=50)
    photo = models.ImageField('Фото', upload_to='media')
    category= models.CharField('Категория',max_length=50)
    specs = models.TextField('Спецификация')
    prise = models.CharField('Цена',max_length=50)
    is_home = models.CharField('Наличие',max_length=250)
    

    class Meta:
        verbose_name = ("Спецтехника")
        verbose_name_plural = ("Спецтехника")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("numer", kwargs={"numer_id": self.pk})

class Otzyv(models.Model):
    name = models.CharField(max_length= 60, verbose_name='Имя')
    text = models.TextField( max_length=1000, verbose_name='Отзыв')
    tel =models.CharField(max_length= 12, verbose_name='Телефон')
    date = models.DateTimeField( verbose_name='Дата')
    
    class Meta:
        verbose_name = ("Отзыв")
        verbose_name_plural = ("Отзывы")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_id": self.pk})


class Client(models.Model):
    name = models.CharField(max_length= 60, verbose_name='Имя')
    tel =models.CharField(max_length= 12, verbose_name='Телефон')
    call = models.CharField(max_length= 60, verbose_name='Звонок',null=True)

    class Meta:
        verbose_name = ("Клиенты")
        verbose_name_plural = ("Клиенты")

    def __str__(self):
        return self.name

    


