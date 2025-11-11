# 🎵 Music Store API — Phase 2 Coding Assignment

This is a **read-only REST API** built using **FastAPI** and **asyncpg** for the Phase 2 assignment.  
It connects to a **PostgreSQL (Supabase)** database and provides endpoints to fetch **artists, albums, invoices, and customer spending details**.

---

## 🧱 Tech Stack

| Component | Technology |
|------------|-------------|
| **Language** | Python 3.10+ |
| **Framework** | FastAPI |
| **Database** | PostgreSQL (Supabase - Read Only) |
| **Driver** | asyncpg (Asynchronous DB driver) |
| **Server** | Uvicorn (ASGI) |
| **Validation** | Pydantic |
| **Architecture** | Router → Service → DAO → Database |

---

## 📂 Project Structure

```
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
```

---

## ⚙️ Setup Instructions (Mac/Linux)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Rohanharsh163/musicstore_api.git
cd musicstore_api
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the FastAPI App
```bash
uvicorn app:app --reload --port 8000
```

### 5️⃣ Verify API is Running

Open your browser:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Or test via terminal:
```bash
curl http://127.0.0.1:8000/artists
```

---

## 🧩 Database Configuration

**Database:** Supabase PostgreSQL (Read-only access)

| Parameter | Value |
|------------|--------|
| **Host** | aws-1-ap-southeast-1.pooler.supabase.com |
| **Port** | 6543 |
| **User** | bitshuser_ro.ziyfpepffnykprwwljnc |
| **Password** | weloveancfood |
| **Database** | postgres |

These credentials are pre-configured in `db.py`.

---

## 🚀 API Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/artists` | GET | Get all artists |
| `/albums` | GET | Get all albums or filter by artist |
| `/customers/{id}/invoices` | GET | Get all invoices for a customer |
| `/customers/{id}/total_spend` | GET | Get total amount spent by a customer |

---

## 🧪 Example Requests

### 🎤 Get All Artists
```bash
curl http://127.0.0.1:8000/artists
```

**Response:**
```json
[
  {"artist_id": 1, "name": "AC/DC"},
  {"artist_id": 2, "name": "Aerosmith"}
]
```

---

### 💿 Get Albums by Artist
```bash
curl "http://127.0.0.1:8000/albums?artist_id=1"
```

**Response:**
```json
[
  {"album_id": 1, "title": "For Those About To Rock We Salute You", "artist_id": 1},
  {"album_id": 2, "title": "Let There Be Rock", "artist_id": 1}
]
```

---

### 🧾 Get Customer Invoices
```bash
curl http://127.0.0.1:8000/customers/1/invoices
```

**Response:**
```json
[
  {"invoice_id": 1, "invoice_date": "2024-05-12T00:00:00", "total": 12.99},
  {"invoice_id": 2, "invoice_date": "2024-08-20T00:00:00", "total": 15.49}
]
```

---

### 💰 Get Customer Total Spend
```bash
curl http://127.0.0.1:8000/customers/1/total_spend
```

**Response:**
```json
{
  "customer_id": 1,
  "name": "Luis Goncalves",
  "total_spent": 45.97
}
```

If customer not found:
```json
{"error": "Customer not found"}
```

---

## 🧠 Architecture Overview

**Layered Design:**  
`Router → Service → DAO → Database`

| Layer | Description |
|--------|--------------|
| **Router** | Defines HTTP endpoints and response structures |
| **Service** | Contains business logic, error handling, and validation |
| **DAO** | Handles SQL queries and interacts with the database |
| **Database** | Uses `asyncpg` for efficient async connection pooling |

This structure ensures the app is **modular**, **testable**, and **maintainable**.

---

## 🌐 Documentation

Once the app is running:  
👉 Open [Swagger UI](http://127.0.0.1:8000/docs) for interactive API docs.
