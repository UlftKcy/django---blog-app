# Generated by Django 3.2.8 on 2021-10-25 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20211025_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics/'),
        ),
    ]
