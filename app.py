from flask import Flask, render_template, request, redirect, session
import mysql.connector
from database import get_connection

app = Flask(__name__)
app.secret_key = "pythonpath_secret_key_aarohi"



# =====================================================
# 7-DAY COMPREHENSIVE CURRICULUM
# =====================================================

days = {
    1: {
        "title": "Introduction to Python & Basic Syntax",
        "description": "Learn what Python is, why it is popular, how print() works, comments, and simple calculations.",
        "content": """
        <div class="lesson-chunk">
            <h3>1. What is Python?</h3>
            <p>Python is a high-level, easy-to-read programming language created by <b>Guido van Rossum</b> in 1991. It reads almost like English, making it perfect for beginners while being powerful enough to build web apps, AI models, and automation scripts.</p>
        </div>

        <div class="lesson-chunk">
            <h3>2. Writing Your First Code with print()</h3>
            <p>The <code>print()</code> function displays messages and numbers on the screen. Put text inside quotes <code>'...'</code> or <code>"..."</code>:</p>
            <pre><code># Displaying text on the screen
print("Hello, World!")
print("Welcome, Aarohi!")
print("Python is fast, clean, and fun!")

# Printing numbers (no quotes needed for numbers!)
print(100)
print(3.14)</code></pre>
            <p>You can also print multiple values separated by commas. Python automatically adds a space between them:</p>
            <pre><code>print("Python", "Version", 3.12)
# Output: Python Version 3.12</code></pre>
        </div>

        <div class="lesson-chunk">
            <h3>3. Writing Comments (#)</h3>
            <p>Comments are notes for humans reading the code. Python ignores them when running the program:</p>
            <pre><code># This is a single-line comment
print("Code runs here!")  # This line prints a message

\"\"\"
This is a multi-line comment or docstring.
Useful when explaining complex algorithms or steps.
Python ignores all text inside here!
\"\"\"
</code>
</pre>
        </div>

        <div class="lesson-chunk">
            <h3>4. Python as a Quick Calculator</h3>
            <p>You can use Python directly for arithmetic calculations:</p>
            <pre><code># Everyday math operations
total_inventory = 150 + 75
print("Total Inventory:", total_inventory)   # 225

anshul_score = 45 * 2
print("Anshul Score:", anshul_score)         # 90

print(50 / 5)     # 10.0 (division always returns a float)
print(2 ** 4)     # 16 (2 to the power 4)</code></pre>
        </div>

        <div class="tip-box">
            <b>Beginner Tip:</b> Python is <b>case-sensitive</b>! <code>print()</code> works, but <code>Print()</code> or <code>PRINT()</code> will cause a NameError.
        </div>
        """
    },

    2: {
        "title": "Variables, Data Types & Type Conversion",
        "description": "Store values in memory with variables, master int, float, str, bool, and learn type casting.",
        "content": """
        <div class="lesson-chunk">
            <h3>1. What is a Variable?</h3>
            <p>A variable is a named container that stores data in computer memory. Set a value with <code>=</code>:</p>
            <pre><code>username = "Alex"
level = 5
rating = 4.9
is_active = True

print(username)
print(level)
print(rating)</code></pre>
        </div>

        <div class="lesson-chunk">
            <h3>2. Variable Naming Rules</h3>
            <ul>
                <li>Must start with a letter (a-z) or an underscore <code>_</code> (e.g. <code>user_name</code>).</li>
                <li>Cannot start with a number (e.g. <code>1name</code> is invalid).</li>
                <li>Use letters, numbers, and underscores (no spaces or hyphens).</li>
            </ul>
        </div>

        <div class="lesson-chunk">
            <h3>3. Fundamental Data Types</h3>
            <table class="lesson-table">
                <thead>
                    <tr><th>Data Type</th><th>Description</th><th>Example</th></tr>
                </thead>
                <tbody>
                    <tr><td><code>int</code></td><td>Whole numbers</td><td><code>age = 20</code></td></tr>
                    <tr><td><code>float</code></td><td>Decimal numbers</td><td><code>price = 19.99</code></td></tr>
                    <tr><td><code>str</code></td><td>Text in quotes</td><td><code>city = "Tokyo"</code></td></tr>
                    <tr><td><code>bool</code></td><td>True or False</td><td><code>is_logged_in = True</code></td></tr>
                </tbody>
            </table>
        </div>

        <div class="lesson-chunk">
            <h3>4. Checking Types with type()</h3>
            <pre><code>device = "Smartwatch"
battery_pct = 95
price = 199.99

print(type(device))       # &lt;class 'str'&gt;
print(type(battery_pct))  # &lt;class 'int'&gt;
print(type(price))        # &lt;class 'float'&gt;</code></pre>
        </div>

        <div class="lesson-chunk">
            <h3>5. Type Conversion (Type Casting)</h3>
            <p>Convert data between types using <code>int()</code>, <code>float()</code>, or <code>str()</code>:</p>
            <pre><code># Convert string to number
num_text = "50"
num = int(num_text)
print(num + 10)     # Output: 60

# Convert number to string
user_age = 22
message = "Coder is " + str(user_age) + " years old."
print(message)</code></pre>
        </div>

        <div class="tip-box">
            <b>Easy Tip: Formatted Strings (f-strings):</b> Put an <code>f</code> before the quotes and place variables inside <code>{...}</code>:
            <pre><code>name = "Aarohi"
score = 98
print(f"Developer {name} earned {score} points!")</code></pre>
        </div>
        """
    },

    3: {
        "title": "User Input & Python Operators",
        "description": "Receive interactive input with input(), and learn arithmetic, comparison, and logical operators.",
        "content": """
        <div class="lesson-chunk">
            <h3>1. Taking User Input with input()</h3>
            <p>The <code>input()</code> function lets the user type something from the keyboard:</p>
            <pre><code>player_name = input("Enter player name: ")
print(f"Welcome to the game, {player_name}!")</code></pre>
            <p><b>Note:</b> <code>input()</code> always gives you text (string). Convert it with <code>int()</code> if you need a number:</p>
            <pre><code>age = input("Enter your age: ")
age = int(age)
print(f"Next year you will be {age + 1} years old.")</code></pre>
        </div>

        <div class="lesson-chunk">
            <h3>2. Arithmetic Operators</h3>
            <ul>
                <li><code>+</code> (Addition): <code>10 + 5</code> is <code>15</code></li>
                <li><code>-</code> (Subtraction): <code>10 - 4</code> is <code>6</code></li>
                <li><code>*</code> (Multiplication): <code>4 * 5</code> is <code>20</code></li>
                <li><code>/</code> (Division): <code>10 / 2</code> is <code>5.0</code></li>
                <li><code>//</code> (Floor Division): <code>10 // 3</code> is <code>3</code> (chops decimals)</li>
                <li><code>%</code> (Modulo / Remainder): <code>10 % 3</code> is <code>1</code></li>
                <li><code>**</code> (Power): <code>2 ** 3</code> is <code>8</code></li>
            </ul>
        </div>

        <div class="lesson-chunk">
            <h3>3. Comparison Operators</h3>
            <p>Comparisons return <code>True</code> or <code>False</code>:</p>
            <pre><code># Score verification example
chitransh_score = 92
passing_score = 75

print(chitransh_score >= passing_score)  # True
print(chitransh_score == 100)            # False
print(chitransh_score != 50)             # True</code></pre>
        </div>

        <div class="lesson-chunk">
            <h3>4. Logical Operators (and, or, not)</h3>
            <pre><code>passed_exam = True
submitted_homework = True

# Both must be True
completed = passed_exam and submitted_homework
print("Ready for certificate:", completed)  # True</code></pre>
        </div>
        """
    },

    4: {
        "title": "Conditional Statements (if, elif, else)",
        "description": "Make decisions in code using if, elif, else, and understand Python's indentation rules.",
        "content": """
        <div class="lesson-chunk">
            <h3>1. The if Statement</h3>
            <p>Use <code>if</code> when you want code to run only when a condition is True:</p>
            <pre><code>temperature = 32

if temperature > 30:
    print("It's a hot sunny day! Stay hydrated.")</code></pre>
        </div>

        <div class="lesson-chunk">
            <h3>2. Python Indentation</h3>
            <p>Python uses 4 spaces (indentation) to show which lines belong inside the <code>if</code> block:</p>
            <pre><code>if True:
    print("This line is inside the if block")
    print("This line is also inside")

print("This line is outside and always runs")</code></pre>
        </div>

        <div class="lesson-chunk">
            <h3>3. if - else Statement</h3>
            <pre><code>marks = 75

if marks >= 50:
    print("You passed the exam!")
else:
    print("You need to retry.")</code></pre>
        </div>

        <div class="lesson-chunk">
            <h3>4. Multiple Choices with elif</h3>
            <pre><code>score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"

print(f"Final Grade: {grade}")</code></pre>
        </div>
        """
    },

    5: {
        "title": "Loops & Iteration (for and while)",
        "description": "Automate repeated tasks using for loops with range(), while loops, and break/continue statements.",
        "content": """
        <div class="lesson-chunk">
            <h3>1. The for Loop with range()</h3>
            <p>Use a <code>for</code> loop to repeat an action multiple times:</p>
            <pre><code># Prints numbers 1 to 5
for i in range(1, 6):
    print(f"Practice Step {i}")</code></pre>
        </div>

        <div class="lesson-chunk">
            <h3>2. Looping Through a List</h3>
            <p>You can easily iterate through every item in a list:</p>
            <pre><code>languages = ["Python", "JavaScript", "SQL", "Rust"]

for lang in languages:
    print(f"Mastering: {lang}")</code></pre>
        </div>

        <div class="lesson-chunk">
            <h3>3. The while Loop</h3>
            <p>A <code>while</code> loop keeps running as long as its condition remains True:</p>
            <pre><code>count = 1

while count <= 4:
    print(f"Count is: {count}")
    count += 1  # Add 1 each time</code></pre>
        </div>

        <div class="lesson-chunk">
            <h3>4. break and continue</h3>
            <ul>
                <li><code>break</code>: Stops the loop immediately.</li>
                <li><code>continue</code>: Skips the current turn and moves to the next.</li>
            </ul>
            <pre><code># Stop when we find Anshul in the roster
participants = ["Alex", "Jordan", "Anshul", "Taylor"]
for person in participants:
    if person == "Anshul":
        print("Found Anshul! Stopping search.")
        break
    print("Inspecting:", person)</code></pre>
        </div>
        """
    },

    6: {
        "title": "Python Collections (Lists, Tuples, Dictionaries)",
        "description": "Manage groups of items using ordered lists, immutable tuples, unique sets, and key-value dictionaries.",
        "content": """
        <div class="lesson-chunk">
            <h3>1. Lists (Ordered & Changeable)</h3>
            <p>Lists hold multiple items inside square brackets <code>[...]</code>:</p>
            <pre><code>team = ["Maya", "Chitransh", "David"]

# Indexing starts at 0!
print(team[0])   # "Maya"
print(team[1])   # "Chitransh" (index 1 is the 2nd item)
print(team[-1])  # "David" (last item)

# Adding a new item to the end
team.append("Sarah")

# Number of items
print(len(team)) # 4</code></pre>
        </div>

        <div class="lesson-chunk">
            <h3>2. Tuples (Ordered & Cannot Be Changed)</h3>
            <p>Tuples use parentheses <code>(...)</code> and cannot be modified once created:</p>
            <pre><code>resolution = (1920, 1080)
print(resolution[0])  # 1920</code></pre>
        </div>

        <div class="lesson-chunk">
            <h3>3. Dictionaries (Key : Value Pairs)</h3>
            <p>Dictionaries store information in <code>key: value</code> pairs using curly braces <code>{...}</code>:</p>
            <pre><code>product = {
    "item": "Mechanical Keyboard",
    "brand": "Keychron",
    "price": 89.99
}

# Access values by their key name
print(product["item"])   # "Mechanical Keyboard"
print(product["price"])  # 89.99

# Update a value
product["price"] = 79.99
print(product)</code></pre>
        </div>

        <div class="lesson-chunk">
            <h3>4. Sets (Unique Items)</h3>
            <p>Sets automatically remove duplicate values:</p>
            <pre><code>skills = {"Python", "Flask", "Python", "SQL"}
print(skills)  # Output: {'Python', 'Flask', 'SQL'} (no duplicates!)</code></pre>
        </div>

        <div class="tip-box">
            <b>Quick Summary:</b>
            <ul>
                <li><b>List:</b> <code>["Python", "JavaScript", "SQL"]</code> (Can be changed)</li>
                <li><b>Tuple:</b> <code>(1920, 1080)</code> (Cannot be changed)</li>
                <li><b>Dictionary:</b> <code>{"item": "Laptop", "price": 999}</code> (Key-value pairs)</li>
                <li><b>Set:</b> <code>{"Python", "SQL"}</code> (Unique items)</li>
            </ul>
        </div>
        """
    },

    7: {
        "title": "Functions & Gentle Intro to NumPy and Pandas",
        "description": "Write clean reusable code with def and return, and take your first look at NumPy arrays and Pandas DataFrames.",
        "content": """
        <div class="lesson-chunk">
            <h3>1. What is a Function?</h3>
            <p>A function is a reusable block of code that you define once with <code>def</code> and can call anytime:</p>
            <pre><code># Defining a simple function
def say_hello():
    print("Welcome to Python!")

# Calling the function
say_hello()
say_hello()</code></pre>
        </div>

        <div class="lesson-chunk">
            <h3>2. Function Parameters</h3>
            <p>Pass data into functions using parameters:</p>
            <pre><code>def greet(coder):
    print(f"Hello, {coder}! Ready to build?")

greet("Aarohi")
greet("Jordan")</code></pre>
        </div>

        <div class="lesson-chunk">
            <h3>3. Returning Values with return</h3>
            <pre><code>def add_numbers(a, b):
    return a + b

total = add_numbers(40, 60)
print("Total:", total)  # 100</code></pre>
        </div>

        <div class="lesson-chunk">
            <h3>4. First Look at NumPy</h3>
            <p>NumPy is used for fast numerical calculations on arrays:</p>
            <pre><code>import numpy as np

scores = np.array([95, 90, 88])
print("Average score:", scores.mean())  # 91.0
print("Highest score:", scores.max())   # 95</code></pre>
        </div>

        <div class="lesson-chunk">
            <h3>5. First Look at Pandas</h3>
            <p>Pandas provides the <b>DataFrame</b>, which looks like a neat spreadsheet table:</p>
            <pre><code>import pandas as pd

data = {
    "Product": ["Laptop", "Monitor", "Keyboard", "Mouse"],
    "Units_Sold": [45, 80, 120, 210]
}

df = pd.DataFrame(data)
print(df)</code></pre>
        </div>

        <div class="tip-box">
            <b>Congratulations!</b> You have completed the 7-day Python basics covering syntax, variables, operators, conditionals, loops, lists, dictionaries, functions, and introductory data libraries!
        </div>
        """
    }
}


# =====================================================
# 5 QUESTIONS PER DAY (35 HIGH-QUALITY QUESTIONS)
# =====================================================

quiz_questions = {
    1: [
        {
            "question": "Which function is used in Python to display output on the screen?",
            "options": ["display()", "print()", "show()", "console.log()"],
            "answer": "print()"
        },
        {
            "question": "How do you write a single-line comment in Python?",
            "options": ["// This is a comment", "# This is a comment", "<!-- This is a comment -->", "/* This is a comment */"],
            "answer": "# This is a comment"
        },
        {
            "question": "What is the output of print('Hello', 'World')?",
            "options": ["Hello World", "HelloWorld", "'Hello' 'World'", "Error"],
            "answer": "Hello World"
        },
        {
            "question": "Is Python case-sensitive for keywords like print?",
            "options": ["Yes, print and Print are completely different", "No, Python ignores case", "Only on Linux", "Only for numbers"],
            "answer": "Yes, print and Print are completely different"
        },
        {
            "question": "What is the output of print(10 + 5 * 2)?",
            "options": ["30", "20", "25", "100"],
            "answer": "20"
        }
    ],

    2: [
        {
            "question": "Which of the following is a valid variable name in Python?",
            "options": ["1st_student", "user_name", "user name", "def"],
            "answer": "user_name"
        },
        {
            "question": "What data type is the value 95.5 in Python?",
            "options": ["int", "str", "float", "bool"],
            "answer": "float"
        },
        {
            "question": "What does type(True) return in Python?",
            "options": ["<class 'bool'>", "<class 'str'>", "<class 'int'>", "<class 'boolean'>"],
            "answer": "<class 'bool'>"
        },
        {
            "question": "What is the result of int('40') + 10?",
            "options": ["50", "'4010'", "Error", "'50'"],
            "answer": "50"
        },
        {
            "question": "What do formatted strings (f-strings like f'Hello {name}') do?",
            "options": [
                "Insert variable values directly inside curly brackets",
                "Format code according to PEP8",
                "Create a float variable",
                "Encrypt the text"
            ],
            "answer": "Insert variable values directly inside curly brackets"
        }
    ],

    3: [
        {
            "question": "What data type does the input() function always return by default?",
            "options": ["str", "int", "float", "bool"],
            "answer": "str"
        },
        {
            "question": "What is the result of 17 % 5 in Python (modulo operator)?",
            "options": ["3", "2", "3.4", "1"],
            "answer": "2"
        },
        {
            "question": "Which operator performs floor division (divides and discards decimals)?",
            "options": ["/", "//", "%", "**"],
            "answer": "//"
        },
        {
            "question": "Which comparison operator checks if two values are equal?",
            "options": ["=", "==", "===", "equals"],
            "answer": "=="
        },
        {
            "question": "If score = 95, what does (score > 90) evaluate to?",
            "options": ["True", "False", "None", "Error"],
            "answer": "True"
        }
    ],

    4: [
        {
            "question": "How does Python define code blocks inside an if statement?",
            "options": [
                "Using indentation (spaces)",
                "Using curly braces { }",
                "Using square brackets [ ]",
                "Using semicolons ;"
            ],
            "answer": "Using indentation (spaces)"
        },
        {
            "question": "Which Python keyword stands for 'else if' when checking multiple conditions?",
            "options": ["elseif", "elif", "else if", "when"],
            "answer": "elif"
        },
        {
            "question": "What will this code print: if 8 > 5: print('Pass') else: print('Fail')?",
            "options": ["Pass", "Fail", "Nothing", "Syntax Error"],
            "answer": "Pass"
        },
        {
            "question": "Which block executes if none of the if or elif conditions are True?",
            "options": ["else", "default", "finally", "stop"],
            "answer": "else"
        },
        {
            "question": "Can an if statement exist on its own without an else part?",
            "options": ["Yes, the else block is optional", "No, else is mandatory", "Only inside a function", "Only in loops"],
            "answer": "Yes, the else block is optional"
        }
    ],

    5: [
        {
            "question": "Which numbers are generated by range(1, 5)?",
            "options": ["1, 2, 3, 4, 5", "1, 2, 3, 4", "0, 1, 2, 3, 4", "1, 3, 5"],
            "answer": "1, 2, 3, 4"
        },
        {
            "question": "Which loop repeats as long as a specified condition remains True?",
            "options": ["for loop", "while loop", "repeat loop", "foreach loop"],
            "answer": "while loop"
        },
        {
            "question": "Which keyword immediately exits and terminates a loop?",
            "options": ["break", "stop", "exit", "continue"],
            "answer": "break"
        },
        {
            "question": "Which keyword skips the current iteration and jumps to the next turn of the loop?",
            "options": ["continue", "skip", "pass", "next"],
            "answer": "continue"
        },
        {
            "question": "How many times does this loop run: for x in ['Python', 'Flask', 'SQL']?",
            "options": ["3 times", "4 times", "2 times", "1 time"],
            "answer": "3 times"
        }
    ],

    6: [
        {
            "question": "Given items = ['Laptop', 'Mouse', 'Keyboard'], what does items[0] return?",
            "options": ["'Laptop'", "'Mouse'", "'Keyboard'", "IndexError"],
            "answer": "'Laptop'"
        },
        {
            "question": "Which method adds a new element to the end of an existing list?",
            "options": [".add()", ".append()", ".insert_last()", ".push()"],
            "answer": ".append()"
        },
        {
            "question": "What is the key difference between a List and a Tuple?",
            "options": [
                "Tuples are immutable (cannot be changed), while Lists can be changed",
                "Lists can only store integers",
                "Tuples cannot be indexed",
                "There is no difference"
            ],
            "answer": "Tuples are immutable (cannot be changed), while Lists can be changed"
        },
        {
            "question": "What Python collection is {'item': 'Laptop', 'price': 999}?",
            "options": ["Dictionary", "List", "Tuple", "Set"],
            "answer": "Dictionary"
        },
        {
            "question": "What will set(['apple', 'apple', 'banana']) output?",
            "options": ["{'apple', 'banana'}", "['apple', 'apple']", "Error", "3 items"],
            "answer": "{'apple', 'banana'}"
        }
    ],

    7: [
        {
            "question": "Which keyword is used to define a new function in Python?",
            "options": ["def", "function", "func", "define"],
            "answer": "def"
        },
        {
            "question": "Which statement sends a value back from a function to the caller?",
            "options": ["return", "send", "give", "output"],
            "answer": "return"
        },
        {
            "question": "What is the standard conventional import alias for NumPy?",
            "options": ["import numpy as np", "import numpy as npy", "import numpy as num", "import numpy as math"],
            "answer": "import numpy as np"
        },
        {
            "question": "If scores = np.array([95, 90, 85]), which method returns the highest number?",
            "options": [".max()", ".mean()", ".high()", ".top()"],
            "answer": ".max()"
        },
        {
            "question": "What is a 2-dimensional tabular data structure with rows and columns called in Pandas?",
            "options": ["DataFrame", "DataSheet", "DataMatrix", "DataTable"],
            "answer": "DataFrame"
        }
    ]
}


# =====================================================
# ROUTES
# =====================================================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email    = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if not username or not email or not password:
            return render_template("signup.html", error="All fields are required.", username=username, email=email)

        conn = get_connection()
        if conn is None:
            return render_template("signup.html", error="Database connection failed. Please ensure MySQL is running.", username=username, email=email)

        cursor = None
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
            if cursor.fetchone():
                return render_template("signup.html", error="An account with this email already exists.", username=username, email=email)

            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                (username, email, password)
            )
            conn.commit()
            return redirect("/login?registered=1")

        except mysql.connector.Error as e:
            print("Signup Database Error:", e)
            return render_template("signup.html", error="Something went wrong during signup. Please try again.", username=username, email=email)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    registered = request.args.get("registered") == "1"
    success_msg = "Account created successfully! Please sign in." if registered else None

    if request.method == "POST":
        email    = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if not email or not password:
            return render_template("login.html", error="Email and password are required.", email=email)

        conn = get_connection()
        if conn is None:
            return render_template("login.html", error="Database connection failed. Please ensure MySQL is running.", email=email)

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                "SELECT * FROM users WHERE email = %s AND password = %s",
                (email, password)
            )
            user = cursor.fetchone()

            if user:
                session["user_id"]  = user["id"]
                session["username"] = user["username"]
                return redirect("/dashboard")

            return render_template("login.html", error="Invalid email or password.", email=email)

        except mysql.connector.Error as e:
            print("Login Database Error:", e)
            return render_template("login.html", error="Something went wrong during login. Please try again.", email=email)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    return render_template("login.html", success=success_msg)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    conn = get_connection()
    if conn is None:
        return "Database connection failed. Please check MySQL."

    cursor = None
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT day_number FROM progress WHERE user_id = %s AND completed = TRUE",
            (session["user_id"],)
        )
        completed_rows = cursor.fetchall()
        completed = [row["day_number"] for row in completed_rows]

        progress = int((len(completed) / 7) * 100)

        return render_template(
            "dashboard.html",
            username=session["username"],
            completed=completed,
            progress=progress,
            days=days
        )
    except mysql.connector.Error as e:
        print("Dashboard Error:", e)
        return "Failed to load dashboard."
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route("/day/<int:day_number>")
def day(day_number):
    if "user_id" not in session:
        return redirect("/login")
    if day_number not in days:
        return redirect("/dashboard")

    return render_template(
        "day.html",
        day_number=day_number,
        day=days[day_number],
        total_days=len(days)
    )


@app.route("/complete/<int:day_number>")
def complete_day(day_number):
    if "user_id" not in session:
        return redirect("/login")

    if day_number not in days:
        return redirect("/dashboard")

    conn = get_connection()
    if conn:
        cursor = None
        try:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO progress (user_id, day_number, completed)
                VALUES (%s, %s, TRUE)
                ON DUPLICATE KEY UPDATE completed = TRUE
                """,
                (session["user_id"], day_number)
            )
            conn.commit()
        except mysql.connector.Error as e:
            print("Complete Day Error:", e)
        finally:
            if cursor:
                cursor.close()
            conn.close()

    return redirect("/dashboard")


@app.route("/quiz/<int:day_number>")
def quiz(day_number):
    if "user_id" not in session:
        return redirect("/login")

    questions = quiz_questions.get(day_number)
    if not questions:
        return redirect("/dashboard")

    return render_template(
        "quiz.html",
        day_number=day_number,
        day_title=days[day_number]["title"],
        questions=questions
    )


@app.route("/quiz/<int:day_number>/submit", methods=["POST"])
def submit_quiz(day_number):
    if "user_id" not in session:
        return redirect("/login")

    questions = quiz_questions.get(day_number)
    if not questions:
        return redirect("/dashboard")

    score = 0
    total = len(questions)

    for i, q in enumerate(questions):
        user_answer = request.form.get("q" + str(i))
        if user_answer == q["answer"]:
            score += 1

    # Save result to database
    conn = get_connection()
    if conn:
        cursor = None
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO quiz_results (user_id, day_number, score, total) VALUES (%s, %s, %s, %s)",
                (session["user_id"], day_number, score, total)
            )
            # If user scored at least 3 out of 5, mark the day as completed!
            if score >= 3:
                cursor.execute(
                    """
                    INSERT INTO progress (user_id, day_number, completed)
                    VALUES (%s, %s, TRUE)
                    ON DUPLICATE KEY UPDATE completed = TRUE
                    """,
                    (session["user_id"], day_number)
                )
            conn.commit()
        except mysql.connector.Error as e:
            print("Save Quiz Result Error:", e)
        finally:
            if cursor:
                cursor.close()
            conn.close()

    return render_template(
        "result.html",
        score=score,
        total=total,
        day_number=day_number,
        passed=(score >= 3)
    )


@app.route("/game")
def game():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("game.html")


if __name__ == "__main__":
    app.run(debug=True)