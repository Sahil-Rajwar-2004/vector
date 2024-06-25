# If you are using Window OS then
# this file can automatically install this lib on your system
# or If you are on Linux or macOS then run the install.sh file
# cause I don't have a PyPi account

Write-Host "Initiating the installation process..."

$libraryName = "vector"
$libraryVersion = "0.1.0"

$pythonPath = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $pythonPath) {
    Write-Host "Python is not installed on this system."
    exit 1
}

$pipPath = (Get-Command pip -ErrorAction SilentlyContinue).Source
if (-not $pipPath) {
    Write-Host "pip is not installed on this system."
    exit 1
}

$checkResult = & pip show $libraryName 2>&1

if ($checkResult -like "*Name: $libraryName*") {
    Write-Host "$libraryName is already installed."

    $userInput = Read-Host "Do you want to uninstall $libraryName and install version $libraryVersion? (yes/no)"
    if ($userInput -eq "yes") {
        & pip uninstall -y $libraryName
        if ($?) {
            Write-Host "$libraryName has been uninstalled."
        } else {
            Write-Host "Failed to uninstall $libraryName. Exiting."
            exit 1
        }
    } else {
        Write-Host "Installation of $libraryName version $libraryVersion declined."
        exit 0
    }
}

Write-Host "Creating source distribution package..."
& python setup.py sdist
if ($?) {
    Write-Host "Source distribution package created successfully."
} else {
    Write-Host "Failed to create source distribution package."
    exit 1
}

Write-Host "Installing $libraryName version $libraryVersion..."
& pip install .\dist\$libraryName-$libraryVersion.tar.gz
if ($?) {
    Write-Host "$libraryName version $libraryVersion installed successfully."
} else {
    Write-Host "Failed to install $libraryName version $libraryVersion."
}


