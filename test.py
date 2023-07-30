from fastapi.testclient import TestClient
from pymongo import MongoClient
from bson import ObjectId
import pytest
from main import app


client = TestClient(app)
mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client['courses']


def test_get_courses_no_params():
    response = client.get("/courses")
    assert response.status_code == 200