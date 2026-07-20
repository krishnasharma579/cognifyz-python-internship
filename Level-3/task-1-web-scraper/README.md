# 🌐 Web Scraper

A Python web scraper that extracts quotes, authors, and tags from the **Quotes to Scrape** website using **Requests** and **BeautifulSoup**. The scraped data is displayed in the console and saved to a CSV file.

---

## 📌 Features

- Sends an HTTP GET request to a website
- Parses HTML content using BeautifulSoup
- Extracts quotes, authors, and tags
- Displays scraped data in the console
- Saves data to a CSV file
- Handles connection and request errors gracefully
- Uses clean and structured Python code

---

## 🛠️ Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- CSV Module
- OS Module

---

## 📂 Project Structure

```
task-1-web-scraper/
│
├── main.py
├── quotes.csv
├── requirements.txt
└── README.md
```

---

## 📦 Installation

Install the required libraries:

```bash
pip install requests beautifulsoup4
```

Or install them from the requirements file:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project directory.

```bash
cd task-1-web-scraper
```

3. Run the program.

```bash
python main.py
```

---

## 💻 Example Output

```
==================================================
Quote #1
Quote : “The world as we have created it is a process of our thinking...”
Author: Albert Einstein
Tags:
- change
- deep-thoughts
- thinking
- world

==================================================
Quote #2
...
```

After execution, a **quotes.csv** file is automatically created containing all the scraped data.

---

## 📄 CSV Output

| Quote | Author | Tags |
|--------|--------|------|
| The world as we have created it... | Albert Einstein | change, deep-thoughts, thinking, world |

---

## 📖 Concepts Practiced

- Web Scraping
- HTTP Requests
- HTML Parsing
- BeautifulSoup
- File Handling (CSV)
- Exception Handling
- Loops
- String Manipulation
- OS Module

---

## 🎯 Learning Outcome

This project was developed as part of my **Python Development Internship** at **Cognifyz Technologies**. It helped me understand web scraping, HTML parsing, HTTP requests, CSV file generation, and writing clean, structured Python code.

---

⭐ Feel free to explore the project and share your feedback.