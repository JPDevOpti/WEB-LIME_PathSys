from motor.motor_asyncio import AsyncIOMotorClient
from app.config.settings import settings

class DatabaseManager:
    client: AsyncIOMotorClient = None
    database = None

database_manager = DatabaseManager()

async def connect_to_mongo():
    """Create database connection"""
    database_manager.client = AsyncIOMotorClient(settings.MONGODB_URL)
    database_manager.database = database_manager.client[settings.DATABASE_NAME]

async def close_mongo_connection():
    """Close database connection"""
    database_manager.client.close()

def get_database():
    return database_manager.database
