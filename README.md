Rule Engine Application for Eligibility Determination
This project is a 3-tier rule engine application designed to evaluate user eligibility based on attributes like age, department, income, spend, etc. The system uses an Abstract Syntax Tree (AST) to represent dynamic conditional rules, allowing for flexibility in rule creation, combination, and modification.

Features
Dynamic Rule Creation: Create eligibility rules based on user attributes (e.g., age, department, salary, etc.).
AST Representation: Each rule is represented as an Abstract Syntax Tree for better efficiency and dynamic modification.
Rule Combination: Multiple rules can be combined into a single tree to avoid redundant checks.
Flexible Evaluation: Evaluate user data dynamically based on the provided rules and return the eligibility status.
UI: A simple and intuitive interface for creating and evaluating rules.
Table of Contents
Project Overview
Technologies Used
System Architecture
Installation
Usage
API Endpoints
Contributing
License
Project Overview
The Rule Engine Application is a decision-making tool for determining user eligibility based on multiple attributes. The rules can be dynamically modified and combined, making the system highly adaptable for different use cases.

For example, you can define a rule like:

java
Copy code
((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)
The application processes this rule using an AST structure, making it easy to evaluate against different user profiles.

Technologies Used
Python (Backend Logic)
Flask (API Layer)
HTML/CSS/JavaScript (UI)
SQLite (Data Storage)
Git (Version Control)
System Architecture
This is a 3-tier architecture consisting of:

UI Layer: A simple frontend interface for interacting with the rule engine.
API Layer: Provides endpoints to create, combine, and evaluate rules.
Backend/Data Layer: Responsible for processing the AST and storing rule data in the database.
Installation
To get started with this project locally:

Clone the repository:

bash
Copy code
git clone https://github.com/your-username/rule-engine-app.git
Navigate to the project directory:

bash
Copy code
cd rule-engine-app
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
Open your browser and navigate to http://127.0.0.1:5000.

Usage
Rule Creation
Users can create complex eligibility rules based on conditions like age, department, salary, and more. The rules can be entered through a user-friendly interface.

Rule Evaluation
Once the rule is created, user data can be tested against the rule to determine eligibility. The system will return either True (eligible) or False (not eligible).

Example Rule
A sample rule could look like this:

java
Copy code
((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)
API Endpoints
POST /create_rule: Create a new rule and return the AST representation.
POST /combine_rules: Combine multiple rules into a single AST.
POST /check_eligibility: Evaluate a user’s attributes against the combined rule.
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/new-feature).
Make your changes.
Commit the changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature/new-feature).
Create a Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for more information.

