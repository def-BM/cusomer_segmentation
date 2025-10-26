import pymongo
from passlib.context import CryptContext

# --- Database Connection ---
MONGO_URI = "mongodb://localhost:27017/"
client = pymongo.MongoClient(MONGO_URI)

# Use the database and collection you specified
db = client["customerDB"]
collection = db["users"]

# --- Password Hashing ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    # Verifies a plain password against a hashed one.
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    # Hashes a password.
    return pwd_context.hash(password)

# --- User Functions ---
def user_exists(username):
    # Check if a user already exists in the database.
    if collection.find_one({"username": username}):
        return True
    return False

def add_user(username, password):
    # Adds a new user to the database with a hashed password.
    if user_exists(username):
        return False  # User already exists
    hashed_password = get_password_hash(password)
    collection.insert_one({"username": username, "password": hashed_password})
    return True

def check_credentials(username, password):
    # Checks if the username exists and the password is correct.
    user = collection.find_one({"username": username})
    if user and verify_password(password, user["password"]):
        return True
    return False