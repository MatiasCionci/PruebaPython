# Generated by Django 3.2.24 on 2024-02-26 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loginn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreU', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fechaNacimiento', models.DateField()),
                ('mail', models.CharField(max_length=50)),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuarios.loginn')),
            ],
        ),
    ]
