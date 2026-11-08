# Lab 11 – Build Your First GitHub Actions Workflow
#CSC 525

##  Workflow Configuration

Created a GitHub Actions workflow (`hello.yml`) to automate the execution of my Python program.

### Workflow Triggers
- **Push:** Runs automatically when code is pushed to the `main` branch.
- **workflow_dispatch:** Allows manual workflow execution.

### Execution Environment

| Configuration | Description |
|---|---|
| Runner | `ubuntu-latest` |
| Checkout | `actions/checkout@v4` |
| Environment Variable | `WHO_TO_GREET` |
| Execution Command | `python hello.py` |

### Expected Output

Hello GitHub Actions Student!
This program is running inside GitHub Actions. 

### 🤖 AI Usage Statement
AI was utilized to assist with understanding GitHub Actions, developing the Python script, configuring the YAML workflow, and formatting the README documentation. I reviewed the code and used it to complete the assignment.
