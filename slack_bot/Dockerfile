# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
# (a text files with all the libraries you want to install)
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
#RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

#RUN pip install psycopg2-binary

# Run app.py when the container launches
CMD ["python", "slack_bot.py"]
