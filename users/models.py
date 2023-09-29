from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .manager import BaseManager
from common.models import BaseModel


class User(BaseModel, AbstractBaseUser):
    class Gender(models.TextChoices):
        MALE = "Male"
        FERMALE = "Fermale"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to="user/images/", default='defaultuser.webp')
    gender = models.CharField(max_length=10, choices=Gender.choices)
    phone_number = models.CharField(max_length=13)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = BaseManager()

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class UserVerification(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='verifications')
    code = models.CharField(max_length=4)
    time_limit = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.get_full_name}'s verification ({self.id})"
