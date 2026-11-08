
# Name displayed in GitHub Actions
name: Hello World with Python

# Events that trigger the workflow
on:
 # Run when code is pushed to main
  push:
    branches:
      - main
# Allow manual execution
  workflow_dispatch:

# Define the jobs
jobs:
  hello-python:
    name: Run the Python Hello World program
    # Operating system for the runner
    runs-on: ubuntu-latest

    # Download repository files 
    steps:
      - name: Check out the repository
        uses: actions/checkout@v4

      # Execute the Python program
      - name: Run the Python program
        env:
          WHO_TO_GREET: 'GitHub Actions Student'
          run: python hello.py
