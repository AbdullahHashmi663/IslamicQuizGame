# Islamic Quiz Application

A comprehensive Django-based web application designed to test and enhance knowledge of Islamic teachings, history, and practices. This interactive quiz platform offers a rich collection of multiple-choice questions covering various aspects of Islam, from basic concepts to advanced topics.

## Overview

The Islamic Quiz Application serves as an educational tool that helps users:
- Test their knowledge of Islamic teachings
- Learn about Islamic history and practices
- Track their progress through quiz attempts
- Access detailed solutions and explanations
- Administer and manage quiz content

## Key Features

### For Users
- **Interactive Quizzes**: Multiple-choice questions covering various Islamic topics
- **Progress Tracking**: Record of quiz attempts and scores
- **Instant Feedback**: Immediate scoring and result analysis
- **Solution Generation**: Access to detailed solutions in document format
- **User-Friendly Interface**: Clean and intuitive design for easy navigation

### For Administrators
- **Content Management**: Easy addition and modification of quiz questions
- **User Management**: Track user attempts and performance
- **Customization**: Create different quiz categories and difficulty levels
- **Analytics**: Monitor quiz participation and performance metrics

## Technical Features

- **Django Framework**: Built on Django for robust web application development
- **Database Integration**: Efficient storage and retrieval of quiz data
- **Document Generation**: Automated creation of quiz solutions in Word format
- **Responsive Design**: Works seamlessly across different devices
- **Admin Dashboard**: Comprehensive backend for content management

## Topics Covered

The quiz questions cover a wide range of Islamic topics including:
- Islamic History
- Quranic Knowledge
- Hadith Studies
- Islamic Jurisprudence (Fiqh)
- Islamic Ethics and Morality
- Prophetic Traditions
- Islamic Culture and Civilization
- Contemporary Islamic Issues

## Target Audience

- Students of Islamic studies
- General public interested in learning about Islam
- Islamic educational institutions
- Community centers and mosques
- Self-learners seeking to test their knowledge

## Educational Value

This application serves as an effective tool for:
- Self-assessment of Islamic knowledge
- Educational institutions for testing and evaluation
- Community learning and engagement
- Continuous learning and improvement
- Documentation of Islamic knowledge

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AbdullahHashmi663/IslamicQuizGame.git
cd IslamicQuizGame
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Usage

1. Access the admin interface at `http://localhost:8000/admin` to manage quizzes
2. Visit `http://localhost:8000` to take quizzes
3. Generate quiz solutions document:
```bash
python create_quiz_solutions.py
```

## Deployment

### Automatic Deployment with GitHub Actions

This project is configured for automatic deployment using GitHub Actions. To set up deployment:

1. Fork this repository to your GitHub account

2. Set up PythonAnywhere:
   - Create an account at [PythonAnywhere](https://www.pythonanywhere.com)
   - Create a new web app
   - Get your API token from the Account page

3. Add these secrets to your GitHub repository:
   - Go to Settings > Secrets and variables > Actions
   - Add the following secrets:
     - `PYTHONANYWHERE_DOMAIN`: Your PythonAnywhere domain
     - `PYTHONANYWHERE_USERNAME`: Your PythonAnywhere username
     - `PYTHONANYWHERE_API_TOKEN`: Your PythonAnywhere API token

4. Push to the main branch to trigger deployment:
```bash
git push origin main
```

The GitHub Action will automatically:
- Install dependencies
- Run tests
- Deploy to PythonAnywhere
- Reload the web app

### Manual Deployment

If you prefer to deploy manually:

1. Set up a PythonAnywhere account
2. Clone the repository
3. Set up a virtual environment
4. Install dependencies
5. Configure the web app
6. Run migrations
7. Collect static files
8. Reload the web app

## Project Structure

- `quiz_app/` - Main Django application
  - `models.py` - Database models
  - `views.py` - View functions
  - `management/commands/` - Custom management commands
- `create_quiz_solutions.py` - Script to generate quiz solutions document
- `requirements.txt` - Project dependencies
- `.github/workflows/` - GitHub Actions configuration

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any questions or suggestions, please feel free to open an issue in the repository. 