from django.contrib.auth.backends import BaseBackend
from .models import User
import logging

class CustomUserModelBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            logging.debug(f'Attempting to log in with email: {email}')
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        return None