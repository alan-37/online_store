# Generated by Django 4.0.1 on 2022-03-16 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('blouse', 'blouse'), ('bag', 'bag'), ('headdress', 'headdress'), ('patch', 'patch'), ('t-shirt', 't-shirt')], default='t-shirt', max_length=20),
        ),
    ]
