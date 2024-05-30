import pymysql

# 数据库连接参数
config = {
    'host': 'localhost',       # 例如 'localhost'
    'port': 3306,              # 标准 MySQL 端口号
    'user': 'root',   # 你的用户名
    'password': 'root',  # 你的密码
    'database': 'moviedb',     # 数据库名
    'charset': 'utf8mb4',      # 字符集
    'cursorclass': pymysql.cursors.DictCursor
}

# 创建连接
connection = pymysql.connect(**config)

try:
    # 创建 cursor
    with connection.cursor() as cursor:
        # 执行 SQL 语句，选出 movie_id > 1278 的行
        sql_select = "SELECT movie_id, historical_rating FROM movies_movie WHERE movie_id > 1278"
        cursor.execute(sql_select)
        results = cursor.fetchall()

        # 更新 historical_rating
        for row in results:
            new_rating = row['historical_rating'] / 2
            sql_update = "UPDATE movies_movie SET historical_rating = %s WHERE movie_id = %s"
            cursor.execute(sql_update, (new_rating, row['movie_id']))

        # 提交事务
        connection.commit()

finally:
    # 关闭连接
    connection.close()

print("Historical ratings updated successfully.")
