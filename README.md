# Chat Assistant with SQLite Database

## Overview
This project implements a Python-based Chat Assistant that interacts with an SQLite database to respond to user queries about employee and department information. The application uses Flask as the web framework and Waitress as the production-grade server.

---

## Features
- **Natural Language Query Support:** Users can ask questions such as:
  - "Show me all employees in the Sales department."
  - "Who is the manager of the Engineering department?"
  - "List all employees hired after 2021-01-01."
  - "What is the total salary expense for the Marketing department?"
- **Robust Error Handling:** The assistant handles invalid queries and returns meaningful error messages.
- **Database Integration:** Interacts with an SQLite database containing `Employees` and `Departments` tables.
- **Production Ready:** Uses the Waitress server for deployment.

---

## Prerequisites
Ensure you have the following installed:
- Python 3.7 or higher
- SQLite

### Libraries Required
- Flask
- Waitress

Install the required libraries using:
```bash
pip install Flask Waitress
```

---

## Project Structure
```
.
├── demodb.db        # SQLite database file
├── app.py           # Main application code
├── README.md        # Documentation file
└── requirements.txt # List of dependencies
```

---

## Database Schema
### Table: Employees
| ID | Name   | Department  | Salary | Hire_Date  |
|----|--------|-------------|--------|------------|
| 1  | Alice  | Sales       | 50000  | 2021-01-15 |
| 2  | Bob    | Engineering | 70000  | 2020-06-10 |
| 3  | Charlie| Marketing   | 60000  | 2022-03-20 |

### Table: Departments
| ID | Name        | Manager  |
|----|-------------|----------|
| 1  | Sales       | Alice    |
| 2  | Engineering | Bob      |
| 3  | Marketing   | Charlie  |

---

## How to Run Locally

### Step 1: Clone the Repository
```bash
git clone <your-github-repo-url>
cd <your-repo-directory>
```

### Step 2: Setup the Environment
#### Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Ensure Database is Present
Make sure the `demodb.db` file is present in the project directory. If it's missing, create it and populate it with the required tables.

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Test the Application
Access the health check endpoint:
```bash
http://127.0.0.1:8080/health
```

Use tools like **Postman** or `curl` to interact with the application:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"query": "Show me all employees in Sales"}' http://127.0.0.1:8080/chat
```

---

## Deployment
To deploy the application in a production environment:
1. Ensure the database file `demodb.db` is in the correct location.
2. Use `waitress` to run the server securely.
   ```bash
   waitress-serve --host=0.0.0.0 --port=8080 app:app
   ```

---

## Example Queries
1. **Get all employees in Sales:**
   ```json
   {
     "query": "Show me all employees in Sales"
   }
   ```

2. **Get the manager of Engineering:**
   ```json
   {
     "query": "Who is the manager of Engineering?"
   }
   ```

3. **List employees hired after a specific date:**
   ```json
   {
     "query": "List all employees hired after 2021-01-01"
   }
   ```

4. **Get the total salary expense for Marketing:**
   ```json
   {
     "query": "What is the total salary expense for Marketing?"
   }
   ```

---

## Environment Variables
- `PORT`: The port number for the application (default is `8080`).
- `HOST`: Host address (default is `127.0.0.1`).

---

## Error Handling
- Returns `400` for missing queries.
- Returns `500` for database errors.
- Gracefully handles no results found.

---

## Improvements
- Implement advanced NLP for better query understanding.
- Add more robust logging.
- Secure database queries against SQL injection.
- Enhance front-end interface.

---

## Contribution
Feel free to fork this project and submit pull requests. Suggestions and improvements are always welcome!

---

## License
This project is licensed under the MIT License.

