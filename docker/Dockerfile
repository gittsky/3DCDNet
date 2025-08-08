FROM nvidia/cuda:11.8.0-devel-ubuntu22.04
ARG DEBIAN_FRONTEND=noninteractive

# This Dockerfile adds a non-root 'vscode' user with sudo access. However, for Linux,
ARG USERNAME=vscode
ARG USER_UID=610215912
ARG USER_GID=610200513

# Configure apt and install packages
RUN apt-get clean && apt-get update \
    && apt-get -y install --no-install-recommends apt-utils dialog 2>&1 \
    #
    # Verify git
    && apt-get -y install git \
    #
    && groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Update and install debian stuff
RUN apt-get update && apt-get -y install \
vim \
python-is-python3 \
python3-pip \
wget \
unzip \
libgl1-mesa-dev \
&& rm -rf /var/lib/apt/lists/*

USER $USERNAME

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Run Jupyter Notebook when the container launches
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

# this installs all files specified in the requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY requirements_3dcdnet.txt .
RUN pip install -r requirements_3dcdnet.txt

# COPY requirements_dc3dcd.txt .
# RUN pip install -r requirements_dc3dcd.txt