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
    libgtk-3-common \
    libpulse0 \
    libgstreamer1.0-0 \
    libgstreamer-plugins-base1.0-0 \
    libgconf-2-4 \
    libuuid1 \
    libfreetype6 \
    curl \
    openjdk-11-jre-headless \
    xvfb \
    libasound2 \
    libgbm1 \
    libatk-bridge2.0-0 \
    libx11-xcb1 \
    xdg-utils \
    fonts-liberation \
    libfontconfig1 \
    fontconfig-config \
    libxrender1 \
    libxt6 \
    libdbus-glib-1-2 \
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

# Установка Chrome
RUN wget -qO- https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/google.gpg] https://dl.google.com/linux/chrome/deb/ stable main" \
    > /etc/apt/sources.list.d/google.list && \
    apt-get update && apt-get install -y google-chrome-stable

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

#Installing Firefox
RUN apt-get update && apt-get install -y xz-utils curl && \
    curl -L "https://download.mozilla.org/?product=firefox-latest&os=linux64&lang=en-US" -o firefox.tar.xz && \
    tar -xf firefox.tar.xz -C /opt/ && \
    ln -s /opt/firefox/firefox /usr/bin/firefox && \
    rm firefox.tar.xz

RUN GECKODRIVER_VER=$(curl -s https://github.com/mozilla/geckodriver/releases/download/v0.36.0/geckodriver-v0.36.0-linux64.tar.gz | grep 'tag_name' | cut -d\" -f4) && \
    wget -q "https://github.com/mozilla/geckodriver/releases/download/v0.36.0/geckodriver-v0.36.0-linux64.tar.gz" && \
    tar -xzf geckodriver-v0.36.0-linux64.tar.gz -C /usr/local/bin/ && \
    chmod +x /usr/local/bin/geckodriver && \
    rm geckodriver-v0.36.0-linux64.tar.gz

# DEBUG browsers
RUN echo "Checking browsers..." && \
    which firefox || echo "Firefox not found" && \
    firefox --version || echo "Firefox cannot run" && \
    which microsoft-edge || echo "Edge not found" && \
    which microsoft-edge-stable || echo "Edge-stable not found" && \
    microsoft-edge-stable --version || echo "Edge cannot run"

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
