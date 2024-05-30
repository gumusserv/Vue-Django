import mysql.connector
from collections import Counter

# 数据库连接配置
config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'moviedb'
}

# 连接到数据库
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# 查询所有记录的genre
select_query = "SELECT genre FROM movies_movie"

try:
    # 执行查询
    cursor.execute(select_query)
    records = cursor.fetchall()
    
    # 统计题材的数量
    genre_counter = Counter()
    
    for (genre,) in records:
        genres = genre.split(',')
        genre_counter.update(genres)
    
    # 打印题材统计结果
    for genre, count in genre_counter.items():
        print(f"{genre}: {count}")
    
    print("Genre counting completed.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # 关闭游标和连接
    cursor.close()
    conn.close()
