# Use an official PyTorch image as a parent image
FROM pytorch/pytorch:latest

# Set the working directory inside the container
WORKDIR /app/nlp

# Copy your application code into the container
COPY . /app/nlp/

# Install any additional dependencies
RUN pip install -r requirements.txt

# Specify the command to run when the container starts
CMD ["python", "./BERT_Sentiment_Analyser/LLM_Sentiment_Analyser.py"]
