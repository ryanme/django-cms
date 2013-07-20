from cms.utils.compat.dj import python_2_unicode_compatible
from django.db import models
from cms.models.fields import PlaceholderField
from hvad.models import TranslatableModel, TranslatedFields


class Example1(models.Model):
    char_1 = models.CharField(u'char_1', max_length=255)
    char_2 = models.CharField(u'char_2', max_length=255)
    char_3 = models.CharField(u'char_3', max_length=255)
    char_4 = models.CharField(u'char_4', max_length=255)
    placeholder = PlaceholderField('placeholder')


class TwoPlaceholderExample(models.Model):
    char_1 = models.CharField(u'char_1', max_length=255)
    char_2 = models.CharField(u'char_2', max_length=255)
    char_3 = models.CharField(u'char_3', max_length=255)
    char_4 = models.CharField(u'char_4', max_length=255)
    placeholder_1 = PlaceholderField('placeholder_1', related_name='p1')
    placeholder_2 = PlaceholderField('placeholder_2', related_name='p2')


class DynamicPlaceholderSlotExample(models.Model):
    char_1 = models.CharField(u'char_1', max_length=255)
    char_2 = models.CharField(u'char_2', max_length=255)
    placeholder_1 = PlaceholderField(related_name='dynamic_pl_1')
    placeholder_2 = PlaceholderField(related_name='dynamic_pl_2')

    def get_placeholder_1_slot(self):
        return self.char_1

    def get_placeholder_2_slot(self):
        return self.char_2


@python_2_unicode_compatible
class MultilingualExample1(TranslatableModel):
    translations = TranslatedFields(
        char_1=models.CharField(u'char_1', max_length=255),
        char_2=models.CharField(u'char_2', max_length=255),
    )
    placeholder_1 = PlaceholderField('placeholder_1')

    def __str__(self):
        return self.char_1