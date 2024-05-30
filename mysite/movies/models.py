from django.db import models

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)  # 电影名称
    duration = models.IntegerField(help_text="Duration in minutes")  # 电影时长，单位为分钟
    year = models.IntegerField()  # 上映年份
    director = models.CharField(max_length=255)  # 导演
    actors = models.TextField()  # 演员，由于可能有多个演员，使用 TextField
    genre = models.CharField(max_length=100)  # 主题或类型
    movie_link = models.URLField()  # 电影链接
    cover_image_url = models.URLField()  # 电影封面图片链接
    historical_rating = models.FloatField()  # 历史评分
    douban_id = models.CharField(max_length=100, default="无")  # 新字段，设置一个默认值
    discription = models.TextField()
    


    def __str__(self):
        return self.title

