from flask_cors import CORS
from flask import Flask, jsonify, request
from supabase import create_client, Client
import os


app = Flask(__name__)
CORS(app)

SUPABASE_URL="https://kbrlklndusmdfjwcvnsu.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImticmxrbG5kdXNtZGZqd2N2bnN1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzg2NDExNjAsImV4cCI6MjA1NDIxNzE2MH0._EURNdlChRcKURgKvpc-76TwnB0-ek6LCKIFF5Tf8F8"


supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


@app.route("/")
def home():
    return jsonify({"message": "Flask API for Capstone Database"})



# ----------------- USERS TABLE ROUTES -----------------

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    response = supabase.table("users").select("*").execute()
    return jsonify(response.data)

# Get a specific user by email
@app.route('/users/<email>', methods=['GET'])
def get_user_by_email(email):
    response = supabase.table("users").select("*").eq("email", email).execute()
    return jsonify(response.data)

# Add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json  # Get JSON data from request
    response = supabase.table("users").insert({
        "email": data["email"],
        "role": data["role"]
    }).execute()
    return jsonify(response.data)

# ----------------- COURSES TABLE ROUTES -----------------

# Get all courses
@app.route('/courses', methods=['GET'])
def get_courses():
    response = supabase.table("courses").select("*").execute()
    return jsonify(response.data)

# Get details of a specific course by course_id
@app.route('/courses/<course_id>', methods=['GET'])
def get_course_by_id(course_id):
    response = supabase.table("courses").select("*").eq("course_id", course_id).execute()
    return jsonify(response.data)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)