# Generated by Django 3.0.5 on 2020-09-15 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0006_auto_20200915_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='damage',
            name='location',
            field=models.CharField(blank=True, choices=[('FRONT', 'Front'), ('REAR', 'Rear'), ('SIDE', 'Side')], default=None, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='imagespace',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='vehicle.Vehicle'),
        ),
        migrations.DeleteModel(
            name='DamageLocation',
        ),
    ]
