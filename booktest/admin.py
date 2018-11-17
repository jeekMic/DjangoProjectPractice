from django.contrib import admin
from booktest.models import BookInfo, HeroInfo, AreaInfo,PicTest


# Register your models here.


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class BookInfoAdmin(admin.ModelAdmin):
    '''图书模型管理类'''
    list_display = ['id', 'btitle', 'bpub_date']

class HeroInfoAdmin(admin.ModelAdmin):
    '''Heroic figure manage class '''
    list_display = ['id', 'hname', 'hcomment']
# 关联对象
class AraeStackedInline(admin.StackedInline):
    model = AreaInfo
    extra = 3
class AraeTabularInline(admin.TabularInline):
    model = AreaInfo
    extra = 3
class AreaInfoAdmin(admin.ModelAdmin):
    list_per_page = 10 #每页指定10个
    list_display = ['id','atitle','title', 'aprent']
    actions_on_bottom = True
    list_filter = ['id','atitle'] # 列表页右侧过滤栏
    search_fields = ['id','atitle']
    # fields = ['aParent', 'atitle'] 详细页里面的选项
    # 对详细页面里面的字段进行分类，有些事高级属性，有些事一般属性
    fieldsets =(
        ('基本',{'fields':['atitle']}),
        ('高级',{'fields':['aParent']})
    )
    # inlines = [AraeStackedInline]
    inlines = [AraeTabularInline]


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
admin.site.register(AreaInfo,AreaInfoAdmin)
admin.site.register(PicTest)
