FROM python:3.12.2-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt  

RUN pip install flask-cors

RUN pip install scikit-learn==1.3.2

RUN pip install pandas 

EXPOSE 3001

CMD ["python", "main.py"]