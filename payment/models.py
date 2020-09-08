from django.db import models
from jobtest.utils import card_validator, present_or_future_date
from django.core.validators import ValidationError, MinValueValidator, MinLengthValidator
# Create your models here.


class DetailCard(models.Model):
    # to do how to make fields requiered
    credit_card_number = models.CharField(
        max_length=19, blank=False, verbose_name='credit card number')
    card_holder = models.CharField(
        max_length=250, blank=False, verbose_name='card holder')
    expiration_date = models.DateField(
        validators=[present_or_future_date], blank=False, verbose_name='expiration date')
    security_code = models.CharField(validators=[MinLengthValidator(3)],
                                     max_length=3, blank=True, verbose_name='security code')
    amount = models.DecimalField(
        decimal_places=2, max_digits=12, validators=[MinValueValidator(0)], verbose_name='amount')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self, *args, **kwargs):
        is_card_valid = card_validator(self.credit_card_number)
        if not is_card_valid:
            raise ValidationError('Invalid Card Number')
        super().clean(*args, **kwargs)
