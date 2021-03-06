# Generated by Django 3.0.7 on 2020-10-11 20:25

from django.db import migrations, models
import django.db.models.deletion
import places.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_auto_20201011_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placesimages',
            name='image',
            field=models.ImageField(upload_to=places.models.PlacesImages.get_path_to_places_image, verbose_name='Файл с фотографией'),
        ),
        migrations.AlterField(
            model_name='placesimages',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядковый номер'),
        ),
        migrations.AlterField(
            model_name='placesimages',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.Place', verbose_name='Название места'),
        ),
    ]
