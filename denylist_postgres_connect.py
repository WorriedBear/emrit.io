import psycopg2

conn = psycopg2.connect(
   database="emrit_dwh", user='kaustubh', password='m2BFViFMCCFggFW', host='85.10.210.10', port= '5432'
)
cursor = conn.cursor()

cursor.execute("select version()")

data = cursor.fetchone()
print("Connection established to: ",data)

conn.close()