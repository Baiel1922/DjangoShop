from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from shop_root.settings import EMAIL_HOST_USER

class MyUserManager(BaseUserManager):
    def _create(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email не может быть пустым')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', False)
        extra_fields.setdefault('is_staff', False)
        return self._create(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        return self._create(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(primary_key=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=8, blank=True, default='')
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def generate_activation_code(self):
        from django.utils.crypto import get_random_string

        code = get_random_string(6)
        self.activation_code = code
        self.save()
        return code

    def send_activation_email(self, email, code):
        message = f"""
            Your activation code {code}
        """
        send_mail('Account activation!',
                  message,
                  EMAIL_HOST_USER,
                  [email, ]
                  )

    def activate_with_code(self, activation_code):
        if self.activation_code != activation_code:
            raise Exception('Wrong activation code')
        self.is_active = True
        self.activation_code = ''
        self.save()

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, obj=None):
        return self.is_staff

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    total_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.email