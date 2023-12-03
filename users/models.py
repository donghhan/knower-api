from django.db import models, transaction
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class KnowerUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("필수 요소가 빠졌습니다(KnowerUserManager 에러)")
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except Exception as e:
            raise e

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_admin") is not True:
            raise ValueError("Error: is_staff sets to False.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Error: is_superuser sets to False.")

        return self.create_user(email, password, **extra_fields)


class KnowerUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="E-mail", unique=True, max_length=64)
    first_name = models.CharField(verbose_name="이름", max_length=30, blank=True)
    last_name = models.CharField(verbose_name="성", max_length=30, blank=True)
    mobile_number = models.CharField(verbose_name="휴대전화번호", max_length=30, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="활동 여부")
    is_superuser = models.BooleanField(default=False, verbose_name="어드민 ")
    is_admin = models.BooleanField(default=False, verbose_name="어드민")

    objects = KnowerUserManager()

    USERNAME_FIELD = "email"

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
