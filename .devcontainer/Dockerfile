# Usar a imagem base do Ubuntu
FROM ubuntu:latest

# Definir modo não interativo para evitar prompts
ENV DEBIAN_FRONTEND=noninteractive

# Atualizar a lista de pacotes e instalar dependências essenciais
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    curl \
    gnupg2 \
    lsb-release \
    ca-certificates \
    apt-transport-https \
    wget \
    build-essential \
    sudo \
    software-properties-common \
    git

# Instalar o Node.js 22 corretamente
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get install -y nodejs && \
    apt-mark hold nodejs

# Verificar instalação do Node.js e NPM
RUN node -v && npm -v

# Instalar Python 3 e pacotes adicionais
RUN apt-get install -y python3 python3-pip python3-venv && \
    python3 --version && pip3 --version

# Adicionar repositório para GCC 14 e instalar o GCC 14
RUN add-apt-repository ppa:ubuntu-toolchain-r/test -y && \
    apt-get update && \
    apt-get install -y gcc-14 g++-14 && \
    update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-14 100 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-14 100

# Verificar instalação do GCC
RUN gcc --version && g++ --version

# Definir a pasta de trabalho
WORKDIR /workspace

# Definir comandos padrão
CMD [ "bash" ]
