# Mysig Inventory Management Application

## Overview

A CRUD application to track inventory information and location. 

```mermaid
stateDiagram-v2
  [*] --> Backend
  [*] --> Frontend
  Frontend --> Search
  Frontend --> Add: /add
  Search --> Results
  state Results {
    View
    Edit 
    Delete
  }
```

## Backend

```mermaid
erDiagram
  COOKIECUTTER }|--|| BIN
  COOKIECUTTER {
    int id PK
    int binId FK
    int ColorId FK
    string Keywords
    float Height
    float Width
    int materialId FK
    string imageFile
  }
  BIN {
    int binId PK
    string name
  }
  COOKIECUTTER }|--|| COLOR
  COLOR {
    int colorID PK
    string name
  }
  COOKIECUTTER }|--|| MATERIAL
  MATERIAL {
    int materialId PK
    name
  }
```

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER {
        string name
        string custNumber
        string sector
    }
    ORDER ||--|{ LINE-ITEM : contains
    ORDER {
        int orderNumber
        string deliveryAddress
    }
    LINE-ITEM {
        string productCode
        int quantity
        float pricePerUnit
    }
```
