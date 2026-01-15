# 📝 Task Tracker App (Django)

A simple and user-friendly **Task Tracker web application** built using **Django**.  
This project helps users manage their daily tasks efficiently with authentication support.

---

## 🚀 Features

- User Registration & Login
- Create, View, Update, and Delete Tasks
- User-specific task management
- Clean UI with HTML & CSS
- Secure authentication system
- Django Admin panel support

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS
- **Database:** SQLite (default Django DB)
- **Tools:** Git, GitHub, VS Code

---

## 📂 Project Structure

```text
Task_Tracker_App/
│
├── core/                # Main Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tasks/               # Task management app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
├── manage.py
├── requirements.txt
└── .gitignore


⚙️ Installation & Setup

Follow these steps to run the project locally:

1️⃣ Clone the Repository
git clone https://github.com/Arvind-sta/Task_Tracker_App.git
cd Task_Tracker_App

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py migrate

5️⃣ Start the Server
python manage.py runserver


Open browser and visit:

http://127.0.0.1:8000/

👤 Usage

Register a new user

Login with your credentials

Add tasks

Update or delete tasks

Manage tasks easily from your dashboard

🔮 Future Improvements

Task priority levels

Due dates & reminders

REST API integration

Deployment on cloud (Render / Railway)

Improved UI with Bootstrap or React

🤝 Contributing

Contributions are welcome!
Feel free to fork the repository and submit a pull request.

👨‍💻 Author

Arvind Prajapati

GitHub: Arvind-sta

Aspiring Data Scientist & Backend Developer
