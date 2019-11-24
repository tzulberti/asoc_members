# Generated by Django 2.0.4 on 2019-10-15 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_update_group_and_perms'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsor',
            options={'ordering': ['organization_name'], 'permissions': (('set_sponsors_enabled', 'puede habilitar patrocinadores'), ('view_sponsors', 'puede ver patrocinadores'))},
        ),
        migrations.AlterModelOptions(
            name='sponsoring',
            options={'ordering': ['sponsor__organization_name'], 'permissions': (('close_sponsoring', 'puede cerrar patrocinio'),)},
        ),
    ]