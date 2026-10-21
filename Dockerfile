FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY pyproject.toml README.md ./
COPY src/ src/

RUN pip install --no-cache-dir --no-deps .

EXPOSE 8000

CMD ["uvicorn", "industrial_vision.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
