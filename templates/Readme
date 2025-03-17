# Command Line Arguments (CLI Args) & Environment Variables (Env Vars) in Python

This README provides an overview of **Command Line Arguments (CLI Args)** and **Environment Variables (Env Vars)** in Python with real-time examples. These concepts are especially useful for DevOps engineers to automate and configure deployments securely.

## 1. Command Line Arguments (CLI Args)

Command-line arguments allow users to pass information to a script when it is executed from the command line (or terminal). These arguments are typically used to provide parameters or options that influence the program's behavior.

In Python, command-line arguments can be accessed using the `sys.argv` list, which is part of the `sys` module.

### Python Example: `deploy.py`

```python
import sys

def deploy_app(environment):
    print(f"Deploying application to {environment} environment")

if __name__ == "__main__":
    # Command-line argument to specify the environment (prod, dev, etc.)
    if len(sys.argv) != 2:
        print("Usage: python deploy.py <environment>")
    else:
        environment = sys.argv[1]
        deploy_app(environment)
```

### How to Use

1. Save the script as `deploy.py`.
2. Run the script from the command line, passing the environment argument (e.g., prod, dev):

```sh
python deploy.py prod
```

#### Output:
```
Deploying application to prod environment
```

In this example, the script takes one command-line argument to specify the environment (e.g., prod, dev). The argument is accessed using `sys.argv[1]`.

---

## 2. Environment Variables (Env Vars)

Environment variables are variables set outside of the program in the operating system or shell environment. They are commonly used to store sensitive information, configuration settings, or credentials.

In Python, you can access environment variables using the `os.environ` dictionary from the `os` module.

### Python Example: `config.py`

```python
import os

def get_db_connection():
    db_host = os.getenv('DB_HOST', 'localhost')  # Get environment variable or use default
    db_user = os.getenv('DB_USER', 'admin')
    db_password = os.getenv('DB_PASSWORD', 'secret')
    
    print(f"Connecting to database at {db_host} with user {db_user}")

if __name__ == "__main__":
    get_db_connection()
```

### Setting Environment Variables

To set environment variables in your shell:

#### For Linux/macOS:
```sh
export DB_HOST=192.168.1.100
export DB_USER=dev_user
export DB_PASSWORD=dev_pass
```

#### For Windows (Command Prompt):
```sh
set DB_HOST=192.168.1.100
set DB_USER=dev_user
set DB_PASSWORD=dev_pass
```

### How to Use

1. Set the environment variables in your terminal.
2. Run the script `config.py`:

```sh
python config.py
```

#### Output:
```
Connecting to database at 192.168.1.100 with user dev_user
```

In this example, environment variables store sensitive information like database credentials. The `os.getenv()` method retrieves these values securely. If the environment variables are not set, it will fall back to default values (`localhost`, `admin`, `secret`).

---

## Real-Time Use Cases for a DevOps Engineer

### 1. Command-Line Arguments:
- **Deployment Scripts:** Command-line arguments allow specifying which environment to deploy to (e.g., prod, staging, dev).
- **CI/CD Pipelines:** You may pass different configuration options or flags when triggering a script (e.g., `--rollback`, `--force`).

### 2. Environment Variables:
- **Storing Sensitive Information:** Environment variables are commonly used to store sensitive credentials such as API keys, database passwords, and other secrets to avoid hardcoding them in the code.
- **Configurable Settings:** Configuration details like database host, API endpoints, and environment-specific values can be controlled through environment variables, allowing flexibility across different environments (e.g., dev, staging, production).

These concepts are integral to automating tasks in a DevOps pipeline, ensuring secure and configurable deployments.
