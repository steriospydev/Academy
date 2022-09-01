from django import template
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

register = template.Library()

@register.filter(name="is_instructor")
def is_instructor(user):
    return user.groups.filter(name="Instructors").exists()