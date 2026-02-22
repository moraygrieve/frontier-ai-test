# Frontier AI Test

A Python project for experimenting with various frontier AI models, with Docker utilities and automated testing using PySys. At the moment this only includes OpenAI though addition of Anthropic is WIP.

## Features
- **Automated testing**: PySys-based test suite for API workflows
- **Docker utilities**: Reusable shells for non-interactive, interactive, and asynchronous container execution

## Project Structure
```
frontier-ai-test/
├── README.md
├── pysysproject.xml
├── src
│   └── utils
│       └── docker.py         # Docker shell helpers
└── test
    ├── docker_001            # Non-interactive shell tests
    ├── docker_002            # Interactive shell tests
    ├── docker_003            # Asynchronous shell tests
    ├── docker_004            # Interactive shell with whitelisted commands
    ├── openai_001            # Basic OpenAI response test
    ├── openai_002            # Function-calling/tool-use test
    └── openai_003            # YAML-driven prompt test
```

## Requirements
- Python 3.11 (matches `pysysproject.xml`)
- Python packages:
  - `openai`
  - `pysys`
  - `docker`
  - `PyYAML`

## Setup
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd frontier-ai-test
   ```

2. **Install dependencies:**
   ```bash
   pip install openai pysys docker PyYAML
   ```

3. **Set up OpenAI API key:**
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

4. Ensure Docker is installed and running (required for the Docker tests).

## Usage

### Running Tests

- Run all tests:
  ```bash
  pysys run
  ```

- Run a specific test:
  ```bash
  pysys run docker_001
  pysys run docker_002
  pysys run docker_003
  pysys run docker_004
  pysys run openai_001
  pysys run openai_002
  pysys run openai_003
  ```

## How it Works

The project uses PySys for automated testing:
- Validates OpenAI API and Docker responses
- Asserts expected outcomes
- Provides detailed logging and output capture
- Supports multiple test modes and configurations

PySys configuration is defined in `pysysproject.xml` (adds `./src` to the path). Docker utilities live in `src/utils/docker.py` and provide:
- `DockerNonInteractiveShell`
- `DockerInteractiveShell`
- `DockerAsynchronousShell`

## API Dependencies
- **OpenAI API**: Requires `OPENAI_API_KEY` in the environment for OpenAI tests
- **Docker**: Required and must be running to execute Docker tests

## License
MIT
