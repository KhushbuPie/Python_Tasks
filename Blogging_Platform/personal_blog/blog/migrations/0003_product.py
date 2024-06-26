# Generated by Django 5.0.6 on 2024-06-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postwithdetails_alter_category_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
