# CourseFinder

A content-based course recommendation system built with FastAPI, scikit-learn, and NLP. Select a course you love and discover the 5 most similar courses using TF-IDF vectorization and cosine similarity.

---

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment on Render](#deployment-on-render)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Search-based course selection with real-time filtering and keyboard navigation
- Top 5 NLP-powered recommendations ranked by cosine similarity score
- Multi-page layout: Home, Recommend, About, Contact
- Dark/light theme toggle with localStorage persistence
- Responsive monochrome design, no external UI frameworks
- Instant results via precomputed similarity matrix

---

## Demo

**Live Deployment (Render)**: [https://udemy-harshit-course-recommender.onrender.com](https://udemy-harshit-course-recommender.onrender.com)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/HARSHIT071004/Course-recommender.git
cd Course-recommender
```

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the development server:

```bash
python -m uvicorn app:app --host 127.0.0.1 --port 5000 --reload
```

Or without reload:

```bash
python -m uvicorn app:app --host 127.0.0.1 --port 5000
```

Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Deployment on Render

Ensure `requirements.txt` contains:

```
fastapi
uvicorn[standard]
jinja2
python-multipart
scikit-learn
pandas
gunicorn
```

On Render:

1. Create a New Web Service
2. Select Python 3 as environment
3. Connect your GitHub repo
4. Branch: `main`
5. Build Command: `pip install -r requirements.txt`
6. Start Command: `gunicorn app:app`
7. Deploy

---

## Tech Stack

- **FastAPI** — async Python web framework
- **uvicorn** — ASGI server
- **scikit-learn** — TfidfVectorizer, cosine_similarity
- **pandas** — data loading and manipulation
- **Jinja2** — template rendering
- **Vanilla JS** — no framework, no build step

---

## Project Structure

```
Course-Recommender-NLP/
├── app.py                 # FastAPI routes and server entry point
├── model.py               # CourseRecommender class (TF-IDF + similarity)
├── requirements.txt       # Python dependencies
├── data/
│   └── courses.csv        # Udemy course dataset (11 columns)
├── static/
│   └── style.css          # Monochrome design system with dark/light themes
└── templates/
    ├── base.html           # Shared layout (nav, theme toggle, footer)
    ├── home.html           # Hero, features, how-it-works
    ├── recommend.html      # Search bar + recommendation grid
    ├── about.html          # Project info, tech stack, stats
    └── contact.html        # Contact form
```

---

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a Pull Request

---

By Harshit Sharma

This project is licensed under the MIT License.
