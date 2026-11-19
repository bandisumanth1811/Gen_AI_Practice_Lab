
from fastapi import FastAPI

# Create the API application
app = FastAPI()

# Temporary student data
students = [
    {"id": 1, "name": "Rahul", "course": "Data Science"},
    {"id": 2, "name": "Priya", "course": "Computer Science"},
    {"id": 3, "name": "John", "course": "AI Engineering"}
]

# GET endpoint
@app.get("/")
def home():
    return {"message": "Welcome to Student API"}

# Get all students
@app.get("/students")
def get_students():
    return students

# Get one student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    return {"error": "Student not found"}
