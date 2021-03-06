from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.core.mail import send_mail
from django.db import models


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, account_name, is_staff, is_superuser, **extra_fields):
        """
                Creates and saves a User with the given email and password.
                """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        account_name = self.normalize_account_name(account_name)
        user = self.model(email=email,
                          is_staff=is_staff,
                          account_name=account_name,
                          is_active=True,
                          is_superuser=is_superuser,
                          last_login=now,
                          date_joined=now,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, account_name, password=None, **extra_fields):
        return self._create_user(email, password, account_name, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """
    account_name = models.CharField(_('account_name'), max_length=30, unique=True, blank=False)
    email = models.EmailField(_('email address'), max_length=254, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=False)
    last_name = models.CharField(_('last name'), max_length=30, blank=False)
    # Phones
    phone_number = models.CharField(_('home phone number'), max_length=30, blank=False,
                                    help_text=_('Required. digits and +-() only.'),
                                    validators=[validators.RegexValidator(r'^[0-9+()-]+$',
                                                                          _('Enter a valid phone number.'),
                                                                          'invalid')])
    mobile_number = models.CharField(_('mobile number'), max_length=30, blank=False,
                                     help_text=_('Required. digits and +-() only.'),
                                     validators=[validators.RegexValidator(r'^[0-9+()-]+$',
                                                                           _('Enter a valid mobile number.'),
                                                                           'invalid')])
    # Address
    zip_code = models.CharField(_('zip code'), max_length=5, blank=False,
                                help_text=_('Required. digits only.'),
                                validators=[validators.RegexValidator(r'^[0-9]+$',
                                                                      _('Enter a valid bank number.'),
                                                                      'invalid')])
    home_address = models.CharField(_('home address'), max_length=60, blank=False)

    # Bank ID
    # bank_id_first = models.CharField(_('bank number'), max_length=3, blank=False,
    #                                  help_text=_('Required. digits only.'),
    #                                  validators=[validators.RegexValidator(r'^[0-9]+$',
    #                                                                        _('Enter a valid bank id number.'),
    #                                                                        'invalid')])
    # bank_id_last = models.CharField(_('bank account'), max_length=3, blank=False,
    #                                 help_text=_('Required. digits only.'),
    #                                 validators=[validators.RegexValidator(r'^[0-9]+$',
    #                                                                       _('Enter a valid bank account id number.'),
    #                                                                       'invalid')])

    # Admin
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])
