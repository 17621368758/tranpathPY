# Generated by Django 2.0.5 on 2018-07-05 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0021_userrole'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='parentSellerId',
            field=models.IntegerField(null=True, verbose_name='所属商家（seller.id，null:系统商家或供应商）'),
        ),
    ]
