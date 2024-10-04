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
- An account with Unkey and your API ID

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
