________________________________________
AI-Powered Fault Detection for Product Reliability

This project leverages deep learning, specifically transfer learning with the VGG16 model, to automatically detect manufacturing defects in industrial components. The trained model is deployed in a user-friendly web application built with Flask.

Features

●	High-Accuracy Defect Detection: Utilizes a pre-trained VGG16 model, fine-tuned to achieve high accuracy in classifying products as "Good" or "Defective."
●	Web-Based Interface: A clean, modern, and mobile-responsive web application for easy interaction.
●	Real-Time Prediction: Users can upload an image of a product and receive an instant quality analysis.
●	Live Image Preview: The interface provides an instant preview of the uploaded image before analysis.

Technology Stack

●	Backend: Python, Flask
●	Machine Learning: TensorFlow, Keras
●	Model Architecture: VGG16 (Transfer Learning)
●	Frontend: HTML5, CSS3, JavaScript
●	Data Handling: NumPy

Project Structure

The project is organized into a standard Flask application structure.



/Fault_Detection_App
|
|-- static/
|   |-- style.css
|   |-- hero-background.png
|   |-- icon-email.png
|   |-- icon-phone.png
|   `-- icon-location.png
|
|-- templates/
|   |-- index.html
|   |-- about.html
|   |-- contact.html
|   |-- predict.html
|   `-- result.html
|
|-- uploads/
|   (This folder is created automatically to store uploaded images)
|
|-- app.py
`-- Vgg16_97.h5

●	app.py: The main Flask script that runs the web server and handles prediction logic.
●	Vgg16_97.h5: The saved, pre-trained Keras model.
●	templates/: Contains all the HTML files for the different web pages.
●	static/: Contains all static assets like the CSS stylesheet, background image, and icons.

Setup and Installation

To run this project locally, follow these steps:
1.	Clone the repository:
Bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name

2.	Install the required dependencies:
It is recommended to use a virtual environment.
Bash
pip install flask tensorflow numpy

3.	Run the application:
Execute the following command in your terminal.
Bash
python app.py

4.	Access the application:
Open your web browser and navigate to:
http://127.0.0.1:5000


Usage

1.	Navigate to the homepage and click "Begin Analysis".
2.	On the prediction page, click the "Choose File" button to select an image of a product.
3.	The selected image will be previewed on the page.
4.	Click the "Run Analysis" button to get the prediction.
5.	The result page will display the analyzed image and the model's prediction of its quality status.
