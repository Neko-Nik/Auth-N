# Auth-N: Custom Auth API

Auth-N is a powerful API for managing user authentication. Developed by Nikhil Raj (Alias: Neko Nik), this custom solution offers robust security features and flexible user management capabilities.

## Key Features:
- User registration, login, and logout functionalities.
- Role-based access control with support for various user roles and permissions.
- Password policy enforcement and management, including password reset and change functionalities.
- Multi-factor authentication options such as password less login and two-factor authentication (2FA).
- Enhanced security features including JWT token authentication, IP-based restriction, and CSRF protection.
- Audit logging to track user actions and system activities.
- Seamless integration with other services via API key authentication and machine-to-machine communication.

### Note: This project is currently under development and not yet ready for production use. Please check back later for updates and releases.


# How to setup the project locally

## Prerequisites

- Python 3.10 or higher (Recommended version: 3.12.0)
- Virtual Environment (venv)
- Git
- IDE (PyCharm, VSCode, etc.) [VSCode is recommended]
- Docker (Optional)

## Steps to setup and run the project

1. Clone the repository
2. Create a virtual environment: `python3.10 -m venv .venv`
3. Activate the virtual environment: `source .venv/bin/activate`
4. Install the dependencies: `pip install -r requirements.txt`
5. Create a local logs directory: `mkdir logs`
6. Change the `src/utils/base/constants.py` file according to your local setup
7. Run the application: `uvicorn api.main:app --reload --port 8086` or `gunicorn -k uvicorn.workers.UvicornWorker api.main:app`
8. Open the browser and go to `http://localhost:8086/docs` to see the OpenAPI documentation and test the APIs using Swagger UI
9. The application is now running successfully, if you face any issues, feel free to raise an issue on the GitHub repository

## Steps to run the tests

Currently, there are no tests available for the project. We are working on adding tests to the project. Stay tuned for updates.
Feel free to contribute to the project by adding tests.

# Documentation

We are working on creating detailed documentation for the project. The documentation will be available soon. Stay tuned for updates.

Refer to the TODO list for the documentation in the `docs/TODO.md` file for more information. [TODO List](https://github.com/Neko-Nik/Auth-N/blob/main/docs/TODO.md)


# 👨‍💻 Contributing:

Thank you for considering contributing to this project! Your efforts are highly valued, and they contribute to the growth and improvement of our community. Here's how you can get involved:

- **Pull Requests**: If you have changes or improvements to suggest, please submit a pull request. We'll review it promptly and merge it if it aligns with the project's standards.
  
- **Questions and Guidance**: Don't hesitate to reach out if you have any questions or need assistance with contributing. We're here to help you get started and support you throughout the process.

- **Appreciation**: We deeply appreciate all contributions made by our community members. Your dedication and effort are what make the open-source community thrive.

- **Feedback and Suggestions**: We welcome your feedback and suggestions for improving this project.

- **Security Vulnerabilities**: Read our [Security Policy](https://github.com/Neko-Nik/Auth-N/blob/main/SECURITY.md) for information on reporting security vulnerabilities.

Feel free to engage with us and join our collaborative efforts. Together, we can make this project even better!


# 🛡️ License

Auth-N is licensed under the MIT License - see the [LICENSE](https://github.com/Neko-Nik/Auth-N/blob/main/LICENSE) file for details.


# 🙏 Support

This project needs a ⭐️ from you. Don't forget to leave a star ⭐️.


# Our Pledge

We take participation in our community as a harassment-free experience for everyone and we pledge to act in ways to contribute to an open, welcoming, diverse and inclusive community.

If you have experienced or been made aware of unacceptable behaviour, please remember that you can report this. Read our [Code of Conduct](https://github.com/Neko-Nik/Auth-N/blob/main/CODE_OF_CONDUCT.md) for more information.


# Contact:

For any inquiries or feedback, please contact me at `nikhil@nekonik.com`. Shedule a meeting with me at [Calendly - Neko Nik](https://calendly.com/neko-nik/general-meet)
