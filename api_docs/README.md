# NeuraMind AI API Documentation

This folder contains the API documentation for the NeuraMind AI backend.

## Files

- **openapi.yaml**: OpenAPI specification for the backend API.

## How to Use

1. Use an API client like Postman or Swagger UI to test the endpoints.
2. Import the `openapi.yaml` file into Swagger UI for an interactive API interface.

## Endpoints

### 1. Home Endpoint
- **URL**: `/`
- **Method**: GET
- **Description**: Returns a welcome message.

### 2. Route Calculation
- **URL**: `/route`
- **Method**: GET
- **Description**: Calculates a route between two locations.

### 3. Image Generation
- **URL**: `/generate-image`
- **Method**: GET
- **Description**: Generates an image based on a prompt.

## Notes

- Ensure the backend server is running on `http://localhost:5000` before testing the endpoints.
