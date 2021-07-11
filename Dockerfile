# Step 1 select default OS image
FROM alpine:3.7

RUN mkdir /app
WORKDIR /app

# Step 2 Setting up environment
RUN apk add --no-cache python3-dev && pip3 install --upgrade pip

# Step 3 Configure a software
COPY requirements.txt .


RUN pip3 install -r requirements.txt

# Copying project files
COPY ["MongoDB.py", "main.py", "/app/"]

# Exposing an internal port
EXPOSE 5001


# Step 4 set default commands
ENTRYPOINT [ "python3" ] # Default Command

# These commands will be replaced if user provides any command by himself
CMD ["main.py"]
