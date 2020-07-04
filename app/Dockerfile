FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . /app

RUN pip3 install -r requirements.txt
RUN python -c 'import pyppeteer; pyppeteer.chromium_downloader.download_chromium()'

#CMD ["/start-reload.sh"]
