Music Store API — Phase 2 Coding Assignment


This project is a read-only REST API built using FastAPI and asyncpg for the Phase 2 assignment.It connects to a PostgreSQL (Supabase) database and provides endpoints to fetch artists, albums, invoices, and customer spending details.
🧱 Tech Stack

Language: Python 3.10+

Framework: FastAPI

Database: PostgreSQL (Supabase - Read Only)

Driver: asyncpg (Asynchronous DB driver)

Server: Uvicorn (ASGI)

Data Validation: Pydantic

Architecture: Router → Service → DAO → Database

📂 Project Structure
musicstore_api/
│
├── app.py                    # FastAPI application entrypoint
├── db.py                     # Database connection pool setup
│
├── dao/
│   ├── artist_dao.py
│   ├── album_dao.py
│   └── customer_dao.py
│
├── routers/
│   ├── artists.py
│   ├── albums.py
│   └── customers.py
│
├── services/
│   ├── artist_service.py
│   ├── album_service.py
│   └── customer_service.py
│
├── schemas/
│   ├── artist.py
│   ├── album.py
│   └── invoice.py
│
├── requirements.txt
├── README.md
└── Dockerfile

⚙️ Setup Instructions (Mac/Linux)
1️⃣ Clone the repository
git clone https://github.com/Rohanharsh163/musicstore_api.git
cd musicstore_api

2️⃣ Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the FastAPI app
uvicorn app:app --reload --port 8000

5️⃣ Verify API is running

Open your browser and go to:
👉 http://127.0.0.1:8000/docs

(Swagger UI)
Or test via terminal:

curl http://127.0.0.1:8000/artists

🧩 Database Configuration

Database: Supabase PostgreSQL (Read-only access)

Parameter	Value
Host	aws-1-ap-southeast-1.pooler.supabase.com
Port	6543
User	bitshuser_ro.ziyfpepffnykprwwljnc
Password	weloveancfood
Database	postgres
These credentials are pre-configured in db.py.	
🚀 API Endpoints
Endpoint	Method	Description
/artists	GET	Get all artists
/albums	GET	Get all albums or filter by artist
/customers/{id}/invoices	GET	Get all invoices for a customer
/customers/{id}/total_spend	GET	Get total amount spent by a customer
🧪 Example Requests
Get all artists
curl http://127.0.0.1:8000/artists


Response:

[
  {"artist_id": 1, "name": "AC/DC"},
  {"artist_id": 2, "name": "Aerosmith"}
]

Get albums for an artist
curl "http://127.0.0.1:8000/albums?artist_id=1"


Response:

[
  {"album_id": 1, "title": "For Those About To Rock We Salute You", "artist_id": 1},
  {"album_id": 2, "title": "Let There Be Rock", "artist_id": 1}
]

Get customer invoices
curl http://127.0.0.1:8000/customers/1/invoices


Response:

[
  {"invoice_id": 1, "invoice_date": "2024-05-12T00:00:00", "total": 12.99},
  {"invoice_id": 2, "invoice_date": "2024-08-20T00:00:00", "total": 15.49}
]

Get customer total spend
curl http://127.0.0.1:8000/customers/1/total_spend


Response:

{
  "customer_id": 1,
  "name": "Luis Goncalves",
  "total_spent": 45.97
}


If customer not found:

{"error": "Customer not found"}

🧠 Architecture Overview

Layered Design:

Router → Service → DAO → Database


Router — Defines HTTP endpoints and response structures.

Service — Contains business logic, error handling, and validation.

DAO (Data Access Object) — Handles SQL queries and interacts with the database.

Database — Uses asyncpg for efficient asynchronous connection pooling.
This structure keeps the code modular, testable, and easy to maintain.



Then open:
👉 http://127.0.0.1:8000/docs
