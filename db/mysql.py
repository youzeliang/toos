import pymysql

conn = pymysql.connect(
    host="",
    user="",
    password="",
    database="",
    port=3306,
)


def insert():
    try:
        cursor = conn.cursor()
        video_url = "https://www.baidu.com"
        params = (video_url, 1)
        update_stmt = "UPDATE xxx SET video_url = %s WHERE knowledge_id = %s"
        cursor.execute(update_stmt, params)
        conn.commit()  # 提交事务
        print("Update successful.")
    except pymysql.MySQLError as e:
        print(f"Error occurred: {e}")
        conn.rollback()


