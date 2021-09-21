import re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import receiver
from django.utils.deconstruct import deconstructible
from django.utils.html import mark_safe


@deconstructible
class _PhoneValidator:

    _pattern = re.compile(
    "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
)

    def __call__(self, value):
        if not self._pattern.match(value):
            raise ValidationError("{!r}, Value is not phone number.".format(value))

class User(AbstractUser):
    phone = models.CharField(
        max_length=20,
        validators=[_PhoneValidator()],
        null=True,
        verbose_name="User",
        )

    def show_image(self):
        return mark_safe('<img src="{}" widtg="100%" />'.format("https://www.google.com/search?q=avatarsds&tbm=isch&ved=2ahUKEwi52on5xpDzAhXHIRoKHW_DD4gQ2-cCegQIABAA&oq=avatarsds&gs_lcp=CgNpbWcQAzoFCAAQgAQ6BAgAEBNQmAxYyRJg0xNoAHAAeACAAW2IAZ4CkgEDMi4xmAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=VxFKYfnSMsfDaO-Gv8AI&bih=619&biw=1354&client=ubuntu&hs=jJS&hl=ru#imgrc=HiicI_NiFTZlXM"))
    show_image.short_description = "Avatar"
    show_image.allow_tags = True

    def send_sms(self, message):
        ...

    def __str__(self):
        return self.username
    


    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"

@receiver(pre_save, sender=User)
def hash_passwd(sender, instance, **kwargs):
    print(kwargs)
    if (instance.id is None) or (sender.object.get(id=instance.id).password != instance.password):
        instance.set_password(instance.password)
     