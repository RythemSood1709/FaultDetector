import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from flask import Flask, request, render_template

# Get the base directory where this script is located (which will be the 'Code' folder)
BASE_DIR = os.path.dirname(__file__)

# Initialize the Flask application
# Flask will automatically look for 'templates' and 'static' folders relative to this script's location.
# So, if this script is in 'Code/', it will look for 'Code/templates/' and 'Code/static/'.
app = Flask(__name__)

# Load the Keras model.
# The model file 'Vgg16_97.h5' is now expected to be in the same directory as this script (i.e., 'Code/').
model_path = os.path.join(BASE_DIR, 'Vgg16_97.h5')
try:
    model = tf.keras.models.load_model(model_path)
    print(f"Model loaded successfully from: {model_path}")
except Exception as e:
    print(f"Error loading model from {model_path}: {e}")
    # You might want to handle this error more gracefully in a production environment
    # For now, we'll let the app potentially crash if the model isn't found.


def model_predict(img_path, model):
    """
    Performs a prediction on an image using the loaded Keras model.

    Args:
        img_path (str): The file path to the image.
        model (tf.keras.Model): The loaded Keras model.

    Returns:
        numpy.ndarray: The prediction output from the model.
    """
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)  # Add batch dimension
    x = preprocess_input(x)  # Preprocess the image for VGG16
    preds = model.predict(x)
    return preds

@app.route('/')
def index():
    """Renders the home page."""
    return render_template('index.html')

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template('contact.html')

@app.route('/predict')
def predict_page():
    """Renders the prediction upload page."""
    return render_template('predict.html')

@app.route('/submit', methods=['POST'])
def submit():
    """
    Handles image upload and prediction submission.
    """
    if request.method == 'POST':
        # Get the uploaded file from the request
        f = request.files['file']

        # Define the path to save the uploaded file.
        # It will be saved in 'Code/static/uploads/'
        uploads_dir = os.path.join(BASE_DIR, 'static', 'uploads')
        os.makedirs(uploads_dir, exist_ok=True) # Create the directory if it doesn't exist

        file_path = os.path.join(uploads_dir, f.filename)
        f.save(file_path) # Save the uploaded file

        # Get prediction from the model
        prediction_value = model_predict(file_path, model)

        # Determine the prediction text and class based on the model's output
        if prediction_value[0][0] < 0.5:
            prediction_text = "STATUS: DEFECTIVE PRODUCT"
            prediction_class = "default_product"
        else:
            prediction_text = "STATUS: GOOD PRODUCT"
            prediction_class = "good_product"
            
        # Render the result page with prediction details
        return render_template('result.html', 
                                prediction_text=prediction_text, 
                                prediction_class=prediction_class, 
                                image_filename=f.filename)

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)

