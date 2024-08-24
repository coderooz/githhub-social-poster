from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
filter={
    'private': False, 
    'license.key': 'mit', 
    'visibility': 'public',
    'id': 831599172
}

result = client['github']['repositories'].find(filter=filter).limit(1)
print(list(result))