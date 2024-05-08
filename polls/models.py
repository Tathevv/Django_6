from django.db import models

# Create your models here.

DRAFT_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published')
)


class Manufacture(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    address = models.CharField(max_length=100)
    draft = models.CharField(max_length=30, choices=DRAFT_CHOICES)
    photo = models.ImageField(upload_to='photos/')


class Car(models.Model):
    COLOR_CAR = (
        ('white', 'White'),
        ('black', 'Black'),
        ('red', 'Red'),
        ('grey', 'Grey'),
        ('blue', 'Blue')
    )
    additional_name = models.ManyToManyField(Manufacture, blank=True, related_name='additional',)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    date = models.DateField()
    color = models.CharField(max_length=30, choices=COLOR_CAR)
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
