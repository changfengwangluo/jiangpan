from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http import HttpResponse,Http404
from . import models
# Create your views here.

#首页
def index(request):
    data={}

    companyinfo=models.CompanyInfo.objects.all()[0]#企业信息

    goodscategory=models.GoodsCategory.objects.all()#产品分类
    #产品
    goods=models.Goods.objects.all()[:12]

    # 风景分类
    fengjingfenlei = models.FengjingCategory.objects.all()

    fengjing=models.Fengjing.objects.all()

    #新闻分类
    chanye=models.ArticleCategory.objects.get(name='产业新闻')
    chanyearticles=get_list_or_404(models.Article,category=chanye.id)

    meiti = models.ArticleCategory.objects.get(name='媒体报道')
    meitiarticles = get_list_or_404(models.Article, category=meiti.id)

    kepu = models.ArticleCategory.objects.get(name='科普园地')
    kepuarticles = get_list_or_404(models.Article, category=kepu.id)
    #团队成员
    tuandui=models.Tuandui.objects.all()[:6]
    #企业荣誉
    rongyu = models.Rongyu.objects.all()[:6]

    data['companyinfo']=companyinfo
    data['goodscategory']=goodscategory
    data['chanyearticles']=chanyearticles
    data['meitiarticles']=meitiarticles
    data['kepuarticles']=kepuarticles
    data['tuandui']=tuandui
    data['rongyu']=rongyu
    data['goods']=goods
    data['fengjingfenlei']=fengjingfenlei
    data['fengjing']=fengjing



    return render(request,'index.htm',data)
###
#关于我们
def about(request):
    return render(request,'a/guanyuwomen/qiyejianjie/index.html',{})
#公司文化
def gongsiwenhua(request):
    return render(request,'a/guanyuwomen/gongsiwenhua/index.html',{})
#团队成员
def tuanduichengyuan(request):
    return render(request,'a/guanyuwomen/tuanduichengyuan/index.html',{})
#企业荣誉
def qiyerongyu(request):
    return render(request,'a/guanyuwomen/qiyerongyu/index.html',{})
#联系我们
def lianxiwomen(request):
    return render(request,'a/guanyuwomen/lianxiwomen/index.html',{})
###产品展示
# 产品展示
def chanpinzhanshi(request):
    return render(request, 'a/chanpinzhanshi/index.html', {})
# 产品分类
def chanpinfenlei(request,category_id):
    goods=models.Goods.objects.get_list_or_404(category_id=category_id)
    return render(request, 'a/chanpinzhanshi/list.html', {'goods':goods})
# 产品详情
def chanpin(request,goods_id):
    goods=models.Goods.objects.get_list_or_404(id=goods_id)
    return render(request, 'a/chanpinzhanshi/info.html', {'goods':goods})

###技术培训
#技术培训
def jishupeixun(request):
    articles=models.Article.objects.get()
    return render(request, 'a/jishupeixun/index.html', {})
#培训明细
def peixunmingxi(request,category_id):
    return render(request, 'a/jishupeixun/info.html', {})

###招商引资
def zhaoshangyinzi(request):
    return render(request, 'a/zhaoshangyinzi/index.html', {})


###风光景点
#风光景点
def fengguangjingdian(request):
    return render(request, 'a/fengguangjingdian/index.html', {})
#景点明细
def jingdianmingxi(request,):
    return render(request, 'a/fengguangjingdian/info.html', {})


#新闻资讯
#新闻资讯
def xinwenzixun(request):
    articles=models.Article.objects.all()
    return render(request, 'a/xinwenzixun/index.html', {'articles':articles})

#category
def zixuncategory(request,category_id):
    zixunlist=models.Article.objects.get(category=category_id)
    return render(request, 'a/xinwenzixun/info.html', {'zixunlist':zixunlist})

#资讯明细
def zixunmingxi(request,article_id):
    data={}
    article=models.Article.objects.get(id=article_id)
    category_id=models.Article.objects.values('category')
    xiangguan=models.Article.objects.all()[:4]

    data['article']=article
    data['xiangguan']=xiangguan

    return render(request, 'a/xinwenzixun/article.html', data)

