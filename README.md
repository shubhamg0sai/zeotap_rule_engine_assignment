# zeotap_rule_engine_assignment
The identified key concepts, including the rule engine, AST, 3-tier architecture, error handling, user interface, and unit tests, collectively illustrate the systematic approach of the application outlined in the document.
<hr/>

## Features of the Rule Engine with AST
1. Data Structure for AST
Node Class:
type: Indicates "operator" (AND/OR) or "operand" (condition).
left: Left child node.
right: Right child node (for operators).
value: Holds comparison values for operands.

2. Dynamic Rule Management
Create Rules: Use create_rule(rule_string) to create rules from strings.
Combine Rules: Use combine_rules(rules) to merge multiple rules into one AST efficiently.
Modify Rules: Allow changes to existing rules, including operators and operand values.

3. Evaluation of Rules
Evaluate Rule: evaluate_rule(data) checks the AST against user data, returning True or False based on conditions.

4. Error Handling
Handle errors for:
Invalid rule strings (missing operators, malformed conditions).
Incorrect data formats during evaluation.

5. Data Storage
Database: Use SQLite to store rules and metadata.
Schema:
id: Primary key.
rule_string: Original rule.
ast: Serialized AST representation.
created_at and updated_at: Timestamps for record tracking.


## Project Structure 

``` tree structure
app/
├── apirun.py             # API functions for rule engine
├── aststr.py             # AST data structure definition
├── dbCnfi.py        # Database handling
├── egrules.py           # Rule logic implementation
├── static/            # Static files (CSS, JS)
│   ├── css/
│   │   └── style.css  # UI styles
│   └── js/
│       └── script.js  # Interactive JavaScript
└── templates/         # HTML templates
    └── index.html     # Main UI

tests/
├── test_rules.py      # Unit tests for rules
└── test_api.py        # Unit tests for API

requirements.txt        # Project dependencies
run.py                 # Application entry point
README.md               # Project documentation
 file
```


##  API Design
create_rule(rule_string): Parses and returns an AST node.

combine_rules(rules): Merges multiple rules into a single AST.

evaluate_rule(data): Evaluates the combined AST against the provided data.


<hr/>

### system requriments 🛠️
- Python 3.6 or higher
- Flask
- SQLite (Database)

### Build and installation
1. **Clone the Repository**
 ```bash
   git clone https://github.com/shubhamg0sai/zeotap_rule_engine_assignment.git
   cd zeotap_rule_engine_assignment
   cd rule_engine
   ```
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```
   ```bash
   venv/Scripts/activate  # For Windows
   ```
    # OR
   ```bash
   source venv/bin/activate  # For macOS/Linux
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   python run.py
   ```
   Open your web browser and go to http://127.0.0.1:4444/.
<hr/>

# Input Sample Rules
 **Rule 1:**
```bash
  ((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)
  ```
  **Rule 2:**
```bash
 ((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)
  ```


Input a Query to Evaluate:

  ```bash
  {
    "age": 50,
    "department": "Sales",
    "salary": 60000,
    "experience": 10
  }
  ```
<hr/>
## Working:

https://github.com/shubhamg0sai/zeotap_rule_engine_assignment/raw/refs/heads/Delete/rule_engine/rule_engine.mp4
