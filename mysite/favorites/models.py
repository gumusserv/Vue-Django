from django.db import models
from accounts.models import User  # 使用你自定义的用户模型
from movies.models import Movie   # 引用你的电影模型

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'movie')  # 确保用户不会重复收藏同一部电影

    def __str__(self):
        return f"{self.user.username} favorited {self.movie.title}"
