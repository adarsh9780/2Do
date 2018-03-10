from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import re

def length_validator(seq):
    if len(seq) != 13:
        raise ValidationError(
            _('Provided number is not a valid number'),
        )

message = "Please enter a valid 10 digit number. Do not use +91."
regex = r'^+91[0-9]{10}'
regex_validator = RegexValidator(regex=regex, message=message)

# Create your models here.
class ToDoModel(models.Model):
    name = models.CharField(max_length=40)
    time = models.DateTimeField()
    to_do = models.TextField()
    phone_number = models.CharField(max_length=13, validators=[regex_validator, length_validator])


    def __str__(self):
        return self.to_do
