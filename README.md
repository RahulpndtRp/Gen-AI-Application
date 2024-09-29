
# FastAPI LLM Application

## Overview
This project is a **FastAPI** application designed to interact with multiple Large Language Models (LLMs) like **OpenAI**, **LLaMA**, and embedding models. The application supports multi-user access with authentication (JWT), and it is designed to be extendable, allowing you to add more models and features. Additionally, you can integrate a frontend using **HTML** or **Streamlit** for real-time interaction with these models.

---

## Features

- **Multi-Model Support**: Interact with different LLMs like OpenAI and LLaMA. The application can query models dynamically.
- **Embeddings**: Obtain text embeddings from models like OpenAI and LLaMA.
- **Multi-User Access**: The application supports multi-user environments with JWT-based authentication.
- **RESTful API**: A structured API for sending queries and receiving responses from the models.
- **Frontend Integration**: Can be integrated with a frontend using HTML or Streamlit for user interaction.
- **Extensibility**: The project is modular, allowing for easy addition of new models or services.

---

## Tech Stack

- **Backend**: FastAPI, Python
- **Models**: OpenAI, LLaMA, Custom Embedding Models
- **Database**: SQLite (or any SQLAlchemy-compatible database)
- **Authentication**: JWT-based multi-user authentication
- **Frontend**: Optional (HTML/Streamlit)
- **Containerization**: Docker (optional)
  
---

## Folder Structure

```
fastapi_llm_app/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── llm.py
│   │   │   │   └── embeddings.py
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   ├── db/
│   │   ├── models/
│   │   │   └── user.py
│   ├── schemas/
│   │   ├── user.py
│   │   └── llm.py
│   ├── services/
│   │   ├── llm_service.py
│   │   ├── embedding_service.py
│   ├── utils/
│   │   ├── llama_integration.py
│   │   ├── openai_integration.py
│   │   ├── embedding_integration.py
│   ├── frontend/
│   │   ├── templates/
│   │   └── streamlit_app.py
│   ├── main.py
├── tests/
├── .env
├── requirements.txt
└── Dockerfile
```

---

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/fastapi-llm-app.git
cd fastapi-llm-app
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory and provide the necessary API keys and database URL:
```
OPENAI_API_KEY="your_openai_api_key"
LLAMA_API_URL="http://llama-api-url"
DATABASE_URL="sqlite:///./test.db"
```

### 5. Run the Application
```bash
uvicorn app.main:app --reload
```

The application will be running at: `http://127.0.0.1:8000`

### 6. Access API Documentation
FastAPI provides interactive API documentation:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Features and Usage

### 1. Query LLM Models (OpenAI, LLaMA)
Send a request to the LLM endpoint to query a specific model:
- **Endpoint**: `/api/v1/llm/query`
- **Method**: `POST`
- **Payload**:
    ```json
    {
        "model_name": "openai",
        "prompt": "What is the capital of France?"
    }
    ```
- **Response**:
    ```json
    {
        "model_name": "openai",
        "response": "The capital of France is Paris."
    }
    ```

### 2. Query Embeddings from Models
Send a request to the embeddings endpoint:
- **Endpoint**: `/api/v1/embeddings/query`
- **Method**: `POST`
- **Payload**:
    ```json
    {
        "model_name": "openai",
        "prompt": "Machine learning is fascinating."
    }
    ```
- **Response**:
    ```json
    {
        "model_name": "openai",
        "response": [embedding_vector]
    }
    ```

### 3. Multi-User Authentication
The app supports JWT-based authentication:
- **Login**: Users authenticate and receive a JWT token.
- **Protected Routes**: Add routes that require JWT authentication.

### 4. Streamlit Frontend (Optional)
You can interact with the models via a Streamlit frontend. To run the Streamlit app:
```bash
streamlit run app/frontend/streamlit_app.py
```

### 5. Docker Support (Optional)
Build and run the application in Docker:
```bash
docker build -t fastapi-llm-app .
docker run -d -p 8000:8000 fastapi-llm-app
```

---

## Testing

Unit tests are available in the `tests/` folder. To run the tests:
```bash
pytest tests/
```

---

## Future Improvements

- **Model Expansion**: Add more LLM models (GPT-4, Hugging Face models, etc.).
- **Frontend**: Build an HTML frontend for more complex interactions.
- **Scaling**: Integrate with a cloud platform like AWS or GCP for scalable deployments.
- **Logging & Monitoring**: Add structured logging and monitoring for production readiness.

---

## Contributing

Feel free to contribute by opening an issue or submitting a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

