import xadmin
from xadmin import views
from . import models
class ArticleAdmin(object):

    list_display=['title','create_time','category']
    search_field=['title','create_time','category']

class ArticleCategoryAdmin(object):
    list_display=['name']
    search_field=['name']

class GoodsCategoryAdmin(object):
    list_display = ['name']
    search_field = ['name']

class GoodsAdmin(object):
    list_display = ['name','price','imagea']
    search_field = ['name','price','imagea']

class FengjingAdmin(object):
    list_display = ['name','category']
    search_field = ['name','category']

class FengjingCategoryAdmin(object):
    list_display = ['name']
    search_field = ['name']

class CompanyInfoAdmin(object):
    list_display = ['name','tel','url']
    search_field = ['name','tel','url']


class TuanduiAdmin(object):
    list_display = ['name', 'zhiwei', 'image']
    search_field = ['name', 'zhiwei', 'image']

class RongyuAdmin(object):
    list_display = ['name','image']
    search_field = ['name','image']

class LunboAdmin(object):
    list_display = [ 'name']
    search_field = [ 'name']

xadmin.site.register(models.Lunbo,LunboAdmin)

xadmin.site.register(models.Article,ArticleAdmin)
xadmin.site.register(models.ArticleCategory,ArticleCategoryAdmin)

xadmin.site.register(models.Goods,GoodsAdmin)
xadmin.site.register(models.GoodsCategory,GoodsCategoryAdmin)

xadmin.site.register(models.Fengjing,FengjingAdmin)
xadmin.site.register(models.FengjingCategory,FengjingCategoryAdmin)

xadmin.site.register(models.Tuandui,TuanduiAdmin)
xadmin.site.register(models.CompanyInfo,CompanyInfoAdmin)
xadmin.site.register(models.Rongyu,RongyuAdmin)



#主题设置
class ThemesSettins(object):
    enable_themes=True#启用主题菜单
    use_bootswatch=True#启用主题列表
xadmin.site.register(views.BaseAdminView,ThemesSettins)

class GlobalSettins(object):
    site_title='江畔果香办公后台管理系统'
    site_footer='屏山县江畔果香生态农业有限公司'
    menu_style='accordion'
xadmin.site.register(views.CommAdminView,GlobalSettins)