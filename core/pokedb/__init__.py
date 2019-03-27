import pymongo


# create_poke_db creates the PokeDB in Mongo.
def create_poke_db():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['pokedb']
    client.close()

def insert_user_email(email):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['pokedb']
    users = db['email']
    # Insert the email object and close the client.
    users.insert_one(email)
    client.close()

def get_all_email():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['pokedb']
    users = db['email']
    # Insert the email object and close the client.
    user_email = []
    for email in users.find():
        user_email.append(email['Email'])
    client.close()
    return user_email