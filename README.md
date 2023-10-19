# TuTable - Student Management System
## Description
TuTable is a web application built using Django framework, designed for managing students in a tutoring context. This sytem allows you to monitor your 

## Features
- Add Students: Add a new students to the database, providing their id, name, telephone number and tutoring subject.
- Student Data Modification: Edit the information about the existing student and contact details.
- Student Deletion: Remove students from the database when the tutoring ends or for other reasons.
- Lesson Creation: Record details of lessons, such as date, subject and payment status.
- Lesson Editing: Update lessons informations e.g. when student pay for a lesson.

## How to Run the Project Locally
To run the application on your local machine follow these steps:

### Prerequisites
1. Make sure you have Python installed on your computer. If not, you can download it from https://python.org.
2. Ensure you have pip installed. It's typically included with Python, but you can check by running pip --version.

### Installation
1. Clone this repository to your local machine or download it as a ZIP file and extract the contents.
```bash
git clone https://github.com/jkalinowsky/TuTable.git
```
2. Navigate to the project directory:
```bash
cd TuTable
```
3. Create a virtual environment:
```bash
python -m venv venv
```
4. Activate the virtual environment:
- on Windows:
```bash
venv\Scripts\activate
```
- on macOS/Linux:
```bash
source venv\bin\activate
```
5. Install the required Python packages:
```bash
pip install -r requirements.txt
```
6. Apply the database migrations:
```bash
python manage.py migrate
```

### Running the Server
1. Start the Django development server:
```bash
python manage.py runserver
```
2. Acces the TuTable web application in your web browser at: http://127.0.0.1:8000/.
3. Begin managing your students and lessons with TuTable.
