from django.db import models
from datetime import datetime
# Create your models here.

#专合社信息
class Zhuanheshe(models.Model):
    name=models.CharField(verbose_name='名称',max_length=255)
    address=models.CharField(verbose_name='办公地址',max_length=255)
    faren=models.CharField(verbose_name='法人',max_length=255)
    phone=models.CharField(verbose_name='法人联系手机',max_length=255)
    lishia=models.CharField(verbose_name='理事1',max_length=255)
    lishib=models.CharField(verbose_name='理事2',max_length=255)
    lishic=models.CharField(verbose_name='理事3',max_length=255)
    jianshi=models.CharField(verbose_name='监视',max_length=255)
    caiwu=models.CharField(verbose_name='财务',max_length=255)
    caiwutel=models.CharField(verbose_name='财务联系电话',max_length=255)


    class Meta:
        verbose_name = '专合社信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#车辆使用记录
class Cheliangjilu(models.Model):
    name=models.CharField(verbose_name='车主（签字）',max_length=100)
    phone=models.CharField(verbose_name='车主联系电话',max_length=100)
    chepai=models.CharField(verbose_name='车牌',max_length=100)
    chuche=models.CharField(verbose_name='出车时间',max_length=100)
    yongtu=models.CharField(verbose_name='出车用途',max_length=100)
    licheng=models.CharField(verbose_name='行驶里程',max_length=100)
    qianzi=models.CharField(verbose_name='董事长签字',max_length=100)
    beizhu=models.CharField(verbose_name='备注',max_length=255)

    class Meta:
        verbose_name = '车辆使用记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 公章使用记录
class Gongzhangjilu(models.Model):
    name = models.CharField(verbose_name='使用人（签字）', max_length=100)
    phone = models.CharField(verbose_name='使用人联系电话', max_length=100)
    shiyong = models.CharField(verbose_name='使用事由', max_length=100)
    qianzi = models.CharField(verbose_name='董事长签字', max_length=100)
    beizhu = models.CharField(verbose_name='备注', max_length=255)

    class Meta:
        verbose_name = '公章使用记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
