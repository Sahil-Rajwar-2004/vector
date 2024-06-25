#!/usr/bin/python3

# If you are using Linux or macOS 
# this file can automatically install this lib on your system
# or If you are on Windows then run the install.ps file
# cause I don't have a PyPi account

echo "Initiating the installation process..."

if pip show vector > /dev/null 2>&1; then
    echo "'vector' library is already installed."
    read -p "Do you want to uninstall the existing 'vector' library? (yes/no): " response
    if [[ "$response" =~ ^[Yy][Ee][Ss]$ || "$response" =~ ^[Yy]$ ]]; then
        echo "Uninstalling the existing 'vector' library..."
        pip uninstall -y vector
    else
        echo "Exiting without reinstalling."
        exit 0
    fi
fi

cd /mnt/d/fun/vector || { echo "Directory not found!"; exit 1; }

echo "Creating dist folder..."
mkdir -p dist

if [ ! -f setup.py ]; then
    echo "setup.py not found! Exiting"
    exit 1
fi

echo "Creating source distribution and wheel..."
python3 setup.py sdist bdist_wheel

if [ "$(ls -A dist)" ]; then
    echo "Distribution packages created successfully"
else
    echo "Failed to create distribution packages! Exiting"
    exit 1
fi

echo "Installing the library..."
pip install dist/*.whl

if python3 -c "import vector" &> /dev/null; then
    echo "Library installed successfully"
else
    echo "Failed to install the library! Exiting"
    exit 1
fi

echo "Installation process completed"

