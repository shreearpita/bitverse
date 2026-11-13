# ◈ BITVERSE

### Transform images into binary artwork.

BITVERSE is a Python-powered image-to-binary-art generator that transforms ordinary images into detailed visual compositions made entirely of `0`s and `1`s.

Using grayscale intensity mapping, Bayer matrix dithering, and monospace typography rendering, BITVERSE reconstructs images as binary patterns while preserving their recognizable visual structure.

---

## ✦ Features

- **Image to Binary Art:** Convert uploaded images into binary compositions.
- **Bayer Matrix Dithering:** Translate grayscale intensity into structured binary density patterns using a 4 × 4 threshold matrix.
- **Binary Typography:** Render the resulting binary matrix using a bundled monospace font.
- **Dual-Color Rendering:** Distinguish `1`s and `0`s using separate foreground colors.
- **PNG Export:** Download the generated binary artwork as an image.
- **TXT Export:** Download the underlying binary matrix as plain text.
- **Simple Interface:** Upload, generate, preview, and download through a Streamlit interface.

## ⚙️ How It Works

BITVERSE follows a multi-stage image-processing pipeline:

```text
       INPUT IMAGE
            │
            ▼
      IMAGE RESIZING
            │
            ▼
     GRAYSCALE MATRIX
            │
            ▼
    BAYER DITHERING
       (4 × 4 matrix)
            │
            ▼
     BINARY DENSITY
            │
            ▼
   TYPOGRAPHY RENDERING
            │
       ┌────┴────┐
       ▼         ▼
   PNG IMAGE   TXT MATRIX
```

### The underlying process

1. **Grayscale Conversion:** The input image is converted into a matrix of grayscale intensity values.
2. **Density Mapping:** Pixel brightness is mapped to binary density levels.
3. **Dithering:** A Bayer threshold matrix distributes binary patterns according to the intensity of each pixel.
4. **Typography Rendering:** The resulting binary matrix is rendered as monospace characters.
5. **Export:** The final artwork and its underlying binary representation are made available for download.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| NumPy | Matrix operations and numerical processing |
| Pillow | Image processing and typography rendering |
| Streamlit | Interactive web interface |
| DejaVu Sans Mono | Bundled monospace font |

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or later
- pip

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/bitverse.git
cd bitverse
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**
```powershell
.venv\Scripts\Activate.ps1
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run BITVERSE

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal to access the application.

## 📁 Project Structure

```text
bitverse/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── assets/
│   └── DejaVuSansMono.ttf
│
└── src/
    └── core/
        └── density_renderer.py
```

## 📦 Output

BITVERSE generates two downloadable files:

- `bitverse_artwork.png` — the rendered binary artwork.
- `bitverse_artwork.txt` — the underlying binary matrix.

## 🔮 Future Possibilities

BITVERSE is an evolving project. Potential directions include:

- Adaptive image processing and density control.
- Alternative dithering algorithms.
- Custom typography and color palettes.
- Radial and geometric binary reconstruction.
- Additional export formats and creative rendering modes.

## 🤝 Contributing

Suggestions, improvements, and experimentation are welcome.

If you have an idea that could make binary art more interesting, feel free to open an issue or submit a pull request.

---

**BITVERSE — Where images become bits.**
