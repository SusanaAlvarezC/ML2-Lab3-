# **Lab III - Advanced Topics**
## **Machine Learning II**

---

**Student 1:** Susana María Álvarez  
* **CC:** 1049609578
* **Email:** susana.alvarezc@udea.edu.co  

**Student 2:** Alejandro Martínez Henández  
* **CC:** 1035877060  
* **Email:** alejandro.martinezh@udea.edu.co  

---

**This project aims to fulfill point 5: "Bonus points if deployed on a local or cloud server."** 
Unfortunately, we encountered difficulties uploading it to a cloud server because the application exceeded the 500 MB limit. We attempted to deploy it on both Heroku and PythonAnywhere.

## Prerequisites

Make sure you have Python installed on your local machine. If you don't, download the latest version from the official Python website (https://www.python.org/downloads/).

## Virtual Environment Setup (optional but recommended)

1. Create a virtual environment with the following command:

   ```bash
   python -m venv env

2. Activate the virtual environment:
   * On Windows:
       env\Scripts\activate
   * On Unix or MacOS:
       source env/bin/activate
3. Install the necessary dependencies by running the following command:
   pip install -r requirements.txt

## Running the Project

Make sure you are in the project's root directory (/app) and execute the following command to start the application:

python app.py

La aplicación estará disponible en http://localhost:5000/.

## Additional Notes

Ensure you have the following libraries installed:

    Flask
    sentence_transformers
    transformers
    nltk
    numpy

You can install them manually or use the provided requirements.txt file.

## Project Structure

  * app folder: Contains the main file app.py, the tale.txt file, and the templates and static folders.
  * templates: Contains HTML files, such as index.html.
  * static: Contains static files, such as styles.css.
  * requirements.txt file contains necessary dependencies for execution.

## Application Instructions
When the application is run, the following interface will appear:
  ![imagen](https://github.com/SusanaAlvarezC/ML2-Lab3-/assets/22481634/981ed985-75fd-4827-89e0-01728031af68)
  ![imagen](https://github.com/SusanaAlvarezC/ML2-Lab3-/assets/22481634/62a66057-1d27-4d19-94f4-b919b3fb9a58)

1. Read the story.
2. Pose a question related to the text in the available textbox.
3. Select the model of your choice.
4. Click on "Get answer."

      




