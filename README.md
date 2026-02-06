#Photo to spiral art generator 

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Pygame-Interactive-green?style=for-the-badge&logo=pygame" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Generative-Art-purple?style=for-the-badge" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Status-Portfolio%20Ready-black?style=for-the-badge" /></a>
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/github/stars/USERNAME/REPO?style=for-the-badge" /></a>
  <a href="#"><img src="https://img.shields.io/github/forks/USERNAME/REPO?style=for-the-badge" /></a>
  <a href="#"><img src="https://img.shields.io/github/issues/USERNAME/REPO?style=for-the-badge" /></a>
  <a href="#"><img src="https://img.shields.io/github/license/USERNAME/REPO?style=for-the-badge" /></a>
</p>

<p align="center">
  A high performance generative art system that reconstructs an input image using a single continuous spiral line.<br/>
  Built with Python and Pygame for speed, precision, and live visual feedback.
</p>

---

## Project Overview

This project transforms a static input image into a one stroke spiral line artwork. Instead of rendering pixels or dots, the system draws one continuous polyline whose thickness varies based on image luminance.

Dark regions of the image generate denser, thicker strokes, while lighter regions produce thinner lines. The artwork is generated live on screen, allowing viewers to observe the full creation process in real time.

The result is a visually striking combination of algorithmic geometry, image processing, and artistic abstraction.

---

## Visual Characteristics

* Single continuous spiral path with no pen lifts
* Tonal shading achieved through stroke thickness modulation
* Live reconstruction of the image on screen
* High-detail output with smooth line continuity
* Suitable for exhibitions, portfolios, and academic demonstrations

---

## How the System Works

1. The input image is converted to grayscale
2. Pixel luminance values are extracted into a matrix
3. A mathematical spiral path is generated from the center outward
4. At each point along the spiral, the corresponding image brightness is sampled
5. Stroke thickness is dynamically adjusted based on luminance
6. The polyline is rendered continuously until the full image is reconstructed

---

## Features

* One-stroke spiral image reconstruction
* Real-time, visible drawing process
* Adjustable speed and detail balance
* High-resolution image sampling
* Optimized Pygame rendering loop
* Clean and minimal UI overlay

---

## Technology Stack

| Component            | Technology                     |
| -------------------- | ------------------------------ |
| Programming Language | Python                         |
| Rendering Engine     | Pygame                         |
| Image Processing     | Pillow, NumPy                  |
| Mathematical Model   | Polar geometry (spiral)        |
| Domain               | Generative and Algorithmic Art |

---

## Installation

```bash
pip install pygame pillow numpy
```

---

## Running the Project

1. Place an image file in the project directory
2. Rename the image to:

```text
input.jpg
```

3. Execute the program:

```bash
python design.py
```

The artwork will be generated live on screen until completion.

---

## Configuration

The visual style and performance can be adjusted using the configuration section in `design.py`:

```python
IMG_SIZE = 380          # Image resolution
SPIRAL_TURNS = 180     # Spiral density
POINTS_PER_TURN = 220  # Sampling accuracy
STEPS_PER_FRAME = 6    # Speed control
STROKE_SCALE = 4.0     # Shading intensity
```

---

## Preset Modes

High Detail Mode:

```python
IMG_SIZE = 450
STEPS_PER_FRAME = 4
```

Fast Preview Mode:

```python
IMG_SIZE = 300
STEPS_PER_FRAME = 10
```

Engraving Style:

```python
STROKE_SCALE = 6
```

---

## Author

Sarthak Bhopale
Student At MIT ADT

---

## License

This project is intended for educational, academic, and portfolio use.

Proper attribution is appreciated when using or modifying this work.

---

## Support the Project

If you find this project useful or inspiring:

* Star the repository
* Fork it and experiment with new styles
* Share your generated results

---

