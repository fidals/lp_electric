# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-08 07:38
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings

from pages.models import CustomPage


# Inspired by Django doc:
# https://docs.djangoproject.com/en/1.9/ref/contrib/sites/#enabling-the-sites-framework
def set_custom_pages(apps, schema_editor):
    for fields in settings.CUSTOM_PAGES.values():
        CustomPage.objects.create(**fields)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lp_electric', '0002_models_translation'),
    ]

    operations = [
        migrations.RunPython(set_custom_pages),
    ]
