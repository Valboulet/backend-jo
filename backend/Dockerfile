FROM python:3.12.4-alpine

# Set the working directory
WORKDIR /app/backend-jo

# Prevent the creation of .pyc files and set Python to be non-buffered
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

# Install necessary dependencies
RUN apk update && apk add --no-cache bash netcat-openbsd

# Upgrade pip
RUN pip install --upgrade pip

# Copy the requirements file and install the packages
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy the entrypoint script and set the correct permissions
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x entrypoint.sh

# Copy the rest of the source code
COPY . .

# Set the entrypoint
ENTRYPOINT [ "./entrypoint.sh" ]