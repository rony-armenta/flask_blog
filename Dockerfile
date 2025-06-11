FROM python:3.13.4-alpine3.22
WORKDIR /sysx/app/
COPY requirements.txt .
RUN pip install flask --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "flaskblog.py"]