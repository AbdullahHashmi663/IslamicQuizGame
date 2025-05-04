# Islamic Quiz Application

A Django-based web application for Islamic knowledge quizzes. This application allows users to take quizzes on various Islamic topics and test their knowledge.

## Features

- Multiple choice questions on Islamic topics
- Quiz scoring system
- User attempt tracking
- Quiz solutions document generation
- Admin interface for managing quizzes

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/islamic_quiz.git
cd islamic_quiz
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

## Project Structure

- `quiz_app/` - Main Django application
  - `models.py` - Database models
  - `views.py` - View functions
  - `management/commands/` - Custom management commands
- `create_quiz_solutions.py` - Script to generate quiz solutions document
- `requirements.txt` - Project dependencies

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 