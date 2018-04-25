# Generated by Django 2.0.2 on 2018-04-24 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('substances', '0001_initial'),
        ('thermophysical_properties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PLSBL_T',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=30)),
                ('pressure', models.DecimalField(decimal_places=3, max_digits=30)),
                ('density', models.DecimalField(decimal_places=1, max_digits=30)),
                ('enthalpy', models.DecimalField(decimal_places=1, max_digits=30)),
                ('HEBP', models.DecimalField(decimal_places=1, max_digits=30)),
                ('entropy', models.DecimalField(decimal_places=3, max_digits=30)),
                ('DV', models.DecimalField(decimal_places=1, max_digits=30)),
                ('TC', models.DecimalField(decimal_places=1, max_digits=30)),
                ('substance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='substances.Substance')),
            ],
            options={
                'verbose_name_plural': 'Свойства жидких веществ на линии кипения (по температурам)',
                'verbose_name': 'Свойства жидкого вещества на линии кипения (по температурам)',
            },
        ),
    ]