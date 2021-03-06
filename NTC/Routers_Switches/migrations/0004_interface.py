# Generated by Django 4.0.4 on 2022-05-17 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Routers_Switches', '0003_rename_routers_router'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=80)),
                ('Form_Factor', models.CharField(choices=[('virtual', 'virtual'), ('1G', '1G'), ('10G', '10G'), ('100G', '100G')], max_length=90, null=True)),
                ('Device', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Routers_Switches.router')),
            ],
        ),
    ]
