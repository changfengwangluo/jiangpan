from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse, Http404
from . import models


# Create your views here.

# 首页
def index(request):
    context = {}
    companyinfo = models.CompanyInfo.objects.all()[0]  # 企业信息
    goodscategory = models.GoodsCategory.objects.all()  # 产品分类
    # 产品
    goods = models.Goods.objects.all()[:12]
    # 风景分类
    fengjingfenlei = models.FengjingCategory.objects.all()
    fengjing = models.Fengjing.objects.all()
    # 新闻分类
    chanye = models.ArticleCategory.objects.get(name='产业新闻')
    chanyearticles = get_list_or_404(models.Article, category=chanye.id)
    meiti = models.ArticleCategory.objects.get(name='媒体报道')
    meitiarticles = get_list_or_404(models.Article, category=meiti.id)
    kepu = models.ArticleCategory.objects.get(name='科普园地')
    kepuarticles = get_list_or_404(models.Article, category=kepu.id)
    #所有资讯分类
    zixunfenlei = models.ArticleCategory.objects.all()
    # 团队成员
    tuandui = models.Tuandui.objects.all()[:6]
    # 企业荣誉
    rongyu = models.Rongyu.objects.all()[:6]

    # context['companyinfo'] = companyinfo
    # context['goodscategory'] = goodscategory
    # context['chanyearticles'] = chanyearticles
    # context['meitiarticles'] = meitiarticles
    # context['kepuarticles'] = kepuarticles
    # context['tuandui'] = tuandui
    # context['rongyu'] = rongyu
    # context['goods'] = goods
    # context['fengjingfenlei'] = fengjingfenlei
    # context['fengjing'] = fengjing,
    # context['chanyeid'] = chanye.id,
    # context['meitiid'] = meiti.id,
    # context['kepuid'] = kepu.id,
    # context['zixunfenlei'] = zixunfenlei,
    #复制给字典的方式在这个版本中不太稳定。就把字典直接写在render里面。
    return render(request, 'index.htm',{
        'companyinfo':companyinfo,
        'goodscategory':goodscategory,
        'chanyearticles':chanyearticles,
        'meitiarticles':meitiarticles,
        'kepuarticles':kepuarticles,
        'tuandui':tuandui,
        'rongyu':rongyu,
        'goods':goods,
        'fengjingfenlei':fengjingfenlei,
        'fengjing':fengjing,
        'chanyeid':chanye.id,
        'meitiid':meiti.id,
        'meitiid':meiti.id,
        'kepuid':kepu.id,
        'zixunfenlei':zixunfenlei,

    } )


###
# 关于我们
def about(request):
    companyinfo = models.CompanyInfo.objects.all()[0]  # 企业信息
    return render(request, 'a/guanyuwomen/qiyejianjie/index.html', {'companyinfo': companyinfo})


# 公司文化
def gongsiwenhua(request):
    companyinfo = models.CompanyInfo.objects.all()[0]  # 企业信息
    return render(request, 'a/guanyuwomen/gongsiwenhua/index.html', {'companyinfo': companyinfo})


# 团队成员
def tuanduichengyuan(request):
    tuandui = models.Tuandui.objects.all()
    return render(request, 'a/guanyuwomen/tuanduichengyuan/index.html', {'tuandui': tuandui})


# 企业荣誉
def qiyerongyu(request):
    rongyu = models.Rongyu.objects.all()
    return render(request, 'a/guanyuwomen/qiyerongyu/index.html', {'rongyu': rongyu})


# 联系我们
def lianxiwomen(request):
    companyinfo = models.CompanyInfo.objects.all()[0]  # 企业信息
    return render(request, 'a/guanyuwomen/lianxiwomen/index.html', {'companyinfo': companyinfo})


###产品展示
# 产品展示
def chanpinzhanshi(request):
    goods = models.Goods.objects.all()
    goodscategory = models.GoodsCategory.objects.all()

    return render(request, 'a/chanpinzhanshi/index.html', {'goods': goods, 'goodscategory': goodscategory})


# 产品分类
def chanpinfenlei(request, category_id):
    goodscategory = models.GoodsCategory.objects.all()
    goods = get_list_or_404(models.Goods, category=category_id)
    fenleixinxi=models.GoodsCategory.objects.get(id=category_id)
    return render(request, 'a/chanpinzhanshi/list.html', {
        'goods': goods,
        'goodscategory': goodscategory,
        'fenleixinxi': fenleixinxi,

    })


# 产品详情
def chanpin(request, goods_id):
    goods = get_object_or_404(models.Goods, id=goods_id)  # 产品信息
    # +++++++++ 前台组合图片
    goodsimgs = goods.imagea.url + '+++++++++' + goods.imageb.url + '+++++++++' + goods.imagec.url + '+++++++++' + goods.imaged.url + '+++++++++' + goods.imagee.url + '+++++++++' + goods.imagef.url

    allgoods = get_list_or_404(models.Goods)  # 所有产品

    return render(request, 'a/chanpinzhanshi/info.html', {'goods': goods, 'goodsimgs': goodsimgs, 'allgoods': allgoods})


###技术培训
# 技术培训
def jishupeixun(request):
    jishu = models.ArticleCategory.objects.get(name='技术培训')
    articles = get_list_or_404(models.Article, category=jishu.id)

    return render(request, 'a/jishupeixun/index.html', {'articles': articles})


# 培训明细
def peixunmingxi(request, category_id):
    return render(request, 'a/jishupeixun/info.html', {})


###招商引资
def zhaoshangyinzi(request):
    zhaoshang = models.ArticleCategory.objects.get(name='招商引资')
    articles = get_list_or_404(models.Article, category=zhaoshang.id)
    return render(request, 'a/zhaoshangyinzi/index.html', {'articles': articles})


###风光景点
# 风光景点
def fengguangjingdian(request):
    # 风景分类
    fengjingfenlei = models.FengjingCategory.objects.all()

    fengjing = models.Fengjing.objects.all()

    return render(request, 'a/fengguangjingdian/index.html', {
        'fengjingfenlei': fengjingfenlei,
        'fengjing': fengjing
    })


# 风景分类
def jingdianfenlei(request, category_id):
    fenlei = get_list_or_404(models.FengjingCategory)

    jingdian = models.Fengjing.objects.filter(category=category_id)
    fenleixinxi=models.FengjingCategory.objects.get(id=category_id)
    return render(request, 'a/fengguangjingdian/list.html', {
        'fenlei': fenlei,
        'jingdian': jingdian,
        'fenleixinxi': fenleixinxi,

    })


# 景点明细
def jingdianmingxi(request, jingdian_id):
    jingdianfenlei = get_list_or_404(models.FengjingCategory)

    jingdian = get_object_or_404(models.Fengjing, id=jingdian_id)
    jingdianimgs = jingdian.imagea.url + '+++++++++' + jingdian.imageb.url + '+++++++++' + jingdian.imagec.url + '+++++++++' + jingdian.imaged.url + '+++++++++' + jingdian.imagee.url + '+++++++++' + jingdian.imagef.url
    tuijian = models.Fengjing.objects.order_by('?')[:6]
    return render(request, 'a/fengguangjingdian/info.html', {
        'jingdianfenlei': jingdianfenlei,
        'jingdian': jingdian,
        'jingdianimgs': jingdianimgs,
        'tuijian': tuijian
    })


# 新闻资讯
# 新闻资讯
def xinwenzixun(request):
    zixunfenlei=models.ArticleCategory.objects.all()
    articles = models.Article.objects.all()
    return render(request, 'a/xinwenzixun/index.html', {'articles': articles,'zixunfenlei':zixunfenlei})


# category
def zixuncategory(request, category_id):
    zixunfenlei = models.ArticleCategory.objects.all()
    zixunlist = get_list_or_404(models.Article, category=category_id)
    fenleiinfo=models.ArticleCategory.objects.get(id=category_id)
    return render(request, 'a/xinwenzixun/list.html', {
        'zixunlist': zixunlist,
        'zixunfenlei':zixunfenlei,
        'fenleiinfo':fenleiinfo,

    })


# 资讯明细
def zixunmingxi(request, article_id):

    article = models.Article.objects.get(id=article_id)
    
    xiangguan = models.Article.objects.order_by('?')[:4]
    zixunfenlei = models.ArticleCategory.objects.all()



    return render(request, 'a/xinwenzixun/article.html', {
        'article':article,
        'xiangguan':xiangguan,
        'zixunfenlei':zixunfenlei,
    })
