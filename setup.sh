#!/bin/bash

# --------------------------------------------------------
# FinSight Agent Setup Script
# --------------------------------------------------------

echo "🚀 Setting up FinSight Agent environment..."

# 1️⃣ Create a Python virtual environment (optional but recommended)
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# 2️⃣ Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# 3️⃣ Install Python dependencies from requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "❌ requirements.txt not found! Please create it before running this script."
    exit 1
fi

# 4️⃣ Install Playwright browsers
echo "Installing Playwright browsers..."
playwright install

# 5️⃣ Download NLTK resources
echo "Downloading required NLTK resources..."
python - <<EOF
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger_eng")
EOF

echo "✅ Setup complete! You can now run the app with:"
echo "streamlit run main.py"
