# Apply Job Claw

A personal AI assistant that automates job applications via Telegram bot, using LLM-powered form filling and browser automation.

## Overview

Apply Job Claw is an intelligent desktop application that helps you automate the job application process. It uses AI to fill out job application forms, handles login flows, and communicates with you via Telegram when it needs your input (like OTP codes or custom questions).

## Features

- 🤖 **AI-Powered Form Filling**: Uses LLM to intelligently fill job application forms
- 📱 **Telegram Integration**: Interact with the assistant via Telegram bot
- 🌐 **Browser Automation**: Automatically navigates and fills forms using Playwright
- 📄 **Resume Parsing**: Automatically extracts information from your resume
- 🔐 **Login Handling**: Manages login flows and OTP verification
- 📊 **Application Tracking**: Tracks all your job applications
- 🧪 **Comprehensive Testing**: BDD tests with scenario-based testing

## Architecture

The project follows Clean Architecture principles with:

- **Domain Layer**: Core business logic, interfaces, and models
- **Application Layer**: Use cases and services
- **Infrastructure Layer**: External integrations (Telegram, Browser, LLM, Storage)

All components use interfaces for easy mocking and testing.

## Tech Stack

- **Language**: Python 3.11+
- **Browser Automation**: Playwright
- **Telegram Bot**: python-telegram-bot
- **LLM Client**: OpenAI SDK (compatible with OpenAI-compatible APIs)
- **Storage**: SQLite
- **Testing**: pytest, pytest-bdd
- **Code Quality**: black, ruff, mypy

## Project Structure

```
apply-job-claw/
├── src/
│   ├── domain/              # Core business logic (interfaces, models)
│   ├── application/         # Application services and use cases
│   ├── infrastructure/      # External integrations
│   ├── cli/                 # CLI entry point
│   └── utils/               # Utility modules
├── tests/
│   ├── unit/                # Unit tests
│   ├── integration/         # Integration tests
│   ├── e2e/                 # End-to-end tests (BDD)
│   └── mocks/               # Mock webpages for testing
├── .github/workflows/        # CI/CD pipelines
└── requirements.txt         # Dependencies
```

## Setup

### Prerequisites

- Python 3.11 or higher
- Git
- (Optional) Telegram Bot Token
- (Optional) OpenAI API key or compatible LLM API

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd apply-job-claw
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements-dev.txt
```

4. Install Playwright browsers:
```bash
playwright install chromium
```

### Development Setup

1. Install pre-commit hooks (optional but recommended):
```bash
pre-commit install
```

2. Run tests:
```bash
pytest
```

3. Run linting:
```bash
ruff check .
black --check .
mypy src/
```

## Usage

*Note: This is still in development. Usage instructions will be added as features are implemented.*

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run unit tests only
pytest tests/unit/

# Run with coverage
pytest --cov=src --cov-report=html
```

### Code Quality

The project uses:
- **black** for code formatting
- **ruff** for linting
- **mypy** for type checking

All checks run automatically in CI/CD.

### Commit Strategy

- Small, focused commits
- Each commit should include tests
- Commit message format: `type(scope): description`
  - Types: `feat`, `fix`, `test`, `refactor`, `docs`, `ci`, `chore`

## CI/CD

GitHub Actions automatically runs:
- Linting (ruff, black)
- Type checking (mypy)
- Unit tests
- Integration tests
- E2E tests
- Coverage reporting

All checks must pass before merging PRs.

## Contributing

1. Create a feature branch
2. Make small, focused commits with tests
3. Ensure all tests pass
4. Create a pull request

## License

MIT License

## Status

🚧 **In Development** - Phase 1 (Project Setup) completed. More phases coming soon!
