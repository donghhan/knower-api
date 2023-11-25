from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class KnowerUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, mobile_number, password=None):
        if not email or not first_name or not last_name or not mobile_number:
            raise ValueError("You missed required value.")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, first_name, last_name, mobile_number, password=None
    ):
        admin_user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            mobile_number=mobile_number,
        )
        admin_user.is_admin = True
        admin_user.save(using=self._db)
        return admin_user


class KnowerUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="E-mail", unique=True, max_length=64)
    first_name = models.CharField(verbose_name="이름", max_length=30)
    last_name = models.CharField(verbose_name="성", max_length=30)
    mobile_number = models.CharField(verbose_name="휴대전화번호", max_length=30)
    is_active = models.BooleanField(default=True, verbose_name="비휴면 여부")
    is_admin = models.BooleanField(default=False, verbose_name="어드민")

    objects = KnowerUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "mobile_number"]

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        verbose_name = "유저"
        verbose_name_plural = "유저"
        db_table = "users"
