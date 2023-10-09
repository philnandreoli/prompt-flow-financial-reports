# syntax=docker/dockerfile:1
FROM docker.io/continuumio/miniconda3:latest

WORKDIR /

COPY ./flow /flow

# create conda environment
RUN conda create -n promptflow-serve python=3.9.16 pip=23.0.1 -q -y && \
    conda run -n promptflow-serve \
    pip install -r /flow/requirements.txt && \
    conda run -n promptflow-serve pip install keyrings.alt && \
    conda run -n promptflow-serve pip cache purge && \
    conda clean -a -y


EXPOSE 8080

COPY ./connections/* /connections/
COPY ./start.sh /
CMD ["bash", "./start.sh"]
