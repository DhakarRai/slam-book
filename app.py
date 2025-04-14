from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Configure static folder for images and other assets
app.static_folder = 'static'

@app.route('/')
def slam_book():
    # Render the slam.html template
    return render_template('slam.html')

# Route to serve static files from the static directory
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    # Make sure the static folder exists
    if not os.path.exists('static'):
        os.makedirs('static')
    
    # Run the Flask app in debug mode
    app.run(debug=True)