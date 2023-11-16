from django.contrib.auth.models import BaseUserManager,PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, first_name,last_name,password=None,gender=None,birthdate_month=None,birthdate_year=None,birthdate_day=None,phone_number =None,**extra_fields):
        if not email: 
            raise ValueError("User must enter email address")
        if not first_name:
            raise ValueError("User must enter First Name")
        if not last_name:
            raise ValueError("User must enter Last Name")
        
        user = self.model(email = self.normalize_email(email),first_name = first_name,last_name = last_name,gender =gender ,birthdate_year = birthdate_year,birthdate_month=birthdate_month,birthdate_day=birthdate_day,phone_number = phone_number,**extra_fields)        

        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user
    



    def create_superuser(self, email, first_name,last_name,password):
        user = self.create_user(email=email, first_name=first_name,last_name=last_name,password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user




# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError("The Email field must be set")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)

#         return self.create_user(email, password, **extra_fields)

