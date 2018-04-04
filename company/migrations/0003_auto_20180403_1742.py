# Generated by Django 2.0.2 on 2018-04-03 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20180330_1732'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zhuanheshe',
            options={'verbose_name': '专合社信息', 'verbose_name_plural': '专合社信息'},
        ),
        migrations.AddField(
            model_name='zhuanheshe',
            name='caiwu',
            field=models.CharField(default='', max_length=255, verbose_name='财务'),
        ),
        migrations.AddField(
            model_name='zhuanheshe',
            name='caiwutel',
            field=models.CharField(default='', max_length=255, verbose_name='财务联系电话'),
        ),
        migrations.AddField(
            model_name='zhuanheshe',
            name='jianshi',
            field=models.CharField(default='', max_length=255, verbose_name='监视'),
        ),
        migrations.AddField(
            model_name='zhuanheshe',
            name='lishia',
            field=models.CharField(default='', max_length=255, verbose_name='理事1'),
        ),
        migrations.AddField(
            model_name='zhuanheshe',
            name='lishib',
            field=models.CharField(default='', max_length=255, verbose_name='理事2'),
        ),
        migrations.AddField(
            model_name='zhuanheshe',
            name='lishic',
            field=models.CharField(default='', max_length=255, verbose_name='理事3'),
        ),
        migrations.AlterField(
            model_name='zhuanheshe',
            name='address',
            field=models.CharField(default='', max_length=255, verbose_name='办公地址'),
        ),
        migrations.AlterField(
            model_name='zhuanheshe',
            name='faren',
            field=models.CharField(default='', max_length=255, verbose_name='法人'),
        ),
        migrations.AlterField(
            model_name='zhuanheshe',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='zhuanheshe',
            name='phone',
            field=models.CharField(default='', max_length=255, verbose_name='法人联系手机'),
        ),
    ]
