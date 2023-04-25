from django.db import models

# Create your models here.

"""
1. 我们的模型类 需要继承自 models.Model
2. 系统会自动为我们添加一个主键 id
3. 字段
    字段名=models.类型（选项）
    字段名就是数据表的字段名
    字段名不要使用python，mysql的关键字
    char(m) varchar(m) 中的m就是选项
"""
class BookInfo(models.Model):
    #id
    name=models.CharField(max_length=20)
    # 重写 str方法让admin来现实书记的名字
    def __str__(self):
        return self.name

#人物 后期讲原理
class PeopleInfo(models.Model):
    name=models.CharField(max_length=20)
    gender=models.BooleanField()
    #外键约束：人物属于哪本书
    book=models.ForeignKey(BookInfo, on_delete=models.CASCADE)


