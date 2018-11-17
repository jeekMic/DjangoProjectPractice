from django.db import models

# 设计和表对应的类

# books class
class BookInfoManager(models.Manager):
    # 1 change the query of aggregate
    def all(self):
        books = super().all() # QuerySet
        books = books.filter(isDelete=False)
        # 返回数据
        return books
    def fz(self):
        # 这里可以封装经常使用的模型操作
        pass
    def create_book(self, btitle, bpub_date):
        book = BookInfo()
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()
        return book





class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    # 日期类
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.btitle
    objects = BookInfoManager()
    # 元选项
    # class Meta:
    #     db_table = "bookinfo"

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hbook_id = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    hcomment = models.CharField(max_length=200)
    # 英雄的描述
    hcontent = models.CharField(max_length=500)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.hname


class NewsType(models.Model):
    # 类型名
    type_name = models.CharField(max_length=20)
    types_news = models.ManyToManyField('NewsInfo')

class NewsInfo(models.Model):
    title = models.CharField(max_length=128)
    # 发布时间
    bpub_date = models.DateTimeField(auto_now_add=True)
    # 信息内容
    content = models.TextField()
    # 关系属性
    news_type = models.ManyToManyField('NewsType')

#员工的基本信息
class EmployeeBasicInfo(models.Model):
    #姓名
    name = models.CharField(max_length=20)
    #性别
    gender = models.BooleanField(default=False)
    # 年龄
    age = models.IntegerField()
    #employee_detail = models.OneToOneField('EmployeeDetailInfo')


# 员工的详细信息
class EmployeeDetailInfo(models.Model):
    # 联系地址
    addr = models.CharField(max_length=256)
    # 教育经历
    # 关系属性,代表员工的基本信息
    employee_basic = models.OneToOneField('EmployeeBasicInfo', on_delete=models.CASCADE)

class  AreaInfo(models.Model):
    # the area name 添加verbose_name属性的时候，后台的标题就是这个
    atitle = models.CharField(verbose_name='标题',max_length=20)
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    # 自定义管理器对象
    # area_manager = models.Manager()

    def title(self):
        return self.atitle
    # 在类里面定义的方法都会成为列，但是要到 list_display中去写出来，才会在后台呈现
    def mytitle(self):
        return self.atitle
    def aprent(self):
        try:
            return self.aParent.atitle
        except :
            print("出现错误")
            return "中国"

    title.admin_order_field = 'atitle'
    title.short_description = "地区名称"
    aprent.short_description = "上一级城市"

class PicTest(models.Model):
    # 上传图片
    goods_pic = models.ImageField(upload_to='booktest')

