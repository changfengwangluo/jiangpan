"""GuoPan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import xadmin
from index import views
from django.conf.urls.static import static
from . import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/',xadmin.site.urls),#xadmin后台
    #path('',index),
    path('',views.index,name='index'),#首页
    ###关于我们
    path('about/',views.about,name='about'),#关于我们
    path('gongsiwenhua/',views.gongsiwenhua,name='gongsiwenhua'),#关于我们
    path('tuanduichengyuan/',views.tuanduichengyuan,name='tuanduichengyuan'),#团队成员
    path('qiyerongyu/',views.qiyerongyu,name='qiyerongyu'),#企业荣誉
    path('lianxiwomen/',views.lianxiwomen,name='lianxiwomen'),#联系我们
    ###
    ###产品展示
    path('chanpinzhanshi/',views.chanpinzhanshi,name='chanpinzhanshi'),#产品展示
    path('chanpinfenlei/<int:category_id>',views.chanpinfenlei,name='chanpinfenlei'),#产品分类
    path('chanpin/<int:goods_id>',views.chanpin,name='chanpin'),#产品详情

    ###技术培训
    path('jishupeixun/',views.jishupeixun,name='jishupeixun'),#技术培训
    path('peixunmingxi/',views.peixunmingxi,name='peixunmingxi'),#培训明细

    ###招商引资
    path('zhaoshangyinzi/',views.zhaoshangyinzi,name='zhaoshangyinzi'),#招商引资

    ###风光景点
    path('fengguangjingdian/',views.fengguangjingdian,name='fengguangjingdian'),#风光景点
    path('jingdianfenlei/<int:category_id>',views.jingdianfenlei,name='jingdianfenlei'),#景点分类
    path('jingdianmingxi/<int:jingdian_id>',views.jingdianmingxi,name='jingdianmingxi'),#景点明细

    ###新闻资讯
    path('xinwenzixun/', views.xinwenzixun, name='xinwenzixun'),  # 新闻资讯
    path('zixuncategory/<int:category_id>', views.zixuncategory, name='zixunfenlei'),  # zixunfenlei
    path('zixunmingxi/<int:article_id>', views.zixunmingxi, name='zixunmingxi'),  # 资讯明细

    #ckeditor上传路径
    path('ckeditor',include('ckeditor_uploader.urls')),



]
#添加media文件路径访问
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

