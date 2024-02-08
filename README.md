# Book Recommendation App

This Django application provides book recommendations for users based on their favorite books or books they have downloaded.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Service Package](#service-package)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication:** Users can register, log in, and manage their profiles.
- **Book Management:** Admins can add, edit, and delete books with information like title, author, category, and download link.
- **Recommendation System:** Users receive book recommendations based on their favorite books or downloaded books.
- **Custom Exceptions:** Handle exceptions such as Internal Server Error, Bad Request, Not Authorized, Resource Not Found, and Too Many Requests.

## Project Structure

ai_recommendation/
|-- ai_recommendation/ # Django project directory
| |-- settings.py
| |-- ...
|-- service/ # Separate package for recommendation logic
| |-- models.py
| |-- ...
|-- requirements.txt
|-- manage.py
|-- ...

perl
Copy code

## Getting Started

To get started with the Book Recommendation App, follow the steps below.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/ai-recommendation.git
    ```

2. Change into the project directory:

    ```bash
    cd ai-recommendation
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Migrate the database:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

2. Create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

3. Run the development server:

    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```

4. Access the admin panel at `http://127.0.0.1:8000/admin/` to manage books.

## Service Package

The recommendation logic is implemented in a separate service package (`service_package/recommendation_service.py`). This package handles the recommendation system's logic to provide users with book recommendations based on their preferences.
