from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.core.validators import MinValueValidator, MaxValueValidator


class Basic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Premium(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Enterprise(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    link_expiration_time = models.IntegerField(default=300, validators=[MinValueValidator(300), MaxValueValidator(30000)])


class Image(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    basic = models.ForeignKey(Basic, on_delete=models.PROTECT, blank=True, null=True)
    premium = models.ForeignKey(Premium, on_delete=models.PROTECT, blank=True, null=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.PROTECT, blank=True, null=True)

    @property
    def thumbnail_200px(self):
        if self.basic is not None or self.premium is not None or self.enterprise is not None:
            return default_storage.url(self.image.name + '?height=200')
        return None

    @property
    def thumbnail_400px(self):
        if self.premium is not None or self.enterprise is not None:
            return default_storage.url(self.image.name + '?height=400')
        return None

    @property
    def original_image(self):
        if self.enterprise is not None:
            return default_storage.url(self.image.name)
        return None

    @property
    def expiring_link(self):
        if self.enterprise is not None:
            expiration_time = self.enterprise.link_expiration_time
            return default_storage.url(self.image.name + f'?expires_in={expiration_time}')
        return None
