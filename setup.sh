

#!/bin/bash
set -euo pipefail
##Script for installing all three interpreters.
# Update system and install dependencies
sudo apt-get update -qq
sudo apt-get install -qq -y software-properties-common wget

# Install Python 3
if ! command -v python3 &> /dev/null; then
    echo "Installing Python 3..."
    sudo apt-get install -qq -y python3 python3-pip
else
    echo "Python 3 already installed"
fi

# Install PyPy3
if ! command -v pypy3 &> /dev/null; then
    echo "Installing PyPy3..."
    sudo add-apt-repository -y universe
    sudo apt-get update -qq
    sudo apt-get install -qq -y pypy3 libssl-dev
    sudo ln -sf /usr/bin/pypy3 /usr/local/bin/pypy3
else
    echo "PyPy3 already installed"
fi

# Install Jython dependencies (Java)
if ! command -v java &> /dev/null; then
    echo "Installing Java (Jython dependency)..."
    sudo apt-get install -qq -y openjdk-17-jdk
else
    echo "Java already installed"
fi

# Install Jython
JYTHON_VERSION="2.7.3"
JYTHON_DIR="/opt/jython"
if ! command -v jython &> /dev/null; then
    echo "Installing Jython ${JYTHON_VERSION}..."
    sudo mkdir -p "${JYTHON_DIR}"
    sudo wget -q "https://repo1.maven.org/maven2/org/python/jython-installer/${JYTHON_VERSION}/jython-installer-${JYTHON_VERSION}.jar" -O /tmp/jython_installer.jar
    sudo java -jar /tmp/jython_installer.jar -s -d "${JYTHON_DIR}" -t standard
    sudo ln -sf "${JYTHON_DIR}/bin/jython" /usr/local/bin/jython
    sudo rm /tmp/jython_installer.jar
else
    echo "Jython already installed"
fi

# Verify installations
echo -e "\nInstallation verification:"
echo "Python 3: $(python3 --version 2>&1) [$(which python3)]"
echo "PyPy3: $(pypy3 --version 2>&1) [$(which pypy3)]"
echo "Jython: $(jython --version 2>&1) [$(which jython)]"

echo -e "\nInstallation completed successfully!"