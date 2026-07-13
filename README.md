#  <img width="3%" alt="logobase_white" src="https://github.com/user-attachments/assets/38a2cd13-7de2-4f7c-a64d-d078a38ca10c" /> EDUKE - AI-Powered Academic Performance Prediction

EDUKE is an AI-powered academic management system that predicts student performance using attendance, academic records, quizzes, and teacher/parent feedback. The platform enables collaboration between students, teachers, parents, and administrators while providing personalized learning support through an AI chatbot.

---
<p align="center">
<img width="50% alt="logo_text_long_bg" src="https://github.com/user-attachments/assets/79656bd3-a6fa-465f-914e-aaee56c25fec" />
</p>

## ✨ Features

* 🤖 AI-powered academic performance prediction
* 💬 Personalized AI chatbot for academic guidance
* 📊 Student performance analytics and reports
* 📝 Online MCQ quizzes with instant evaluation
* 📅 Attendance and marks management
* 👨‍🏫 Teacher performance evaluation
* 👨‍👩‍👧 Parent feedback and monitoring
* 🔔 Role-based dashboards
* 💬 Built-in chat system

---

## 👥 Modules

| Module      | Features                                                      |
| ----------- | ------------------------------------------------------------- |
| **Admin**   | Manage institutions, users, classes, subjects, reports        |
| **Teacher** | Attendance, marks, quizzes, evaluations, student feedback     |
| **Student** | View attendance, marks, quizzes, AI recommendations           |
| **Parent**  | Monitor progress, provide feedback, communicate with teachers |

---

## 🛠 Tech Stack

### Backend

* Python
* Django
* Django ORM

### Database

* Neon PostgreSQL

### Frontend

* HTML5
* CSS3
* JavaScript
* Tailwind CSS

### AI & Tools

* Groq API (AI Chatbot)
* Scikit-learn (Performance Prediction)
* Git & GitHub

---

## 📷 Project Screenshots

### Dashboard
<p align="center">
<img width="60%"  alt="home" src="https://github.com/user-attachments/assets/9d4fc6a0-e863-4820-8a99-e9bc1c650705" />
</p>

### Student Dashboard

<p align="center">
<img width="60%"  alt="stud dash" src="https://github.com/user-attachments/assets/4ba90b41-4cc0-4445-93e9-7f50c538982e" />
</p>

### Teacher Dashboard

<p align="center">
<img width="60%" alt="Screenshot 2026-03-18 224256" src="https://github.com/user-attachments/assets/f322ebc5-d105-4644-8584-8f69a1241437" />
</p>

### AI Chatbot

<p align="center">
<img width="60%" alt="stud bot" src="https://github.com/user-attachments/assets/cb94d732-d1f9-41dc-b498-1ccd95347019" />
</p>

### Performance Prediction

<p align="center">
<img width="60%" alt="stud pred" src="https://github.com/user-attachments/assets/1dd761ef-0db5-4abc-b426-192ce89011dc" />
</p>


### Performance Tracking

<p align="center">
<img width="60%" alt="Screenshot 2026-03-18 224535" src="https://github.com/user-attachments/assets/946f8b95-b92a-4527-886b-55f33132a0e6" />
</p>

---

## 🚀 Installation

### Prerequisites

* Python 3.11+
* PostgreSQL / Neon Database
* Git

### Clone Repository

```bash
git clone https://github.com/yourusername/EDUKE.git
cd EDUKE
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file.

```env
SECRET_KEY=your_secret_key

DEBUG=True

DATABASE_URL=your_neon_database_url

GROQ_API_KEY=your_groq_api_key
```

### Apply Migrations

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run the Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000
```


---

## Future Improvements

* Email notifications
* Mobile application
* AI-powered study planner
* Attendance prediction
* Data visualization dashboard
* Multi-institution support

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

## 📄 License

This project is developed for educational purposes.

---

## 👨‍💻 Developer

**Abhijith C S**

* GitHub: https://github.com/theRealAbhijithCS
* Email: [abhijithcs200.com](mailto:your-abhijithcs200.com)
