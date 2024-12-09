# Axmed Medication SKU Management

This project is a backend service for managing medication SKUs, including functionalities for CRUD operations and bulk creation of SKUs. It is built using Django and Django REST Framework.

## Test with Swagger

```url
  https://h-axmed-medication.onrender.com/docs/
```

🚀 **Live Demo**: [Click Me](https://h-axmed-medication.onrender.com/docs/)

## Features

- **CRUD Operations**:
  - Create, read, update, and delete individual medication SKUs.
- **Bulk Upload**:
  - Upload multiple SKUs through a single API.
- **Validation**:
  - Ensures unique combinations of `medication_name`, `formulation`, `dosage`, and `unit`.
  - Validates dosage (positive number) and prohibits numerical values in `formulation` and `unit`.

## Technology Stack

- **Backend Framework**: Django
- **API Development**: Django REST Framework
- **Database**: SQLite (default, configurable for other databases)

---

## Setup and Installation

### Prerequisites

- Python 3.9+
- Django 5.1+
- pip

### Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd axmed
   ```

## Axmed Medication SKU Management

This project provides backend services for managing medication SKUs, enabling CRUD operations and bulk creation of SKUs via REST APIs. Built with Django and Django REST Framework.

### Features

- **CRUD Operations**: Manage individual SKUs (create, read, update, delete).
- **Bulk Upload**: Upload multiple SKUs in one request.
- **Validation**: Ensure valid and unique SKU records.

---

### Setup and Installation

#### Prerequisites

- Python 3.9+
- pip
- (Optional) Docker

#### Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## API Endpoints

### Base URL

`http://127.0.0.1:8000/skus/`

---

### 1. **List SKUs**

- **URL**: `/read/`
- **Method**: `GET`
- **Description**: Retrieve all SKUs.
- **Example Response**:
  ```json
  [
    {
      "id": 1,
      "medication_name": "Amoxicillin",
      "formulation": "Tablet",
      "dosage": 50,
      "unit": "mg"
    }
  ]
  ```

### 2. **Create a New SKU**

- **URL**: `/create/`
- **Method**: `POST`
- **Parameters**:
  - `medication_name` (string)
  - `formulation` (string)
  - `dosage` (positive number)
  - `unit` (string)
- **Example Request**:
  ```json
  {
    "medication_name": "Paracetamol",
    "formulation": "Tablet",
    "dosage": 500,
    "unit": "mg"
  }
  ```

### 3. **Update an Existing SKU**

- **URL**: `/update/<id>/`
- **Method**: `PUT`
- **Parameters**: Same as for creation.
- **Example Request**: Update the dosage of SKU with ID 1:
  ```json
  {
    "dosage": 250
  }
  ```

### 4. **Delete an SKU**

- **URL**: `/delete/<id>/`
- **Method**: `DELETE`

---

### 5. **Bulk Create SKUs**

- **URL**: `/bulk-create/`
- **Method**: `POST`
- **Parameters**: List of SKUs.
- **Example Request**:
  ```json
  [
    {
      "medication_name": "Ibuprofen",
      "formulation": "Capsule",
      "dosage": 200,
      "unit": "mg"
    },
    {
      "medication_name": "Aspirin",
      "formulation": "Tablet",
      "dosage": 100,
      "unit": "mg"
    }
  ]
  ```
