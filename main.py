from flask import Flask, request, render_template, redirect, url_for, session, flash
from functools import wraps
# import google.generativeai as genai


app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key in production

# Dummy user database - in a real app, this would be a proper database
users = {
    'demo': {'password': '12345', 'username': 'Venkat'}
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('signin'))
        return f(*args, **kwargs)
    return decorated_function

"""
genai.configure(api_key="AIzaSyDkJgyGe5g_Cqma16QaRhcORYsGaBtZAq8")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

inputval = str(input())

response = chat_session.send_message(inputval)

print(response.text)

"""


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/cart")
@login_required
def cart():
    return render_template("cart.html")

@app.route("/finance")
@login_required
def finance():
    return render_template("finance.html", accountname=session.get('username', 'Guest'))

@app.route("/products")
@login_required
def products():
    return render_template("products.html", accountname=session.get('username', 'Guest'))

@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('main'))
        else:
            flash('Invalid username or password')
    
    return render_template("signin.html")

@app.route("/signout")
def signout():
    session.pop('username', None)
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)
    