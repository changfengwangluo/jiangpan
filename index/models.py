from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
#文章分类
class ArticleCategory(models.Model):
    name=models.CharField(verbose_name='文章分类',max_length=100)

    class Meta:
        verbose_name='文章分类'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name
#文章
class Article(models.Model):
    title=models.CharField(verbose_name='文章标题',max_length=255)
    content=RichTextUploadingField(verbose_name='文章内容')
    create_time=models.DateField(verbose_name='发布时间',auto_now=True)
    category=models.ForeignKey(ArticleCategory,verbose_name='文章分类',on_delete=models.CASCADE)
    chakan=models.IntegerField(verbose_name='查看数')


    class Meta:
        verbose_name='文章'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.title
#友情链接
class Link(models.Model):
    name=models.CharField(verbose_name='链接名',max_length=100)
    url=models.CharField(verbose_name='链接地址',max_length=200)

    class Meta:
        verbose_name='友情链接表'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name
#产品分类
class GoodsCategory(models.Model):
    name=models.CharField(verbose_name='产品分类名',max_length=100)

    class Meta:
        verbose_name='产品分类'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name


#产品
class Goods(models.Model):
    category=models.ForeignKey(GoodsCategory,verbose_name='产品分类',on_delete=models.CASCADE)
    name=models.CharField(verbose_name='产品名',max_length=255)
    price=models.FloatField(verbose_name='产品价格')
    imagea=models.ImageField(verbose_name='产品图片1',upload_to='media/image/%Y/%d')
    imageb=models.ImageField(verbose_name='产品图片2',upload_to='media/image/%Y/%d')
    imagec=models.ImageField(verbose_name='产品图片3',upload_to='media/image/%Y/%d')
    imaged=models.ImageField(verbose_name='产品图片4',upload_to='media/image/%Y/%d')
    imagee=models.ImageField(verbose_name='产品图片5',upload_to='media/image/%Y/%d')
    imagef=models.ImageField(verbose_name='产品图片6',upload_to='media/image/%Y/%d')

    content=RichTextUploadingField(verbose_name='商品描述')

    class Meta:
        verbose_name='产品'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

#风景分类
class FengjingCategory(models.Model):
    name=models.CharField(verbose_name='风景名',max_length=100)

    class Meta:
        verbose_name='风景分类'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name
#风景明细
class Fengjing(models.Model):
    category=models.ForeignKey(FengjingCategory,verbose_name='风景分类',on_delete=models.CASCADE)
    name=models.CharField(verbose_name='风景名',max_length=255)
    imagea=models.ImageField(verbose_name='风景图片1',upload_to='media/image/%Y/%d')
    imageb=models.ImageField(verbose_name='风景图片2',upload_to='media/image/%Y/%d')
    imagec=models.ImageField(verbose_name='风景图片3',upload_to='media/image/%Y/%d')
    imaged=models.ImageField(verbose_name='风景图片4',upload_to='media/image/%Y/%d')
    imagee=models.ImageField(verbose_name='风景图片5',upload_to='media/image/%Y/%d')
    imagef=models.ImageField(verbose_name='风景图片6',upload_to='media/image/%Y/%d')

    content=RichTextUploadingField(verbose_name='风景描述')

    class Meta:
        verbose_name='风景'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name


#网站信息表
class CompanyInfo(models.Model):
    name=models.CharField(verbose_name='公司名',max_length=100)
    logo=models.ImageField(verbose_name='公司LOGO',upload_to='media/image/%Y/%d')
    tel=models.CharField(verbose_name='电话',max_length=100)
    chuanzhen=models.CharField(verbose_name='传真',max_length=100)
    address=models.CharField(verbose_name='地址',max_length=100)
    email=models.CharField(verbose_name='邮件',max_length=100)
    youbian=models.CharField(verbose_name='邮编',max_length=100)
    url=models.CharField(verbose_name='公司网址',max_length=100)
    desc=RichTextUploadingField(verbose_name='网站简介')
    wenhua=RichTextUploadingField(verbose_name='企业文化')
    lianxi=RichTextUploadingField(verbose_name='联系方式')


    class Meta:
        verbose_name='公司信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

#公司团队
class Tuandui(models.Model):
    name=models.CharField(verbose_name='名字',max_length=50)
    zhiwei=models.CharField(verbose_name='职位',max_length=50)
    image=models.ImageField(verbose_name='头像',upload_to='media/image/%Y/%d')
    desc=RichTextUploadingField(verbose_name='个人简介')

    class Meta:
        verbose_name='团队'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name
#荣誉
class Rongyu(models.Model):
    name = models.CharField(verbose_name='荣誉名字', max_length=50)
    image = models.ImageField(verbose_name='荣誉图片', upload_to='media/image/%Y/%d')
    desc = RichTextUploadingField('荣誉描述')

    class Meta:
        verbose_name = '荣誉'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


#轮播图
class Lunbo(models.Model):
    name=models.CharField(verbose_name='图片名',max_length=100)
    image=models.ImageField(verbose_name='轮播图',upload_to='media/image/%Y/%d')
    nick=models.CharField(verbose_name='测试',max_length=100)

    class Meta:
        verbose_name='轮播图'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.image

