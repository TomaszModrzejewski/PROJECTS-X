from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the homepage of the VPS setup guide.
    """
    return render_template('index.html')

# Run the application
if __name__ == '__main__':
    # Debug mode allows for automatic reloading when code changes
    app.run(debug=True)