# Generated by Django 4.0.6 on 2022-07-09 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationInfo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Org_Code', models.CharField(max_length=5)),
                ('Org_Name', models.CharField(max_length=100)),
                ('Org_ShortName', models.CharField(max_length=10)),
            ],
        ),
    ]