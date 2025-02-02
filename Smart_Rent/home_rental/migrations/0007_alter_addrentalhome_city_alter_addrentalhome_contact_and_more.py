# Generated by Django 5.0.4 on 2024-06-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_rental', '0006_addrentalhome_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addrentalhome',
            name='City',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='addrentalhome',
            name='Contact',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='addrentalhome',
            name='Description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='addrentalhome',
            name='State',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='addrentalhome',
            name='Street1',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='addrentalhome',
            name='Street2',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
