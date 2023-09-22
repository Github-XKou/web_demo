import pyodbc
import pandas as pd
from tqdm import tqdm
# 数据库连接字符串
conn_str = (
    r'DRIVER={SQL Server};'
    r'SERVER=10.2.48.77;'
    r'DATABASE=Q_Test;'
    r'UID=sa;'
    r'PWD=Msdwzdss1314'
)

try:
    conn = pyodbc.connect(conn_str)
    print("连接数据库成功!")

    # 读取CSV文件
    csv_file = 'VNet_DSC.csv'
    df = pd.read_csv(csv_file)

    # 插入数据到数据库
    cursor = conn.cursor()

    for index, row in df.iterrows():
        insert_query = "INSERT INTO YC_3D (ID,DSC,HD) VALUES (?,?,?)"
        #print(row['Name'].split('.'))
        values_to_insert = (
            row['Name'].split('.')[0],
            row['Vein'],
            row['Kidney']
            

        )

        # 执行插入操作
        cursor.execute(insert_query, values_to_insert)

    print("数据已传输!",index+1,'条数据列。')
    conn.commit()

except pyodbc.Error as ex:
    print("连接数据库失败:", ex)
