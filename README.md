# Assignment Wala

Assignment Wala is a website dedicated to assisting students with their assignments and engineering graphics drawings. Our mission is to provide reliable support to students who face challenges that prevent them from completing their academic tasks on time.

## Technologies Used

- **Frontend:**
  - HTML
  - CSS
  - JavaScript
  - Bootstrap

- **Backend:**
  - Django (Python)

- **Database:**
  - MySQL

## Features

- **High-Quality Assistance:** Deliver meticulously crafted assignments and precise engineering graphics drawings.
- **Support Academic Success:** Help students maintain their academic performance.
- **Reliable Service:** Be a dependable resource for students facing various challenges.
- **Confidentiality:** Ensure all personal and academic information remains secure.
- **Timely Delivery:** Deliver all assignments promptly.
- **Customized Solutions:** Tailor every assignment to meet specific requirements and guidelines.

## Installation

### Prerequisites

- Python 3.x
- Django
- MySQL

### Setup Instructions

1. **Clone the repository:**
    ```sh
    git clone https:https://github.com/Roshanhaurasia9319/Assignment-Wala.git
    cd assignment-wala
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv assign
    source assign/Scripts/Activate 
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the MySQL database:**
    - Create a MySQL database.
    - Update the `DATABASES` setting in `assignment_wala/settings.py` with your database information.

5. **Apply the database migrations:**
    ```sh
    python manage.py migrate
    ```

6. **Create a superuser (admin):**
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

8. **Open your web browser and visit:**
    ```
    http://127.0.0.1:8000/
    ```

## Usage

- **Admin Panel:** Access the admin panel at `/admin` to manage assignments, users, and other data.
- **User Interface:** Navigate through the website to explore the services offered and submit assignment requests.

## Contributing

We welcome contributions to improve Assignment Wala. If you have suggestions or want to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.


## Contact

For any inquiries or support, please contact us at:
- Email: appt79825@.com

---
