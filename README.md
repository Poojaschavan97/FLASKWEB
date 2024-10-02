# NLP Web Application with User Authentication

A comprehensive web application built using **Flask** for performing **Sentiment Analysis**, **Named Entity Recognition (NER)**, and **Text Summarization**. The app includes a user authentication system featuring **login**, **registration**, and a personalized **profile page** where users can access various NLP tasks.

## Demo
You can access the application [here](#) (Replace with deployment link if available).

## Features
- **User Authentication**:
  - **Login** and **Registration** pages.
  - Personalized **Profile Page**.
  
- **NLP Functionalities**:
  - **Sentiment Analysis**: Classifies text into positive, negative, or neutral sentiment.
  - **Named Entity Recognition (NER)**: Extracts entities such as names, organizations, and locations from the text.
  - **Summarization**: Provides a summarized version of the input text.

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **NLP**: NLPCLOUD
- **Deployment**: Gunicorn, Docker (optional for production)

## Setup

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/nlp-flask-app.git
cd nlp-flask-app
```

### 2. Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # For Windows use `venv\Scripts\activate`
```

### 3. Install the dependencies:
```bash
pip install -r requirements.txt
```

### 4. Set up the database (SQLite in this example):
```bash
flask shell
from DB import Database
dbo = Database()
dbo.create_all()
exit()
```

### 5. Run the application:
```bash
flask run
```

Access the application at `http://127.0.0.1:5000/`.

## Usage

### 1. User Authentication:
- **Registration**: New users can register on the `/register` page.
- **Login**: Existing users can log in through the `/` (home) page.

### 2. NLP Actions:
Once logged in, users are directed to their **profile page**, where they can choose between:
- **Sentiment Analysis**: Classify the sentiment of text input.
- **Named Entity Recognition (NER)**: Extract and display entities from text.
- **Summarization**: Generate a concise summary from input text.

### Example:
To perform sentiment analysis:
1. Go to the **Sentiment Analysis** page.
2. Enter your text and submit the form.
3. The result will display whether the sentiment is positive, negative, or neutral.

## Project Structure
```
nlp-flask-app/
│
├── app.py               # Main Flask application
├── DB.py                # Database handling (user authentication)
├── API.py               # External API calls for NLP tasks
├── templates/           # HTML templates
│   ├── login.html       # Login page
│   ├── registration.html # Registration page
│   ├── profile.html     # Profile page
│   ├── NER.html         # NER input page
│   ├── Sentiment.html   # Sentiment Analysis page
│   ├── summary.html     # Summarization page
├── static/              # Static files (CSS, JS)
│   ├── styles.css       # Styling for the app
├── requirements.txt     # Python dependencies
└── README.md            # Project README file
```

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](#) (Replace with GitHub issues link).

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
