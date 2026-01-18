# 📚 Learning Log

### A Personal Knowledge Management System

**Learning Log** is a web application that allows users to track their learning progress. It serves as a digital journal where users can create topics (e.g., "Python", "Chess", "Cooking") and log daily entries or notes under each topic. It is built to demonstrate core **CRUD (Create, Read, Update, Delete)** functionalities and secure user management.

---

## 🚀 Key Features

* **🔐 User Authentication:** Secure signup, login, and logout functionality using Django's built-in authentication system.
* **📂 Topic Management:** Users can create new learning topics to organize their entries.
* **📝 Full CRUD Support:**
    * **Create:** Add new entries to specific topics.
    * **Read:** View a list of all topics and individual entries.
    * **Update:** Edit existing entries to correct or add information.
    * **Delete:** Remove topics or entries when they are no longer needed.
* **🛡️ Data Privacy:** A user can only access and edit their own data. Usage of `@login_required` decorators ensures unprotected views are not accessible.
* **🎨 Responsive Design:** Styled using **Bootstrap** for a clean and mobile-friendly interface.

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** Django Templates, Bootstrap 5
* **Database:** SQLite (Default)
* **Version Control:** Git

## ⚙️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/sakshiot4/learning-log.git](https://github.com/yourusername/learning-log.git)
    cd learning-log
    ```

2.  **Create virtual environment:**
    ```bash
    python -m venv venv
    # Activate:
    # Windows: venv\Scripts\activate
    # Mac/Linux: source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Migrate Database:**
    ```bash
    python manage.py migrate
    ```

5.  **Run Server:**
    ```bash
    python manage.py runserver
    ```

6.  **Access the app:**
    Go to `http://localhost:8000/`

## 🔮 Future Improvements

* Add a search bar to filter topics.
* Implement a "Public vs Private" toggle for sharing topics.
* Add Markdown support for rich text in entries.
