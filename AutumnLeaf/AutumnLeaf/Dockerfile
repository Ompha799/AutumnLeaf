FROM python

RUN pip3 install requests
WORKDIR "/app"
COPY app.py .
ENV site=http://api.open-notify.org/astros.json
ENV times=5

CMD ["python3", "app.py"]
