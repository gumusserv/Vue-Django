from django.db import models
from movies.models import Movie
from accounts.models import User  # 引用你自定义的用户模型

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'movie')  # 确保每个用户对同一部电影只有一条收藏记录

    def __str__(self):
        return f"{self.user.username} favorites {self.movie.title}"
