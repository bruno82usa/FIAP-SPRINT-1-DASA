import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "endpoints" in response.json()

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert data["version"] == "1.0.0"

def test_upload_pdf_invalid_file():
    # Test with non-PDF file
    files = {"file": ("test.txt", b"test content", "text/plain")}
    response = client.post("/upload", files=files)
    assert response.status_code == 400
    assert "Only PDF files are allowed" in response.json()["detail"]

def test_upload_pdf_success():
    # Create a dummy PDF file
    pdf_content = b"%PDF-1.4\ntest\n"
    files = {"file": ("test.pdf", pdf_content, "application/pdf")}
    response = client.post("/upload", files=files)
    
    assert response.status_code == 200
    data = response.json()
    assert "report_id" in data
    assert data["status"] == "received"
    assert "message" in data
    assert data["estimated_processing_time"] == 30

def test_ask_question():
    request_data = {
        "report_id": "test123",
        "question": "What is my risk for diabetes?"
    }
    response = client.post("/ask", json=request_data)
    
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "confidence" in data
    assert "sources" in data
    assert "disclaimer" in data
    assert isinstance(data["confidence"], float)
    assert 0 <= data["confidence"] <= 1

def test_ask_question_generic():
    request_data = {
        "report_id": "test123",
        "question": "Some random question"
    }
    response = client.post("/ask", json=request_data)
    
    assert response.status_code == 200
    data = response.json()
    assert len(data["answer"]) > 0

def test_get_recommendations():
    response = client.get("/recommendations/test123")
    
    assert response.status_code == 200
    data = response.json()
    assert "recommendations" in data
    assert "categories" in data
    assert "priority" in data
    assert isinstance(data["recommendations"], list)
    assert len(data["recommendations"]) > 0

def test_get_report_summary():
    response = client.get("/reports/test123/summary")
    
    assert response.status_code == 200
    data = response.json()
    assert data["report_id"] == "test123"
    assert data["status"] == "processed"
    assert "summary" in data
    assert "processed_at" in data

def test_cors_headers():
    response = client.get("/health")
    assert "access-control-allow-origin" in response.headers

if __name__ == "__main__":
    pytest.main([__file__, "-v"])