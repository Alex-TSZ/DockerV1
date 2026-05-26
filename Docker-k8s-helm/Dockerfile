FROM python:3.12.6

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#Not needed but is nice to have
EXPOSE 8000

CMD ["uvicorn", "aiContainer1Py:app", "--host", "0.0.0.0", "--port", "8000"]