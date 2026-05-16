# Analysis-Of-Scrapped-Data-From-Steam

A senior capstone project developed for **ECT 437** and **ECT 438** under the instruction of Jeff Kinne.

This project focuses on collecting, organizing, and analyzing data scraped from the Steam gaming platform using Python, Django, and web scraping technologies. The application stores game-related data in a database and presents the information through a web interface for analysis and visualization.

## Repository

[https://github.com/ahicks217/Analysis-Of-Scrapped-Data-From-Steam](https://github.com/ahicks217/Analysis-Of-Scrapped-Data-From-Steam)

---

# Project Overview
The purpose of this capstone project is to demonstrate the process of:
* Web scraping live gaming data from Steam
* Cleaning and organizing collected datasets
* Storing data in a relational database
* Building a Django web application for displaying and analyzing results
* Exploring trends and statistics within Steam game data

The project combines concepts from:
* Data Collection
* Data Processing
* Database Management
* Web Development
* Data Analysis
* Software Engineering

Steam is one of the largest digital gaming platforms in the world, making it a strong source for real-world data analysis projects. Similar Steam data scraping and analytics projects are commonly used in data engineering and analytics portfolios.

---

# Technologies Used

## Backend
* Python 3
* Django
* SQLite3

## Web Scraping & Data Processing
* BeautifulSoup4
* Requests
* CSV Processing
* Steam API

## Frontend
* HTML5
* CSS3
* JavaScript

## Development Tools
* Visual Studio Code
* Git & GitHub

---

# Features
* Scrapes Steam game data from online sources
* Stores scraped data in a local database
* Displays game information through Django templates
* Uses CSV datasets for additional processing
* Includes migration support through Django ORM
* Organized MVC-style project architecture
* Provides reusable scraping scripts for future expansion

---

# Data Collected
The scraper and API tools collect information such as:
* Game titles
* Steam App IDs
* Ratings and reviews
* Popularity rankings
* Game metadata
* Store information
The project demonstrates how scraped datasets can be transformed into structured and searchable information for analysis purposes.

---

# Installation & Setup
## 1. Clone the Repository
```
git clone https://github.com/ahicks217/Analysis-Of-Scrapped-Data-From-Steam.git
cd Analysis-Of-Scrapped-Data-From-Steam
```

## 2. Create a Virtual Environment
### Windows
```
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux
```
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies
```
ip install -r requirements.txt
```

If no requirements file exists yet, install manually:
```
pip install django beautifulsoup4 requests
```

---

## 4. Run Database Migrations
```
python manage.py migrate
```

---

## 5. Start the Development Server
```
python manage.py runserver
```
Then open:
```
http://127.0.0.1:8000/
```

---

# Running the Scraper
Navigate to the scraper directory and execute the desired script.
Example:
```
python scraper.py
```
or
```
python steamapi.py
```
The generated CSV files can then be imported into the Django database for analysis.

---

# Educational Objectives
This project was created to fulfill the requirements of:
* ECT 437
* ECT 438

The capstone demonstrates practical application of:
* Full-stack web development
* Database integration
* Data scraping techniques
* Data organization and visualization
* Software project planning and documentation

---

# Future Improvements
Potential future enhancements include:
* Interactive data visualizations
* Machine learning analysis of Steam trends
* User authentication system
* REST API integration
* Automated scheduled scraping
* Cloud deployment
* Advanced filtering and search tools

---

# Research & Inspiration
This project was inspired by various public Steam analytics and scraping projects that demonstrate real-world data engineering and analytics workflows.

---

# Authors
* **Alex Hicks**
* **Mahad Osman**
* **Aseel Ibrahim**
### Senior Capstone Project
### ECT 437 & ECT 438

Student GitHub:
[https://git.indstate.edu/ahicks39](https://git.indstate.edu/ahicks39)
