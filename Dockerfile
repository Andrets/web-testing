FROM ubuntu:latest

#Installing basic dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-11-jdk \
    python3 \
    python3-pip \
    python3-venv \
    wget \
    ca-certificates \
    curl \
    && rm -rf /var/lib/apt/lists/*

#Setting up JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

#Creating a virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

#Copy requirements.txt
COPY requirements.txt /tmp/requirements.txt

#Installing Python dependencies
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

# Install the allure cli
RUN wget -qO allure.tar.gz https://github.com/allure-framework/allure2/releases/download/2.17.2/allure-2.17.2.tgz \
    && tar -xzf allure.tar.gz -C /opt/ \
    && ln -s /opt/allure-2.17.2/bin/allure /usr/bin/allure \
    && rm allure.tar.gz

#Adding Allure to the PATH
ENV PATH="/opt/allure/bin:${PATH}"

WORKDIR /app

#Копируем файлы проекта
COPY . /app/
