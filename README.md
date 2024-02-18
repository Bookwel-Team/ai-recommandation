# Book Recommendation App

This Django application provides book recommendations for users based on their favorite books or books they have downloaded.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Testing](#testing)

## Features

- **User Authentication:** Users can register, log in, and manage their profiles.
- **Book Management:** Admins can add, edit, and delete books with information like title, author, category, and download link.
- **Recommendation System:** Users receive book recommendations based on their favorite books or downloaded books.
- **Custom Exceptions:** Handle exceptions such as Internal Server Error, Bad Request, Not Authorized, Resource Not Found, and Too Many Requests.


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

1. Run the development server:

    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```
   
## Endpoints

The application exposes the following endpoints:

- `/recommandation/recommandation/`: Endpoint for the `get_recommendations` logic.
- `/recommandation/pdf/`: Endpoint for the `extract_info_from_pdf` logic.

## Testing

Run the tests using the following command:

   ```bash
  python manage.py test service.tests
   ```