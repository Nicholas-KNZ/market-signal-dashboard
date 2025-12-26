# Python 

FROM python:3.12-slim
WORKDIR /app

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy Python app
COPY app ./app


EXPOSE 8050

# Run Dash app
CMD ["python", "app/app.py"]
