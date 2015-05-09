from pymongo import MongoClient

client = MongoClient()
# getting database "log_db"
db = client.log_db
# getting collection "log_items"
log_items = db.log_items
 
def process_asterisk(log_item):
    log_items.insert(log_item)
