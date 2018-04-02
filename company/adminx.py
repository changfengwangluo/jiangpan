import xadmin

from . import  models

#车辆
class CheliangjiluAdmin(object):
    list_display=['name','phone','chepai','chuche','yongtu','licheng','qianzi','beizhu']
    search_field=['name','phone','chepai','chuche','yongtu','licheng','qianzi','beizhu']
#公章
class GongzhangjiluAdmin(object):
    list_display=['name','phone','shiyong','beizhu']
    search_field=['name','phone','shiyong','beizhu']
#专合社
class ZhuanhesheAdmin(object):
    list_display = ['name', 'address', 'faren', 'phone']
    search_field = ['name', 'address', 'faren', 'phone']



xadmin.site.register(models.Cheliangjilu,CheliangjiluAdmin)
xadmin.site.register(models.Gongzhangjilu,GongzhangjiluAdmin)
xadmin.site.register(models.Zhuanheshe,ZhuanhesheAdmin)



