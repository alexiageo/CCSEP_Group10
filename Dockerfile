FROM ubuntu:18.04

# Update and install system deps
RUN apt-get update && apt-get install -y python3 python3-pip curl gconf-service libgbm1 libasound2 libatk1.0-0 libatk-bridge2.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m secure_programming
WORKDIR /home/secure_programming

COPY cache_hack/ vulnerable_app/
WORKDIR vulnerable_app/
RUN chmod +x boot.sh

RUN pip3 install -r requirements.txt

RUN chown -R secure_programming:secure_programming /home/secure_programming/vulnerable_app

USER secure_programming

ENV FLASK_APP app.py
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
USER secure_programming
EXPOSE 8000
ENTRYPOINT ["./boot.sh"]
