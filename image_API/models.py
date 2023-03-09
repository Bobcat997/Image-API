from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.ForeignKey("Plan", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Plan: {self.plan.name}'


class Plan(models.Model):
    name = models.CharField(max_length=45)
    size = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    link_expiration_time = models.DateTimeField(blank=True, null=True)
    expiration_seconds = models.IntegerField(validators=[MinValueValidator(300), MaxValueValidator(30000)], blank=True,
                                             null=True)


class Thumbnail(models.Model):
    original = models.ForeignKey('Image', on_delete=models.CASCADE)
    image = models.ImageField()
    size = models.IntegerField(default=1)

