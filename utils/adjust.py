import mysql.connector
import requests
# 数据库连接配置
# 数据库连接
conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='moviedb'
)

# # 连接到数据库
# conn = mysql.connector.connect(**config)
# cursor = conn.cursor()

# # 查询所有记录的historical_rating
# select_query = "SELECT movie_id, year FROM movies_movie"

# try:
#     # 执行查询
#     cursor.execute(select_query)
#     records = cursor.fetchall()
    
#     # 检查每条记录的评分是否在0到5之间
#     for movie_id, historical_rating in records:
#         if historical_rating < 1900 or historical_rating > 2024:
#             print(f"Movie ID {movie_id} has a year out of range: {historical_rating}")
    
#     print("Rating check completed.")
# except mysql.connector.Error as err:
#     print(f"Error: {err}")
# finally:
#     # 关闭游标和连接
#     cursor.close()
#     conn.close()

cursor = conn.cursor()

# 查询所有电影的图片URL
cursor.execute("SELECT movie_id, cover_image_url FROM movies_movie")
movies = cursor.fetchall()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
}

success_list = []
fail_list = []

for movie_id, url in movies:
    print(f"开始下载 {movie_id}")
    try:
        # 下载图片
        response = requests.get(url, headers=headers, proxies={"http": None, "https": None})
        if response.status_code == 200:
            image_data = response.content

            # 更新数据库，将图片的二进制数据存储到数据库中
            update_query = "UPDATE movies_movie SET cover_image_blob = %s WHERE movie_id = %s"
            cursor.execute(update_query, (image_data, movie_id))
            success_list.append(movie_id)
        else:
            print(f"Failed to download image for movie_id {movie_id}")
            fail_list.append(movie_id)
    except Exception as e:
        print(f"Error downloading image for movie_id {movie_id}: {e}")
        fail_list.append(movie_id)

# 提交更改并关闭连接
conn.commit()
cursor.close()
conn.close()