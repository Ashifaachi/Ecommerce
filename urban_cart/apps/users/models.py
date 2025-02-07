# from django.db import models

# # Create your models here.
# class Register(models.Model):
#     username = models.CharField(max_length=150)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=20)
#     def __str__(self):
#         return self.username

# # class Login(models.Model):
# #     u_name = models.CharField(max_length=150)
# #     u_password = models.CharField(max_length=20)
    
# #     def __str__(self):
# #         return self.u_name
# class Login(models.Model):
#     username = models.CharField(max_length=150)
#     password = models.CharField(max_length=20)

#     def __str__(self):
#         return self.username
    

# class Logout(models.Model):
#     username = models.ForeignKey(Register,on_delete=models.CASCADE)
#     email = models.ForeignKey(Register,on_delete=models.CASCADE)
#     password = models.ForeignKey(Register,on_delete=models.CASCADE)
#     def __str__(self):
#         return self.username






from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.

class RegisterManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

# class Register(models.Model):
#     username = models.CharField(max_length=150)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=20)

#     def __str__(self):
#         return self.username
class Register(AbstractBaseUser, PermissionsMixin):  # Inherit from PermissionsMixin
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'  # Default is 'username' if you want to use it as the login identifier.
    REQUIRED_FIELDS = ['email']  # Required fields for user creation (exclude password)

    objects = RegisterManager()

    def __str__(self):
        return self.username

# class Login(models.Model):
#     user = models.ForeignKey(Register, on_delete=models.CASCADE)  # Link to Register
#     password = models.CharField(max_length=20)

#     def __str__(self):
#         return f"Login for {self.user.username}"


# class Logout(models.Model):
#     user = models.ForeignKey(Register, on_delete=models.CASCADE)  # Link to Register

#     def __str__(self):
#         return f"Logout for {self.user.username}"
    
# class State(models.Model):
#     s_name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.s_name

# class District(models.Model):
#     s_name = models.ForeignKey(State,on_delete=models.CASCADE)
#     d_name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.d_name
# class State(models.Model):
#     name = models.CharField(max_length=100, unique=True, verbose_name="State Name")

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ['name']  # States will be ordered alphabetically by name


# class District(models.Model):
#     state = models.ForeignKey(
#         State,
#         on_delete=models.CASCADE,
#         related_name='districts',
#         verbose_name="State"
#     )
#     name = models.CharField(max_length=100, unique=True, verbose_name="District Name")

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ['name']  # Districts will be ordered alphabetically by name
# class State(models.Model):
#     name = models.CharField(max_length=100, unique=True)

#     def __str__(self):
#         return self.name

# class District(models.Model):
#     name = models.CharField(max_length=100)
#     state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="districts")

#     class Meta:
#         unique_together = ('name', 'state')  # Ensure unique districts within a state

#     def __str__(self):
#         return f"{self.name}, {self.state.name}"
class State(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, related_name='districts', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
class Account(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)  # Adjust the max_length based on phone number requirements
    address = models.TextField()
    address2 = models.TextField(blank=True, null=True)  # Optional
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    pin = models.CharField(max_length=10)  # Assuming postal codes are alphanumeric

    def __str__(self):
        return f"{self.username} ({self.email})"


