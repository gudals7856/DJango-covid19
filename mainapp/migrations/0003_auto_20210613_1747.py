# Generated by Django 3.2.3 on 2021-06-13 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_alignment_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alignment',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='alignment',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
