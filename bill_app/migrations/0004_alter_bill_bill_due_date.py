# Generated by Django 3.2.9 on 2021-12-02 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill_app', '0003_alter_bill_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_due_date',
            field=models.DateField(),
        ),
    ]