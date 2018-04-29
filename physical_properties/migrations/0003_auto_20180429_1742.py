# Generated by Django 2.0.2 on 2018-04-29 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('substances', '0001_initial'),
        ('physical_properties', '0002_auto_20180419_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='BPCG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('molecular_mass', models.CharField(max_length=100)),
                ('density', models.CharField(max_length=100)),
                ('gas_constant', models.CharField(max_length=100)),
                ('critical_temperature', models.CharField(max_length=100)),
                ('critical_pressure', models.CharField(max_length=100)),
                ('critical_density', models.CharField(max_length=100)),
                ('triple_point_temperature', models.CharField(max_length=100)),
                ('evaporation_heat', models.CharField(max_length=100)),
                ('fusion_heat', models.CharField(max_length=100)),
                ('boiling_temperature', models.CharField(max_length=100)),
                ('fluid_density', models.CharField(max_length=100)),
                ('heat_capacity_cp', models.CharField(max_length=100)),
                ('heat_capacity_cv', models.CharField(max_length=100)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='substances.Substance')),
            ],
            options={
                'verbose_name_plural': 'Значения основных физических констант газов',
                'verbose_name': 'Значение основных физических констант газов',
            },
        ),
        migrations.CreateModel(
            name='MCAFT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.CharField(max_length=100)),
                ('moisture', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Значения влагосодержания воздуха',
                'verbose_name': 'Значение влагосодержания воздуха',
            },
        ),
        migrations.CreateModel(
            name='MCC_PT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.CharField(max_length=100)),
                ('pressure', models.CharField(max_length=100)),
                ('moisture', models.CharField(max_length=100)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='substances.Substance')),
            ],
            options={
                'verbose_name_plural': 'Значения влагосодержания криопродуктов',
                'verbose_name': 'Значение влагосодержания криопродукта',
            },
        ),
        migrations.AlterModelOptions(
            name='acda',
            options={'verbose_name': 'Усредненный состав воздуха', 'verbose_name_plural': 'Усредненный состав воздуха'},
        ),
    ]
