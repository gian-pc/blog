from django.db import models


# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='persona/avatar', blank=True, null=True)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True, unique=True)
    pdf = models.FileField(upload_to='persona/pdf', blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)

    class Meta:
        verbose_name_plural = 'Persona'
        ordering = ['-apellido']
        # Modifica el nombre de la TABLA en la DB
        # db_table = 'Persona'


class Skills(models.Model):
    codigo = models.CharField(max_length=8, primary_key=True)
    skill = models.CharField(max_length=150)
    nivel = models.IntegerField()
    estado = models.BooleanField(default=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=True, null=True)
    imagen = models.CharField(max_length=350, null=True, blank=True)
    descripcion = models.TextField(blank=True, null=True)
    video = models.CharField(max_length=350, null=True, blank=True)

    def __str__(self):
        return '({}) {}'.format(self.codigo, self.skill)

    class Meta:
        verbose_name_plural = 'Skill'
        ordering = ['skill']


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    imagen = models.CharField(max_length=350, null=True, blank=True)
    estado = models.BooleanField(default=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = 'Post'
        ordering = ['fecha']
