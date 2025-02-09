import yaml
import mysql.connector
import pandas as pd

# Đọc file config.yaml
def load_config(file_path="D:\\E-commerce-ETL\\config.yaml"):
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

# Kết nối đến MySQL
def connect_to_mysql():
    try:
        config = load_config()  # Load cấu hình từ file YAML
        db_config = config["database"]

        # Khởi tạo kết nối
        connection = mysql.connector.connect(
            host=db_config["host"],
            port=db_config["port"],
            user=db_config["user"],
            password=db_config["password"],
            database=db_config["database"],
            # charset=db_config["charset"]
            allow_local_infile=True
        )

        if connection.is_connected():
            print("Kết nối thành công đến MySQL!")
            return connection
            
    except mysql.connector.Error as err:
        print(f"Lỗi kết nối: {err}")
        return None

# Hàm đọc file .sql và thực thi
def execute_sql_file(connection, file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            sql_script = file.read()  # Đọc toàn bộ nội dung file .sql

        cursor = connection.cursor()
        for statement in sql_script.split(";"):  # Tách các câu lệnh SQL dựa trên dấu ;
            if statement.strip():  # Bỏ qua các dòng trống
                cursor.execute(statement)
        
        connection.commit()  # Lưu thay đổi vào database
        cursor.close()
        print("Đã thực thi file SQL thành công!")
    
    except mysql.connector.Error as err:
        print(f"Lỗi khi thực thi SQL: {err}")

# Hàm main
def main():
    path_creat_table_sql = "D:\\E-commerce-ETL\\load_dataset_into_mysql\\creat_table.sql"
    path_load_data_sql = "D:\\E-commerce-ETL\\load_dataset_into_mysql\\load_data.sql"
    conn = connect_to_mysql()

    execute_sql_file(conn, path_creat_table_sql)
    execute_sql_file(conn, path_load_data_sql)

    if conn:
        conn.close()
        print("🔌 Đã đóng kết nối.")

# Chạy chương trình
if __name__ == "__main__":
    main()

