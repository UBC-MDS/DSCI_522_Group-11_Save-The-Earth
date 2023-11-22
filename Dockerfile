# Author: Jing Wen, Tony Shum, Weilin Han, Aishwarya Nadimpally
FROM quay.io/jupyter/minimal-notebook:2023-11-19

RUN conda install -y \  
    python=3.11.* \
    pip \
    ipykernel=6.26.0 \
    nb_conda_kernels \
    altair=5.1.2 \
    scipy \
    matplotlib>=3.2.2 \
    scikit-learn>=1.3.1 \
    requests>=2.24.0 \
    graphviz \
    python-graphviz \
    eli5 \
    shap 

RUN pip install \
    mglearn \
    psutil>=5.7.2
