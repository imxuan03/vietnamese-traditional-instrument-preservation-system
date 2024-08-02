
# ViTIP: AI-Powered Vietnamese Traditional Instrument Preservation System using 3D space

The ViTIP project uses artificial intelligence to preserve Vietnam's traditional musical instruments. It detects and classifies instruments using image data, provides 3D visualizations, and enriches contextual information with a lightweight ontology. This project is for cultural heritage professionals, researchers, and the general public interested in preserving and learning about Vietnam’s cultural heritage.

## Features

- **Object Detection and Localization**: Using YOLO to detect and localize musical instruments in images.
- **Classification**: Machine learning algorithms for accurate classification of instruments.
- **3D Models**: Detailed 3D models of each instrument for immersive visualizations.
- **Ontology**: A lightweight ontology enriches the contextual information associated with each instrument.
- **Web Platform**: A dedicated web platform to showcase and deploy these innovations.

### Prerequisites

#### Front-end
- **Three.js**: Core library for creating 3D objects and effects.
- **OrbitControls**: Module for adding orbit controls to the camera.
- **GLTFLoader**: Module for loading and displaying 3D models in GLTF format.
- **Vue.js**: JavaScript framework for building user interfaces.

#### Back-end
- **Django**: Web framework for building web applications.
- **Django REST Framework**: Library for building APIs with Django.
- **Ultralytics (YOLO)**: Library for object detection.
- **Owlready2**: Python library for working with Ontology data.
- **OpenCV (cv2)**: Library for image processing and computer vision.
- **NumPy**: Library for array and matrix operations.
- **TensorFlow (tf)**: Open-source library for machine learning and model training.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ViTIP.git
   cd ViTIP
2. Install the required Python packages:
   ```bash
   pip install Django djangorestframework ultralytics
   owlready2
   opencv-python-headless
   numpy
   tensorflow
3. Set up Django:
   ```bash
   python manage.py migrate
   python manage.py runserver
4. Set up front-end:
   Include Three.js, OrbitControls, and GLTFLoader in your project. Install Vue.js using npm:
   ```bash
   npm install vue
5. Access the web platform at http://localhost:3001/.






## Screenshots

ViTIP framework

<img src="https://github.com/user-attachments/assets/0e0376be-a919-4482-8716-3603228f992f" alt="..." width="100%" height="auto" />

## Authors

- [@octokatherine](https://www.github.com/octokatherine)

