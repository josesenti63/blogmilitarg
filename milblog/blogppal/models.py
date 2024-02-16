from django.db import models
from django.utils import timezone #Agregamos librerias para controlar las fechas de los posteos
from django.contrib.auth.models import User
# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLICADO)


class Post(models.Model):

    class Status(models.TextChoices):
        BORRADOR = 'BR', 'Borrador'
        PUBLICADO = 'PB', 'Publicado'

    titulo_post = models.CharField(max_length= 250) #Titulo del posteo a cargar
    slug = models.SlugField(max_length=250) #Mas adelante va a servir para busquedas
    autor = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    cuerpo_post = models.TextField() #Cuerpo del posteo.
    publicado = models.DateTimeField(default=timezone.now)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, 
                              choices = Status.choices,
                              default = Status.BORRADOR)
    objects = models.Manager()
    publicac = PublishedManager()

    class Meta:
        ordering = ['publicado'] #Le indicamos que se va a ordenar por fecha de publicacion
        indexes = [models.Index(fields=['publicado']),]

    def __str__(self):
        return self.titulo_post #Esto lo usamos para definir el nombre y usarlo en varias aplicaciones
