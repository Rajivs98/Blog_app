Blog Application

Overview
This project is a simple blog application built with Django and Django REST Framework. It provides basic CRUD functionalities for blog posts and comments and includes user authentication using JWT.


Requirements

Python 3.8 or above
Django 5.0 or above
Django REST Framework 3.0 or above
djangorestframework-simplejwt 5.1.0 or above
psycopg2 2.9.1 or above
PostgreSQL 


Installation

Clone the repository:

git clone https://github.com/Rajivs98/Blog_app.git

cd blog_test_project
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the dependencies:


pip install -r requirements.txt
Configure the database:

Update the DATABASES setting in settings.py with your PostgreSQL configuration.


Endpoint of API's ------------------------------------------>

1. For Register User : 

http://127.0.0.1:8000/register   use method POST
example of body - 
{
    "username": "usrename",
    "password": "password",
    "email": "abc@mail.com",
    "first_name": "check",
    "last_name": "ex"
}

2. Login User :
http://127.0.0.1:8000/Login
{
  "username": "username",
  "password": "password"
}

After login use access token for further API

3. Create Post

http://127.0.0.1:8000/posts/ 

{
  "title": "Books",
  "content": "History of Bihar",
  "author":"RR",
  "published_date": "27-07-2024"
}

4. Get and List all Post 

http://127.0.0.1:8000/list_post/


5. For retrieve specific post 

http://127.0.0.1:8000/posts/<id>/ 

6. for Update a specific post
http://127.0.0.1:8000/posts/<id>/  

{
  "title": "Glass",
  "content": "heavy"
}

7. For post Comment 

http://127.0.0.1:8000/posts/1/comments/

{
  "text": "Hi, how are u ?"
}

8. for delete post

http://127.0.0.1:8000/del_post/2/
