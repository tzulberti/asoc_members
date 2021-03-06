# Generated by Django 2.0.4 on 2018-07-08 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_auto_20180707_1619'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='person',
            name='membership',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='person', to='members.Member', verbose_name='membresía'),
            preserve_default=False,
        ),
    ]
