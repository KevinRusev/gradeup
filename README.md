# 🎓 GradeUp - School Recommendation System
![GradeUp](https://github.com/user-attachments/assets/2447bd21-24f3-4cc3-8c58-62c0bae53cbe)


A web application that helps students find the perfect educational institution based on their preferences and needs.

---
# 📑 Table of Contents



>- [🎓 GradeUp - School Recommendation System](#-gradeup---school-recommendation-system)
>- [📸 Preview](#-preview)
>- [🛠️ Contributors](#-contributors)
>- [🚀 Features](#-features)
>- [🔧 Configuration Options](#-configuration-options)
>- [🚀 AI Module Integration (Quick Summary)](#-ai-module-integration-quick-summary)
>- [🖼 System Flowchart](#-system-flowchart)
>- [🛠️ Installation](#-installation)
>- [🧩 Entity Relationship Diagram (ERD)](#-entity-relationship-diagram-erd)
>- [🧩 Class Diagram](#-class-diagram)
>- [🧩 Use Case Diagram](#-use-case-diagram)
>- [💻 Technology Stack](#-technology-stack)
---

## 📸 Preview

>Take a quick look at **Grade Up** in action:

<table>
  <tr>
    <td align="center">
      <img src="documentation/assets/home_page.png" alt="Home Screen" width="600"/>
      <br/>Home Screen
    </td>
    <td align="center">
      <img src="documentation/assets/welcome_page.png" alt="Welcome Screen" width="600"/>
      <br/>Welcome Back Page
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="documentation/assets/dashboard.png" alt="Dashboard" width="600"/>
      <br/>Dashboard
    </td>
    <td align="center">
      <img src="documentation/assets/survey.png" alt="Survey" width="600"/>
      <br/>Survey
    </td>
  </tr>
</table>

---
## 🛠️ Contributors

### Backend 👨‍💻
> [KRRusev21](https://github.com/KRRusev21) |
> [TPIvanov21](https://github.com/TPIvanov21)

### Designers 🎨
> [PSDineva21](https://github.com/PSDineva21) |
> [GYFilipov21](https://github.com/GYFilipov21)

### Scrum Master 🧑‍🏫
> [SGMikov21](https://github.com/SGMikov21)
---
## 🚀 Features

- 🔐User authentication (registration, login, profile management)  
- 🎓Student dashboard with personalized recommendations  
- 🛠️ Admin panel for user and system management  
- 🏫 School and program browsing  
- ⭐ Favorites system to save and compare schools
>You can view the full list of user stories [HERE](documentation/UserStories_GradeUp.docx).
---
## 🔧 Configuration Options

- **Email Verification Toggle** - You can disable email verification by setting `DISABLE_EMAIL_VERIFICATION=true` in your `.env` file
- **Recommendation Engine** - Enhanced algorithm provides personalized university and program recommendations
- **Database Configuration** - Supports both SQLite for development and SQL Server for production

---
# 🚀 AI Module Integration (Quick Summary)

- Two main modules:
  - `AdvancedPredictionSystem`: Predictions with confidence scoring.
  - `RecommendationEngine`: Program & university recommendations.

- Integrated directly into Flask backend.
- Uses SQLAlchemy models: `User`, `Program`, `School`, `SurveyResponse`, etc.

- API routes call modules:
  - `/api/predict` → `predict_with_confidence()`
  - `/api/recommend` → `recommend_programs()`

- Frontend sends survey data → Backend processes → Returns predictions → Displayed to user.

- Results stored in DB: `PredictionHistory`, `Recommendation`.

---

## 🖼 System Flowchart
<div align="center"">
<img src="https://github.com/user-attachments/assets/4e4ccd05-cf39-4808-8df5-a61c6e5af391" alt="System Flowchart" width="500"/>
</div>

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/KevinRusev/gradeup.git
   cd gradeup
   ```

2. **Create a virtual environment (Python 3.12 is recommended!):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:**  
     ```bash
     venv\Scripts\activate
     ```
   - **MacOS/Linux:**  
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**  
   Create a `.env` file and configure your environment settings.

6. **Initialize the database:**
   ```bash
   flask db upgrade
   ```

7. **Run the application:**
   ```bash
   flask run
   ```

---

## 🧩 Entity Relationship Diagram (ERD)

You can view the ERD for this project here:

>👉 [View ER Diagram For GradeUp HERE](https://lucid.app/lucidchart/61f65033-3af4-4cf8-bc17-acb81d5eca5f/view)
---
## 🧩 Class Diagram

You can view the Class Diagram for this project here:

>👉 [View Class Diagram For GradeUp HERE](https://lucid.app/lucidchart/1c0cb330-9383-4fa2-b729-de0712e22a35/view)
---
## 🧩 Use Case Diagram

You can view the Use Case Diagram for this project here:

>👉 [View Use Case Diagram For GradeUp HERE](https://lucid.app/lucidchart/8118d3f6-516f-424c-afa6-288fe6a2db89/view)
---

## 💻 Technology Stack

- **Flask** – Web framework  
- **SQLAlchemy** – ORM for database operations  
- **Flask-Login** – User session management  
- **Bootstrap** – Frontend UI framework  
- **SQL Server** – Configurable backend database

