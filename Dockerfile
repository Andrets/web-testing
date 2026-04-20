FROM ubuntu:22.04

#Installing basic dependencies
RUN apt-get update && apt-get install -y \
    ca-certificates \
    gnupg2 \
    && apt-get update && apt-get install -y \
    wget \
    unzip \
    python3-pip \
    python3-venv \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxi6 \
    libxtst6 \
    libgtk-3-0 \
    curl \
    openjdk-11-jre-headless \
    xvfb \
    libasound2 \
    libgbm1 \
    libatk-bridge2.0-0 \
    libx11-xcb1 \
    xdg-utils \
    fonts-liberation \
    --no-install-recommends \
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

# Установка Chrome и ChromeDriver
RUN echo "Installing Chrome + ChromeDriver" && \
    CHROME_VERSION=139.0.7258.66 && \
    wget -q https://storage.googleapis.com/chrome-for-testing-public/${CHROME_VERSION}/linux64/chrome-linux64.zip && \
    wget -q https://storage.googleapis.com/chrome-for-testing-public/${CHROME_VERSION}/linux64/chromedriver-linux64.zip && \
    unzip chrome-linux64.zip && \
    unzip chromedriver-linux64.zip && \
    mv chrome-linux64 /opt/chrome && \
    mv chromedriver-linux64/chromedriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver

#Installing Edge
RUN wget -q "https://packages.microsoft.com/repos/edge/pool/main/m/microsoft-edge-stable/microsoft-edge-stable_138.0.3351.121-1_amd64.deb" && \
    dpkg -i microsoft-edge-stable_138.0.3351.121-1_amd64.deb || apt-get -f install -y && \
    rm microsoft-edge-stable_138.0.3351.121-1_amd64.deb

#Installing EdgeDriver
RUN wget -q "https://msedgedriver.microsoft.com/138.0.3351.121/edgedriver_linux64.zip" && \
    unzip edgedriver_linux64.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/msedgedriver && \
    rm edgedriver_linux64.zip

#Checking the Edge installation
RUN which microsoft-edge-stable || echo "Microsoft Edge is not installed!"

#Installing Firefox and GeckoDriver
RUN apt-get update && apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:mozillateam/ppa && \
    echo 'Package: *' > /etc/apt/preferences.d/mozilla && \
    echo 'Pin: release o=LP-PPA-mozillateam' >> /etc/apt/preferences.d/mozilla && \
    echo 'Pin-Priority: 1001' >> /etc/apt/preferences.d/mozilla && \
    apt-get update && apt-get install -y firefox

RUN wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.36.0/geckodriver-v0.36.0-linux64.tar.gz" && \
    tar -xzf geckodriver-v0.36.0-linux64.tar.gz -C /usr/local/bin/ && \
    chmod +x /usr/local/bin/geckodriver && \
    rm geckodriver-v0.36.0-linux64.tar.gz

#Настраиваем переменные окружения для headless режима
ENV DISPLAY=:99

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
