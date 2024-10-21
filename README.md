# Ocular Disease Detection System

### Overview
This project is focused on detecting **7 types of ocular diseases** from **color fundus images** using a deep learning approach. We developed a **Convolutional Neural Network (CNN)** model that is trained on the **Ocular Disease Intelligent Recognition (ODIR)** dataset, which contains color fundus images of patients with various eye conditions. The project addresses the issue of class imbalance during training to improve the performance of the model.

The diseases detected by this system are:
- **Normal (N)**
- **Diabetes (D)**
- **Glaucoma (G)**
- **Cataract (C)**
- **Age-related Macular Degeneration (A)**
- **Hypertension (H)**
- **Pathological Myopia (M)**
- **Other diseases/abnormalities (O)**

A web application built using **Streamlit** allows healthcare professionals to upload patient fundus images, input patient details, and receive disease predictions. The patient information and predictions are stored in a **MySQL database** for future reference.

### Key Features
- **Deep Learning Model**: A trained CNN model capable of detecting 7 types of ocular diseases from color fundus images.
- **ODIR Dataset**: The system is built on the Ocular Disease Intelligent Recognition (ODIR) dataset, which consists of fundus images labeled with various eye conditions.
- **Data Preprocessing**: Techniques were implemented to resolve class imbalance, enhancing the model’s accuracy across all disease types.
- **Streamlit Web Application**: An easy-to-use interface where healthcare professionals can:
  - Upload patient fundus images.
  - Input patient details.
  - Get model predictions for ocular diseases.
  - Store patient details and predictions in a secure MySQL database.
- **MySQL Database Integration**: All patient information and disease predictions are stored in a MySQL database for future analysis and reference.

### Dataset
- **Dataset**: Ocular Disease Intelligent Recognition (ODIR) Dataset
  - Contains color fundus images of patients, with labels for 7 types of ocular diseases:
    - Normal (N)
    - Diabetes (D)
    - Glaucoma (G)
    - Cataract (C)
    - Age-related Macular Degeneration (A)
    - Hypertension (H)
    - Pathological Myopia (M)
    - Other diseases/abnormalities (O)
- **Preprocessing**: Preprocessing steps were applied to handle class imbalance and ensure the model can generalize well to all disease types.

### Technologies Used
- **Python**: The primary programming language for model training and web app development.
- **TensorFlow/Keras**: Used for building and training the CNN model.
- **Streamlit**: For developing the interactive web app.
- **Pandas**: For data handling and manipulation.
- **MySQL**: Used for storing patient information and predictions.

### Installation
To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ocular-disease-detection.git
   ```

2. Navigate to the project directory:
   ```bash
   cd ocular-disease-detection
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Set up the MySQL database:
   - Create a MySQL database and update the database configuration in the project (e.g., `db_config.py`).
   - Run the `db_setup.sql` file to create the necessary tables:
     ```bash
     mysql -u username -p database_name < db_setup.sql
     ```

### Usage
1. To run the Streamlit web application, execute:
   ```bash
   streamlit run app.py
   ```

2. The application will launch in your default web browser. You can:
   - Upload a color fundus image for disease prediction.
   - Input patient details (name, age, remarks).
   - View the prediction results for the uploaded image.
   - Store the patient details and prediction in the MySQL database.

### Example Use Case
A healthcare professional uploads a patient’s fundus image and enters the patient’s details. The system predicts the presence of any of the 7 ocular diseases and stores the prediction and patient details in the MySQL database for future reference.

### Future Enhancements
- **Improved Model Performance**: Further tuning of the CNN model to improve accuracy and reduce false positives.
- **Integration with EHR Systems**: Linking the system to electronic health records for seamless data management.
- **Data Augmentation**: Adding advanced augmentation techniques to improve model robustness.
- **Multi-Language Support**: Expanding the web app interface to support multiple languages for broader accessibility.

### Contributing
Contributions to the project are welcome. If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

### Contact Information
For further inquiries or suggestions, feel free to reach out at:
- **Email**: usama11javed@outlook.com
