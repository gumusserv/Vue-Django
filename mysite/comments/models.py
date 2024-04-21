from django.db import models
from accounts.models import User  # 使用你自定义的用户模型
from movies.models import Movie   # 引用你的电影模型

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')
    comment = models.TextField(blank=True, null=True)  # 允许评论为空
    RATING_CHOICES = [
        (0, '0 stars'),
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES, blank=True, null=True)

    class Meta:
        unique_together = ('user', 'movie')  # 确保用户不会重复收藏同一部电影

    def __str__(self):
        return f"{self.user.username} comment {self.movie.title} with {self.comment} and rating {self.rating}"