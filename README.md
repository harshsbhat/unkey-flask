# Flask API with Unkey Key Verification

This is a simple Flask application that demonstrates how to implement API key verification using the Unkey service. The application has both public and protected routes, with the protected route requiring a valid API key.

## Features

- **Public Route**: Accessible without any authentication.
- **Protected Route**: Requires a valid API key to access.
- **Middleware for Key Verification**: Utilizes a decorator to enforce key verification on protected routes.

## Prerequisites

- Python 3.x
- Flask
- Requests library
- An account with Unkey and your API ID and ROOT Key

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/harshsbhat/unkey-flask.git
   cd unkey-flask
```

2. Set up a virtual environment (optional but recommended): :
   ```
   python3 -m venv venv   # For Linux/macOS
   source venv/bin/activate  # For Linux/macOS

   python -m venv venv   # For Windows
   venv\Scripts\activate  # For Windows
```

3. Set up your environment variables: Create a .env file in the project root and add the following variables

```
   cp .env.example .env
```

Get the  Unkey API ID and Unkey rootkey from [unkey dashboard](http://app.unkey.com/)

```
UNKEY_API_ID=your_unkey_api_id
UNKEY_ROOT_KEY=your_unkey_root_key
```

4. Install the required dependencies:

```
pip install -r requirements.txt
```

5. Run the Flask application::

```
python3 src/main.py


## Usage