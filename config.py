from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "22980696"))
API_HASH = environ.get("API_HASH", "2b653cb53821a82097efaba6732f5d75")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "7760581485:AAHQvj-pOL00FtHK7abeo20TTJ_YPbJzR0A")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "1892771262")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "-1002116310726")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://Zfile:zfile@cluster0.erkr0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
