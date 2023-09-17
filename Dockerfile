# Use an official PyTorch image as a parent image
FROM pytorch/pytorch:latest

# Set the working directory inside the container
WORKDIR /app

# Copy your application code into the container
COPY . /app

# Install any additional dependencies
RUN pip install -r requirements.txt

# Specify the command to run when the container starts
CMD ["python", "LLM_Sentiment_Analyser.py"]
