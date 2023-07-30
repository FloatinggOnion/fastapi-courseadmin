import pymongo
import json


# Connect to mongodb
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["courses"]
collection = db["courses"]

# Read courses from courses.json
with open("courses.json", "r") as c:
    courses = json.load(c)

# Creating index for retrieval
collection.create_index("name")

# Adding rating field to each course
for course in courses:
    course['rating'] = {'total': 0, 'count': 0}

# Adding rating field to each chapter
for course in courses:
    for chapter in course['chapters']:
        chapter['rating'] = {'total': 0, 'count': 0}

# Adding courses to collection
collection.insert_many(courses)