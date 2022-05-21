# Generated by Django 4.0.4 on 2022-05-21 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Routers_Switches', '0004_interface'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='Device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Routers_Switches.router'),
        ),
        migrations.AlterField(
            model_name='interface',
            name='Name',
            field=models.CharField(max_length=500),
        ),
        migrations.CreateModel(
            name='Intermediate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.ManyToManyField(null=True, to='Routers_Switches.interface')),
            ],
        ),
    ]