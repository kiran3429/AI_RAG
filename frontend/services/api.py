import requests

BACKEND_URL = "https://rag-studio-123312036314.asia-south1.run.app"


def get_rags():
    response = requests.get(f"{BACKEND_URL}/rags")
    response.raise_for_status()
    return response.json()

def upload_pdf(uploaded_file):

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            "application/pdf"
        )
    }

    response = requests.post(
        f"{BACKEND_URL}/uploads",
        files=files
    )

    response.raise_for_status()

    return response.json()

def ask_question(question):

    payload = {
        "question": question
    }

    response = requests.post(
        f"{BACKEND_URL}/chat",
        json=payload
    )

    print("Status:", response.status_code)
    print("Response:", response.text)

    response.raise_for_status()

    return response.json()