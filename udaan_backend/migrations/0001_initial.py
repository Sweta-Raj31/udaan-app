# Generated by Django 3.2.5 on 2023-03-19 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('type_content', models.CharField(blank=True, max_length=255, null=True)),
                ('contact', models.BigIntegerField(blank=True, null=True)),
                ('dept', models.CharField(blank=True, max_length=255, null=True)),
                ('college', models.CharField(default='college name', max_length=225)),
                ('content', models.FileField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('subject', models.TextField(blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
