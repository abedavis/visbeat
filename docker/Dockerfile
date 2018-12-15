ARG BASE_CONTAINER=jupyter/base-notebook
FROM $BASE_CONTAINER

USER root

# Install all OS dependencies for fully functional notebook server
# also include ffmpeg
RUN apt-get update && apt-get install -yq --no-install-recommends \
    build-essential \
    emacs \
    ffmpeg \
    git \
    inkscape \
    jed \
    libsm6 \
    libxext-dev \
    libxrender1 \
    lmodern \
    netcat \
    pandoc \
    python-dev \
    texlive-fonts-extra \
    texlive-fonts-recommended \
    texlive-generic-recommended \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-xetex \
    unzip \
    nano \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a Python 2.x environment using conda including at least the ipython kernel
# and the kernda utility.
RUN conda create --quiet --yes -p $CONDA_DIR/envs/python2 python=2.7 ipython ipykernel kernda && \
    conda clean -tipsy

# Create a global kernelspec in the image and modify it so that it properly activates
# the python2 conda environment.
RUN $CONDA_DIR/envs/python2/bin/python -m ipykernel install && \
    $CONDA_DIR/envs/python2/bin/kernda -o -y /usr/local/share/jupyter/kernels/python2/kernel.json && \
    . activate python2 && \
    $CONDA_DIR/envs/python2/bin/pip install numpy \
    scipy \
    librosa \
    imageio \
    moviepy \
    youtube-dl \
    requests \
    bs4 \
    matplotlib \
    visbeat



RUN git clone https://github.com/abedavis/visbeat.git

RUN conda install -n python2 -y opencv

RUN chown -R $NB_UID:$NB_UID ./visbeat
RUN chmod 755 ./visbeat


USER $NB_UID

RUN $CONDA_DIR/envs/python2/bin/python -c "import imageio; imageio.plugins.ffmpeg.download()"

WORKDIR $HOME/visbeat/examples/