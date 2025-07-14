# Smart Research Assistant

<div align="center">

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.1+-blue.svg)](https://flask.palletsprojects.com)
[![Langchain](https://img.shields.io/badge/Langchain-3.0+-green.svg)](https://www.langchain.com/)

**Contact**: [degisew.mengist21@gmail.com](mailto:degisew.mengist21@gmail.com) | [LinkedIn](https://linkedin.com/in/degisew-mengist)

</div>

## Overview

An AI-powered full-stack web app that helps startup founders, investors, and professionals quickly research a company and prepare for meetings.

**Key Features**:

- Company search using Tavily

- Summary generation using large language models

- Team background if available in public sources

- Market & competitor insights

- Auto-generated smart questions for founders or investors

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Architecture](#architecture)

## Setup

<details>
<summary><strong>Show Setup Details</strong></summary>

### Prerequisites

- Python 3.10+
- uv 0.7+
- Langchain 3+
- Git 2.30+

### Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/degisew/smart_research_assistant.git
   cd event_ticksmart_research_assistant
   ```

2. **Configure Environment**:

   ```bash
   Create a .env file with-in your root project directory and store secure values.
   ```

   Example `.env`:

   ```bash
   # API Keys
    TAVILY_API_KEY=your_key
    GROQ_API_KEY=your_key
   ```

   - **Local Development**:

     ```bash
      # lInstall uv
      curl -Ls https://astral.sh/uv/install.sh | sh

      # If you have pipx installed n your system,
      pipx install uv

      # create virtual environment
      uv venv       # Creates a virtual environment
      uv pip sync   # Installs dependencies from pyproject.toml

      uv run main.py # run the flask app
     ```

   **Access**: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

</details>

## Architecture

**Tech Stack**:
Python, Flask, Langchain, Groq

## License

MIT License. See [LICENSE](LICENSE).

<div align="center">

**⭐ Star this repo if you found it useful!**

Built by [Degisew Mengist](https://github.com/degisew)

[⬆ Back to Top](#smart-research-assistant)

</div>
