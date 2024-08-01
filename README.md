# Python Project

Template for miscellaneous projects

## Project Structure
While there is no single optimal project structure, I typically prefer a domain-driven layout.

```
├── python_template  # name of your module
│   ├── <domain or entity>
│   │   ├── controller.py  # business logic
│   │   ├── schemas.py  # pydantic models
│   │   ├── models.py  # db models
│   │   ├── config.py  # local configs
│   │   ├── constants.py
│   │   ├── exceptions.py  # domain-specific exceptions
│   │   ├── service.py  # calls to external APIs or databases
│   │   └── utils.py
│   ├── config.py  # global configs
│   ├── exceptions.py  # global exceptions
│   └── __main__.py # app entrypoint
├── tests/  # Unit tests
├── .env
├── .gitignore
└── pyproject.toml  # Poetry and linter configuration
```

## Running the Application

### Prerequisites

- [poetry](https://python-poetry.org/docs/#installation) - all-in one tool to handle dependencies and virtual environments
- _[pre-commit](https://pre-commit.com) (Optional)_ - useful for automating various formatting and linting processed as git hooks.

### Run the program

Poetry will manage the environment and install dependencies for us. Once installed, all you have to do is run the program with `poetry run`.

```bash
# Install dependencies
poetry install

# Run program.
poetry run python -m python_template
```

### Linting and Formatting

We can easily run our static code analysis tools with `pre-commit`.

```bash
# Install hooks
pre-commit install

# Optionally run the hooks on the entire codebase
pre-commit run --all-files
```
