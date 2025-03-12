# Use latest Python image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy all bot files to container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port (if needed for webhooks or API)
EXPOSE 80

# Run the bot
CMD ["python3", "main.py"]
