import uuid
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class UserManager(BaseUserManager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404
    def create_user(self, username, email, password=None,
    **kwargs):
    # """Create and return a `User` with an email, phone
    # number, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')
        if password is None:
            raise TypeError('User must have an email.')
        user = self.model(username=username,
        email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email, password,
    **kwargs):
                           
    # Create and return a `User` with superuser (admin) permissions.
     
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        if username is None:
            raise TypeError('Superusers must have a username.')
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    # public_id = models.UUIDField(primary_key=True,db_index=True, unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField(max_length=8, null=True, blank=True)
    profile_image = models.CharField(max_length=500, blank=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

class Fooditem(models.Model):
    options=(
        ('saucer','saucer'),
        ('soup spoon','soup spoon'),
        ('bundle','bundle'),
        ('eye','eye'),
    )
    option1 = (
        ('breakfast','breakfast'),
        ('lunch','lunch'),
        ('diner','diner'),
        ('snacks','snacks'),
    )
    rating=(
        ('low','low'),
        ('moderate','moderate'),
        ('high','high'),
        ('very high','very high'),
    )
    name = models.CharField(max_length=200)
    user = models.ManyToManyField(User)
    category = models.CharField(max_length=40, choices=option1, null=True, blank=True)
    carbohydrate = models.CharField(max_length=150, choices=rating, null=True, blank=True)
    fats = models.CharField(max_length=150, choices=rating, null=True, blank=True)
    protein = models.CharField(max_length=150, choices=rating, null=True, blank=True)
    calorie=models.IntegerField(default=1,null=True,blank=True)
    quantity = models.IntegerField(default=1,null=True,blank=True)
    unit = models.CharField(max_length=150, choices=options, null=True, blank=True)
    image = models.ImageField(upload_to=None, null=True, blank=True)
    
    def __str__(self):
        return str(self.name)
    
    

    
class Dietplan(models.Model):
    DietName = models.CharField(max_length=150)
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.TextField(null=True, blank=True)
    fooditem = models.ForeignKey(Fooditem, on_delete=models.CASCADE)
    duration = models.IntegerField(null=True, blank=True, default=30)
    age = models.IntegerField(null=True, blank=True, default=30)

    def __str__(self):
        return str(self.DietName)