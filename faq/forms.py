"""
Here we define a form for allowing site users to submit a potential FAQ that
they would like to see added.

From the user's perspective the question is not added automatically, but
actually it is, only it is added as inactive.
"""

from __future__ import absolute_import
import datetime
from django import forms
from django.conf import settings
from .models import Question, Topic

class SubmitFAQForm(forms.ModelForm):
    class Meta:
        model = Question
        if settings.FAQ_ALLOW_ANSWER:
            fields = ['topic', 'text', 'answer']
        else:
            fields = ['topic', 'text']
