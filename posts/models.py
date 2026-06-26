from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'categorias'

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    content = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts"
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    content = models.TextField()
    criado_em = (models.DateTimeField(auto_now_add=True))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios')

    def __str__(self):
        return f"{self.autor} em {self.post}"
    