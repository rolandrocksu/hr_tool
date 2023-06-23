# HR tool

[![Generic badge](https://img.shields.io/badge/version-1.0.0.-blue.svg)](https://shields.io/)


## Installation

```bash
# Clone the Project
git clone https://github.com/rolandrocksu/hr_tool.git

# Create the Virtual Env
cd hr_tool
python -m venv venv
source venv/bin/activate

# Install requirements
pip3 install -r requirements.txt
```

## Dependencies

> To use the make commands, you will need to have Docker installed on your machine.

### Install Docker:

* On Windows:
    * Download and install Docker Desktop from [here](https://www.docker.com/products/docker-desktop).
* On macOS:
    * Download and install Docker Desktop from [here](https://www.docker.com/products/docker-desktop).
* On Linux:
    * Follow the instructions for your distribution from [here](https://docs.docker.com/engine/install/).


## Run the server on local environment using `make` command

```bash
# run the web server on localhost:8000
make run  
```
