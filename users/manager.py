from django.contrib.auth.base_user import BaseUserManager


class BaseManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not first_name or not last_name:      
            raise ValueError("User must have a first name and a last name.")
        if not email:
            raise ValueError("User must have an email.")
        if not password:
            raise ValueError("User must have a password.")
        
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email = self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
