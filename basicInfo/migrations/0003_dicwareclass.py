# Generated by Django 2.1.2 on 2018-10-24 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0031_syslog'),
        ('basicInfo', '0002_probrand'),
    ]

    operations = [
        migrations.CreateModel(
            name='DicWareclass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parentId', models.IntegerField(null=True, verbose_name='父类ID')),
                ('name', models.CharField(max_length=50, verbose_name='类目名称')),
                ('sorts', models.IntegerField(null=True, verbose_name='排序')),
                ('memo', models.CharField(max_length=500, null=True, verbose_name='备注')),
                ('addtime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='添加时间')),
                ('updatetime', models.DateTimeField(null=True, verbose_name='最后修改时间')),
                ('deletetime', models.DateTimeField(null=True, verbose_name='删除时间')),
                ('SellerId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dicWareclass_SellerId', to='system.Seller', verbose_name='所属商家（sellers.id）永远为0')),
                ('adder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dicWareclass_adder', to='system.User', verbose_name='添加人（user.id）')),
                ('deleter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dicWareclass_deleter', to='system.User', verbose_name='删除人')),
                ('updater', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dicWareclass_updater', to='system.User', verbose_name='最后修改人（user.id）')),
            ],
        ),
    ]
