import pandas as pd
import mysql.connector
import re

# 建立数据库连接
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='moviedb'
)

# 从 movie 表中读取数据
query = "SELECT * FROM movie LIMIT 18446744073709551615 OFFSET 1278"
movie_df = pd.read_sql(query, conn)

# 数据清洗和转换
def extract_duration(duration):
    try:
        # 提取持续时间中的第一个数字
        return int(re.findall(r'\d+', duration)[0])
    except:
        return 0

def extract_year(release_date):
    try:
        # 提取release_date中的年份
        year = int(release_date.split('-')[0])
        return year if year > 0 else 2000
    except:
        return 2000

# 应用转换函数
movie_df['duration'] = movie_df['duration'].apply(extract_duration)
movie_df['year'] = movie_df['release_date'].apply(extract_year)

# 处理 score 列，转换为浮点数
movie_df['historical_rating'] = pd.to_numeric(movie_df['score'], errors='coerce').fillna(0.0)

# 替换所有空值为 "无"
movie_df = movie_df.fillna("无")

# 添加默认的 movie_link 列
movie_df['movie_link'] = movie_df['douban_id'].apply(lambda x: f"https://movie.douban.com/subject/{x}")


# 选择需要的列，并重命名
movies_movie_df = movie_df[['title', 'duration', 'year', 'directors', 'actors', 'types', 'main_pic', 'historical_rating', 'movie_link', 'douban_id', 'description']]
movies_movie_df.columns = ['title', 'duration', 'year', 'director', 'actors', 'genre', 'cover_image_url', 'historical_rating', 'movie_link', 'douban_id', 'description']

# 将数据插入到 movies_movie 表中
cursor = conn.cursor()

# 插入数据
for _, row in movies_movie_df.iterrows():
    cursor.execute("""
        INSERT INTO movies_movie (title, duration, year, director, actors, genre, cover_image_url, historical_rating, movie_link, douban_id, discription)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()
