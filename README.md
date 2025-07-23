# url-shortner
A personalized URL shortener app that allows users to create custom short links, track click analytics, and manage their URLs securely through a user-friendly dashboard. Built with Django and styled using Tailwind CSS, it ensures each shortened URL is unique and tied to the authenticated user.


# 🔗 Custom URL Shortener with Analytics

A personalized URL shortener built with Django that allows users to register, log in, create custom short links, and track the number of clicks. Each user can manage their own set of shortened URLs through a secure and intuitive interface.

## 🌟 Features

- 🔒 User Registration & Authentication  
- ✏️ Custom Short URL Input  
- 📊 Click Analytics per URL  
- 🧾 User Dashboard with URL History  
- ✅ Unique short code validation  
- 💻 Clean, responsive UI using Tailwind CSS

## 🧠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, Tailwind CSS
- **Database:** SQLite (default, can be changed to Postgres/MySQL)
- **Authentication:** Django’s built-in user system

## 📂 Project Structure

urlshortener_project/
├── shortener/ # Core Django app
│ ├── models.py # URL model with click tracking
│ ├── views.py # Handles creation, redirects, and analytics
│ ├── forms.py # Forms for custom input
│ ├── templates/ # HTML templates
│ └── urls.py # App-level routes
├── urlshortner_project/ # Main Django project
│ └── settings.py # Configurations
└── manage.py # Django entry point

bash
Copy
Edit

## 🚀 How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/url-shortener.git
   cd url-shortener
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # For Linux/macOS
.venv\Scripts\activate     # For Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations:

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Run the development server:

bash
Copy
Edit
python manage.py runserver
Access the app:

Open your browser and visit: http://127.0.0.1:8000

🧪 Testing the App
Register a new user.

Create a short URL by providing a custom code.

Visit the shortened link to trigger click tracking.

View your dashboard to see how many times each URL was clicked.

✅ Success Criteria
Each user sees only their own URLs.

Short codes are unique per user.

Click analytics are accurate and update on each redirect.




I'm happy to help!
