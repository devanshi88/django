# Generated by Django 3.0.4 on 2020-04-21 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('E_mail', models.EmailField(max_length=100)),
                ('Contect', models.IntegerField(max_length=10)),
                ('Image', models.ImageField(upload_to='Image')),
                ('Proporties', models.IntegerField(max_length=100)),
            ],
        ),
    ]
