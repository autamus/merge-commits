# Start from the latest alpine base image
FROM alpine

LABEL "com.github.actions.name"="Merge Commits"
LABEL "com.github.actions.description"="Output a list of commits in a branch/PR merge."
LABEL "com.github.actions.icon"="activity"
LABEL "com.github.actions.color"="blue"


# Set the Current Working Directory inside the container
WORKDIR /app

# Install required packages for building Binoc.
RUN apk add --no-cache \
    python3 \
    git

# Copy files to container
COPY *.py .

# Mark script as executable.
RUN chmod u+x merge-commits.py

# Command to run the executable
ENTRYPOINT ["python3", "/app/merge-comits.py"]