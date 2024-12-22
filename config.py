from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Строка подключения
uri = "mongodb+srv://alexslepchenko71:i8tCti84DpTVEhcb@cluster0.4uaek.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Підключення до MongoDB
def get_client():
    client = MongoClient(uri, server_api=ServerApi('1'))
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(f"Error: {e}")
        raise
