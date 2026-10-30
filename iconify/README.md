# iconify

Convert PNG and JPEG images into multi-resolution ICO files.

## Installation
```
git clone https://github.com/emiHuy/toolbox.git
cd toolbox/iconify
```

### 1. Create a virtual environment
```
python -m venv .venv
```

### 2. Activate the virtual environment

**Windows (PowerShell):**
```
.venv\Scripts\activate
```

**macOS/Linux:**
```
source .venv/bin/activate
```

### 3. Install `iconify`
```
python -m pip install -e .
```

## Usage
```
iconify image.png
iconify image.png -o favicon.ico
iconify image.png --sizes 16,32,48,256
iconify image.png --crop
iconify --help
```

## PATH (Optional)
To run iconify without activating the virtual environment, add its executable directory to your system PATH:
- Windows: `.venv\Scripts`
- Linux/macOS: `.venv/bin`

The command can then be run from any directory:
```
iconify image.png
```