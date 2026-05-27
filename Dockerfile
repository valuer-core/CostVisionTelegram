FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create a directory for persistent logs
RUN mkdir -p logs

# Copy the main bot script
COPY bot.py .

# Define the command to run the bot
CMD ["python", "bot.py"]
