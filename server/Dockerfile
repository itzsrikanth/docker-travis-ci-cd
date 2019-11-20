FROM python:3.7-alpine
ADD src /src
WORKDIR /src
RUN pip install --upgrade pip && \
    pip3 install -r requirements.txt
EXPOSE 8080
CMD ["python3", "app.py"]
