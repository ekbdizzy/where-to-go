# Generated by Django 3.0.7 on 2020-06-15 22:43

from django.db import migrations, models
import django.db.models.deletion
import places.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Place', 'verbose_name_plural': 'Places'},
        ),
        migrations.CreateModel(
            name='ImagesPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=places.models.PlacesImages.get_path_to_places_image)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.Place')),
            ],
        ),
    ]
