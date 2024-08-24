# Code.AI

Welcome to Code.AI! This project includes both frontend and backend components designed to support multiple programming languages with various tools.

## Frontend Server Setup (Code.aione)

1. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install the Required Packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Create and Configure `client_secret.json` for Google OAuth:**

    Follow the [Google OAuth Quickstart Guide](https://developers.google.com/identity/protocols/oauth2) to obtain your `client_secret.json`. Place the `client_secret.json` file in the project root directory.

4. **Run the Frontend Server:**

    ```bash
    python app.py
    ```

    The frontend server will run on [http://localhost:5000](http://localhost:5000) by default.

## Backend Server Setup (AI_VGCODE)

1. **Navigate to the Backend Project Directory:**

    ```bash
    cd path/to/AI_VGCODE
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the Required Packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Backend Server:**

    ```bash
    python main.py
    ```

    The backend server will run on [http://localhost:5001](http://localhost:5001) by default.

## Usage

- Start the frontend server and backend server simultaneously in separate terminal windows or tabs.
- Access the application via the frontend server URL: [http://localhost:5000](http://localhost:5000).
- Authenticate using Google OAuth to access the full functionality.
- Interact with the tools provided by the frontend interface.

## Configuration

- **Ports:** By default, the frontend runs on port 5000 and the backend on port 5001. You can change these in the `config.py` files of each project if necessary.
- **Languages Supported:** The tools support C++, C, Python, and Java. Configure language-specific settings in the respective tool configurations.

## Contribution

If you wish to contribute to the project, please fork the repository and submit a pull request with your changes. Ensure that you follow the coding standards and include tests for new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or issues, please reach out to [shubhvora03@gmail.com](mailto:shubhvora03@gmail.com).

Thank you for using Code.AI!
