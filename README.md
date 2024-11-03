Pharm Chat
Pharm Chat is a real-time messaging platform designed to facilitate seamless communication between patients and pharmacists. With features like AJAX polling for instant message updates and comprehensive testing, this application enhances the quality of pharmaceutical care.

Features
Real-Time Messaging: Utilizes AJAX for efficient polling, ensuring instant updates without page refreshes.
Patient and Pharmacist Interaction: Patients can easily send inquiries about medications, while pharmacists can respond promptly.
Django Unit Tests: Includes comprehensive unit tests to ensure code quality and reliability.
CI/CD Integration: Streamlined deployment process for continuous integration and delivery.
Technologies Used
Django
AJAX
HTML/CSS/JavaScript
GitHub Actions (for CI/CD)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/pharm-chat.git
cd pharm-app
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
Running Tests
To run the unit tests, use the following command:

bash
Copy code
python manage.py test
Usage
Access the application at http://127.0.0.1:8000/.
Patients can create an account or log in to start messaging pharmacists for inquiries.
Contributing
Contributions are welcome! Please open an issue or submit a pull request to help enhance the project.
