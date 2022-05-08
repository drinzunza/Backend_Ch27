import pymongo
import certifi


con_str = "mongodb+srv://FSDI:ThisisaSimplePassword@cluster0.4ujli.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())

db = client.get_database("OrganikaStore")