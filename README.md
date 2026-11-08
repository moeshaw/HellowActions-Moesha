
# Lab 11 – Build Your First GitHub Actions Workflow
csc 525
##  Workflow Configuration

Created a GitHub Actions workflow (`hello.yml`) to automate the execution of my Python program.

### Workflow Triggers
- **Push:** Automatically runs when changes are pushed to `main`.
- **workflow_dispatch:** Allows manual execution through GitHub Actions.

### Execution Environment

| Configuration | Description |
|---|---|
| Runner | `ubuntu-latest` |
| Checkout | `actions/checkout@v4` |
| Environment Variable | `WHO_TO_GREET` |
| Execution Command | `python hello.py` |

### Expected Output

```text
Hello GitHub Actions Student!
This program is running inside GitHub Actions.
```

### Workflow Result
The workflow runs my Python program and displays its output in the GitHub Actions logs.

---

## 📘 Part 5: Workflow Explanation

### 1. What is the purpose of the `on` section?
Defines when the workflow runs, such as when code is pushed to `main`.

### 2. What does `workflow_dispatch` do?
Allows me to manually start the workflow from the Actions tab. If it not included the workflow will still run but u wont be able to run manually 

### 3. What does `runs-on` specify?
Specifies the operating system used by the job. Mine uses `ubuntu-latest`.

### 4. Why is `actions/checkout` needed?
Checks out my repository so the runner can access my project files.

### 5. What does the language setup action do?
Installs or configures the programming language. Python is already available on my Ubuntu runner, so I did not need a separate setup action.

### 6. What is the difference between compiling and running a program?
Compiling converts source code into an executable format, while running executes the program. Python does not require a separate compilation step in my project.

### 7. Where can you see the program output?
1. Open my GitHub repository.
2. Select the **Actions** tab.
3. Choose **Hello World with Python**.
4. Select the specific workflow run.
5. Open the `hello-python` job.
6. Expand **Run the Python program** to view the execution logs.

### 8. What is the difference between a workflow, a job, and a step?
- **Workflow:** Contains the jobs and is triggered by events such as `push` and `workflow_dispatch`.
- **Job:** Contains the steps and runs on a runner, such as `ubuntu-latest`. Mine is named `hello-python`.
- **Step:** Performs an individual task. A step can use an action (`uses`), such as `actions/checkout@v4`, or execute a command (`run`), such as `python hello.py`.

**How they relate:**
- Events start the workflow.
- The workflow organizes the jobs.
- Jobs organize the steps.
- Steps use actions or run commands.

---

## 🤖 AI Usage Statement

AI was utilized to help me understand GitHub Actions, troubleshoot YAML errors, and improve my code and README documentation. I reviewed the suggestions and used them to complete my project.
