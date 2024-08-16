
# ViTIP: AI-Powered Vietnamese Traditional Instrument Preservation System using 3D space

The ViTIP project uses artificial intelligence to preserve Vietnam's traditional musical instruments. It detects and classifies instruments using image data, provides 3D visualizations, and enriches contextual information with a lightweight ontology. This project is for cultural heritage professionals, researchers, and the general public interested in preserving and learning about Vietnam’s cultural heritage.

## Table of Contents
- [Dataset](#dataset)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [Authors](#authors)
- [Contact](#contact)

## Dataset
The ViTIP dataset is publicly listed on Roboflow Universe: [click here!](https://universe.roboflow.com/hieu10nguyen06/nhac-cu-dan-toc-viet-nam)

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

### 1. Clone the repository:
   ```bash
   git clone https://github.com/imxuan03/vietnamese-traditional-instrument-preservation-system.git
   cd ViTIP
   ```
### 2. Install the required Python packages:
   ```bash
   pip install Django djangorestframework ultralytics owlready2 opencv-python-headless numpy tensorflow
   ```
### 3. Set up Django:
   ```bash
   cd instrument
   python manage.py migrate
   python manage.py runserver
   ```
### 4. Frontend

This template should help get you started developing with Vue 3 in Vite.

#### Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

#### Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

#### Project Setup

```sh
cd ..
cd frontend
npm install
```

#### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```
### 5. Set up front-end:
   Include Three.js, OrbitControls, and GLTFLoader in your project. Install Vue.js using npm:
   ```bash
   npm install vue
```
### 6. Access the web platform (at http://localhost:3001/).



## Usage
1. Object Detection: Upload images to detect and localize instruments.
2. Classification: Classify detected instruments using the trained model.
3. 3D Visualization: Explore detailed 3D models of each instrument.
4. Ontology Information: View enriched contextual information about each instrument.


## Screenshots

ViTIP framework

<img width="100%" alt="framework" src="https://github.com/user-attachments/assets/ca3ca6d1-8caa-4625-91a6-fe4c939a425b">

ViTIP Demo

<img src="https://github.com/user-attachments/assets/0e0376be-a919-4482-8716-3603228f992f" alt="..." width="100%" height="auto" />

##  Contributing
We welcome contributions from the community. To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## Authors
- [@truongthanhma](https://github.com/truongthanhma)
- [@hieu10-06](https://github.com/hieu10-06)
- [@Michael-Ngn](https://github.com/Michael-Ngn)
- [@imxuan03](https://github.com/imxuan03)

## Contact
For any questions or suggestions, please contact mtthanh@ctu.edu.vn.

