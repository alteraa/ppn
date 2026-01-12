FROM pytorch/pytorch:2.2.2-cuda12.1-cudnn8-devel

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    git \
    wget \
    ffmpeg \
    build-essential \
    cmake \
    ninja-build \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/OHF-Voice/piper1-gpl.git /workspace/piper1-gpl

COPY requirements.txt /workspace

RUN pip install -r /workspace/requirements.txt

WORKDIR /workspace/piper1-gpl

RUN pip install -e .[train] && \
    chmod +x ./build_monotonic_align.sh && \
    ./build_monotonic_align.sh && \
    python setup.py build_ext --inplace

CMD ["/bin/bash"]
