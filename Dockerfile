FROM python3:8

COPY requirements.txt .

RUN pip3 install -r requirements.txt

WORKDIR /app

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]