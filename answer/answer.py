import os

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'day68_homework.settings')

    import django

    django.setup()

    from app01 import models

    from django.db.models import Avg, Sum, Max, Min, Count

    # 查找所有书名中包含金老板的书
    # ret = models.Book.objects.filter(title__contains='金老板').values('id', 'title')
    # print(ret)

    # 查找出版日期是2018年的书
    # ret = models.Book.objects.filter(publish_date__year=2018).values('id', 'title')
    # print(ret)

    # 查找出版日期是2017年的书名
    # ret = models.Book.objects.filter(publish_date__year=2017).values('id', 'title')
    # print(ret)

    # 查找价格大于10元的书
    # ret = models.Book.objects.filter(price__gt=10).values('id', 'title')
    # print(ret)

    # 查找价格大于10元的书名和价格
    # ret = models.Book.objects.filter(price__gt=10).values('title', 'price')
    # print(ret)

    # 查找memo字段是空的书
    # ret = models.Book.objects.filter(memo__isnull=False).values('id', 'title')
    # print(ret)

    # 查找在北京的出版社
    # ret = models.Publisher.objects.filter(city__contains='北京').values('id', 'name')
    # print(ret)

    # 查找名字以沙河开头的出版社
    # ret = models.Publisher.objects.filter(name__startswith='沙河').values('id', 'name')
    # print(ret)

    # 查找“沙河出版社”出版的所有书籍
    # 解法一:
    # ret = models.Book.objects.filter(publisher__name='沙河出版社')
    # print(ret)
    # 解法二:
    # ret = models.Book.objects.filter(publisher_id=1)
    # print(ret)

    # 查找每个出版社出版价格最高的书籍价格
    # ret = models.Publisher.objects.annotate(max_price = Max('book__price')).values()
    # print(ret)

    # 查找每个出版社的书名以及出的书籍数量
    # publisher_obj = models.Publisher.objects.annotate(count_book = Count('book__id')).values('id', 'name', 'count_book')
    # for i in publisher_obj:
    #     ret = models.Book.objects.filter(publisher__id=i['id'])
    #     i['books'] = ret
    #     print(i)

    # 查找作者名字里面带“小”字的作者
    # ret = models.Author.objects.filter(name__contains='小')
    # print(ret)

    # 查找年龄大于30岁的作者
    # ret = models.Author.objects.filter(age__gt=30)
    # print(ret)

    # 查找手机号是155开头的作者
    # ret = models.Author.objects.filter(phone__startswith=155)
    # print(ret)

    # 查找手机号是155开头的作者的姓名和年龄
    # ret = models.Author.objects.filter(phone__startswith=155).values('name', 'age')
    # print(ret)

    # 查找每个作者写的价格最高的书籍价格
    # ret = models.Author.objects.annotate(max_price=Max('book__price')).values('id', 'name', 'max_price')
    # print(ret)

    # 查找每个作者的姓名以及出的书籍数量
    # ret = models.Author.objects.annotate(book_count=Count('book')).values('id', 'name', 'book_count')
    # print(ret)

    # 查找书名是“跟金老板学开车”的书的出版社
    # book_obj = models.Book.objects.filter(title__contains='跟金老板学开车').values('id', 'title', 'publisher_id')
    # for i in book_obj:
    #     ret = models.Publisher.objects.filter(id=i['publisher_id']).values('id', 'name')
    #     print(ret)

    # 查找书名是“跟金老板学开车”的书的出版社所在的城市
    # book_obj = models.Book.objects.filter(title__contains='跟金老板学开车').values('id', 'title', 'publisher_id')
    # for i in book_obj:
    #     ret = models.Publisher.objects.filter(id=i['publisher_id']).values('id', 'name', 'city')
    #     print(ret)

    # 查找书名是“跟金老板学开车”的书的出版社的名称
    # book_obj = models.Book.objects.filter(title__contains='跟金老板学开车').values('id', 'title', 'publisher_id')
    # for i in book_obj:
    #     ret = models.Publisher.objects.filter(id=i['publisher_id']).values('id', 'name')
    #     print(ret)

    # 查找书名是“跟金老板学开车”的书的出版社出版的其他书籍的名字和价格
    # publisher_obj = models.Book.objects.filter(title__contains='跟金老板学开车').values('publisher_id')
    # for i in publisher_obj:
    #     ret = models.Book.objects.filter(publisher_id=i['publisher_id']).values('title', 'price')
    #     print(ret)

    # 查找书名是“跟金老板学开车”的书的所有作者
    # author_obj = models.Book.objects.filter(title__contains='跟金老板学开车').values('author')
    # for i in author_obj:
    #     ret = models.Author.objects.filter(id=i['author']).values('id', 'name')
    #     print(ret)

    # 查找书名是“跟金老板学开车”的书的作者的年龄
    # author_obj = models.Book.objects.filter(title__contains='跟金老板学开车').values('author')
    # for i in author_obj:
    #     ret = models.Author.objects.filter(id=i['author']).values('id', 'name', 'age')
    #     print(ret)

    # 查找书名是“跟金老板学开车”的书的作者的手机号码
    # author_obj = models.Book.objects.filter(title__contains='跟金老板学开车').values('author')
    # for i in author_obj:
    #     ret = models.Author.objects.filter(id=i['author']).values('id', 'name', 'phone')
    #     print(ret)

    # 查找书名是“跟金老板学开车”的书的作者们的姓名以及出版的所有书籍名称和价钱
    # author_obj = models.Book.objects.filter(title__contains='跟金老板学开车').values('author', 'publisher_id', 'price')
    # print(author_obj)
    # for i in author_obj:
    #     ret = models.Author.objects.filter(id=i['author']).values('id', 'name', 'phone')
    #     print(ret)