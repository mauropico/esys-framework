
# Docker Container for Particle Simulation with esys-particle

This Docker container is configured to support applications that utilize the `esys-particle` framework, specifically tailored for simulations involving particles. The Dockerfile provided sets up a ready-to-use environment with the necessary tools and libraries, ensuring a consistent runtime for development and production needs.

## Features

- **Base Image**: Uses `muro230/esys-particle` as the primary image, which is preconfigured with the `esys-particle` simulation software.
- **Python Support**: Comes with Python 3 and pip installed, allowing for the use of Python scripts and additional libraries.
- **HDF5 Support**: Includes the `h5py` library, enabling support for handling HDF5 files that are commonly used in large scientific computing projects.

## Configuration Details

- **Working Directory**: The working directory within the container is set to `/usr/local/bin`, a common directory for executable programs.
- **Software Installation**:
  - Updates the package list and installs Python 3 pip, facilitating the management and installation of Python packages.
  - Installs `h5py` using pip, which is essential for working with HDF5 data formats within Python applications.
- **Startup Command**: By default, the container executes `sh main/run.sh` upon startup. This script should be the entry point of your application, handling the initialization and execution of your simulation tasks.

## Usage

To build and run this Docker container, ensure you have Docker installed on your system and follow these steps. You may need to use `sudo`:

1. **Build the Docker Image**:
   ```bash
   docker build -t esys-particle .
   ```

2. **Run the Container**:
   ```bash
   docker run -ti -e OMPI_ALLOW_RUN_AS_ROOT=1 -e OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1 -v ${PWD}:/simulation esys-particle
   ```

Ensure that the `main/run.sh` script is properly configured to execute your specific simulation tasks. Modify the script as necessary to fit your project's requirements.

## Customization

You can modify the Dockerfile to include additional dependencies, change the base image, or adjust the startup script according to your needs. This flexibility allows the Docker container to be adapted for various simulation scenarios using the esys-particle framework.

