# Generated by Django 2.0.13 on 2019-02-18 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailnhsukfrontendsettings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=False)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('link_url', models.URLField(blank=True)),
                ('link_label', models.CharField(blank=True, max_length=255)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
