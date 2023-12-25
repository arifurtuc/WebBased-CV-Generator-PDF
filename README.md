# Web-based CV Generator

This project is a simple web-based CV generator built using Django, allowing users to create and download their resumes.

## Features

- **Form Submission**: Users can submit their personal information, education, work experience, and skills through a form.
- **CV Generation**: The application generates a printable CV in PDF format based on the entered details.
- **Downloading CVs**: Users can view and download their generated CVs.
- **Admin Features:**
  - Manage profiles

## Technologies Used

- Python
- Django
- HTML
- Bootstrap
- PDFKit

## Installation

1. Clone the repository.
2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Django migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

