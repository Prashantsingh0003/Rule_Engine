DB_USERNAME = 'root'  # Replace with your MySQL username
DB_PASSWORD = 'ROOT'  # Replace with your MySQL password
DB_HOST = 'localhost'
DB_PORT = 3306
DB_NAME = 'rule_engine_db'

SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
