from django.db import models
from django.forms import ModelForm

class Foo(models.Model):
    date = models.DateTimeField(help_text = 'Date')

    def __unicode__(self):
        return unicode(self.date)

class FooForm(ModelForm):
    class Meta:
        model = Foo
