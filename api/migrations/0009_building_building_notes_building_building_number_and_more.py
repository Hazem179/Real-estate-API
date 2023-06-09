# Generated by Django 4.1.7 on 2023-05-07 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_contractrequestform'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='building_notes',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='building_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='buildingimage',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.building'),
        ),
    ]
