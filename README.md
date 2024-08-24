# Code.AI

**Code.AI** is a robust project that includes a suite of tools for code generation, summarization, debugging, and commenting. It is designed to work with multiple programming languages and utilizes advanced AI for enhanced code management. The project consists of two main components: a frontend and a backend server, both of which need to be run simultaneously on different ports.

## Features

- **Code Generator**: Generates code snippets based on user inputs.
- **Code Summarizer**: Provides summaries of code to understand functionality quickly.
- **Code Debugger**: Identifies and helps debug issues in the code.
- **Code Commenter**: Automatically adds comments to code to improve readability.
- **Language Support**: Includes support for C++, C, Python, and Java.
- **Google OAuth Authentication**: Secures the application with Google OAuth.

## Project Structure

- **`code.aione`**: Frontend Flask server that handles user interactions and provides a web interface.
- **`AI_VGCODE`**: Backend Flask server that manages AI operations and processes.

## Setup and Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- `pip`
- `virtualenv` (optional but recommended)

### Frontend Server Setup (`code.aione`)

1. **Navigate to the frontend project directory:**

   ```bash
   cd path/to/code.aione
