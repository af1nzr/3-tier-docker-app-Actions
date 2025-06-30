from flask import Flask
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        connection = mysql.connector.connect(
            host='db',               # 'db' is the docker-compose service name
            user='admin',
            password='password',
            database='appdb'
        )

        if connection.is_connected():
            return "✅ Connected to MySQL from Backend"

    except Error as e:
        return f"❌ Failed to connect to MySQL: {e}"

    finally:
        if connection.is_connected():
            connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
