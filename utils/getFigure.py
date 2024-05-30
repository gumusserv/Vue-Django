import mysql.connector
import os
import requests

# 数据库连接配置
config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'moviedb',
    'raise_on_warnings': True
}

# 连接到数据库
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# SQL 查询语句
query = "SELECT movie_id, cover_image_url FROM movies_movie where movie_id > 4558"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
}
try:
    cursor.execute(query)
    results = cursor.fetchall()
    for (movie_id, url) in results:
        print(f"开始下载 {movie_id}")
        try:
            # 下载图片
        
            filename = f"./frontend/public/images/movie_{movie_id}.jpg"
            
            response = requests.get(url, headers=headers, proxies={"http": None, "https": None})
            if response.status_code == 200:
                image_data = response.content
                with open(filename, 'wb') as f:
                    f.write(image_data)
                print(f"Saved {filename}")


                
            else:
                print(f"Failed to download image for movie_id {movie_id}")
                
        except Exception as e:
            print(f"Error downloading image for movie_id {movie_id}: {e}")
            
        
except mysql.connector.Error as err:
    print("Error: {}".format(err))
finally:
    cursor.close()
    cnx.close()
