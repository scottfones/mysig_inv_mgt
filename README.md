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

The backend uses [axum](https://github.com/tokio-rs/axum) to facilitate [GraphQL](https://github.com/async-graphql/async-graphql) queries against a [PostgresSQL](https://www.postgresql.org/) database via [SeaORM](https://www.sea-ql.org/SeaORM/). The current schema corresponds to the following diagram.

```mermaid
erDiagram
  COOKIECUTTER }|--|| BIN: has
  COOKIECUTTER }|--|| COLOR: has
  COOKIECUTTER }|--|| MATERIAL: has
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
  COLOR {
    int colorID PK
    string name
  }
  MATERIAL {
    int materialId PK
    string name
  }
```

### Migrations



