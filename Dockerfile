# Author: Jing Wen, Tony Shum, Weilin Han, Aishwarya Nadimpally
FROM quay.io/jupyter/minimal-notebook:2023-11-19

RUN conda install -y \  
    python=3.11.* \
    pip=23.3.1 \
    ipykernel=6.26.0 \
    nb_conda_kernels=2.3.1 \
    altair=5.1.2 \
    scipy=1.11.3 \
    matplotlib>=3.2.2 \
    scikit-learn>=1.3.1 \
    requests>=2.24.0 \
    graphviz=9.0.0 \
    python-graphviz=0.20.1 \
    eli5=0.13.0 \
    shap=0.43.0 \
    click=8.1.7 \
    jupyter-book=0.15.1 \
    vl-convert-python=1.1.0 \
    make=4.2.1

RUN pip install \
    mglearn==0.2.0 \
    psutil>=5.7.2 \
    pytest==7.4.3
