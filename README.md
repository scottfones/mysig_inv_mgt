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

The backend uses [axum](https://github.com/tokio-rs/axum) to facilitate [GraphQL](https://github.com/async-graphql/async-graphql) queries against a [Postgres](https://www.postgresql.org/) database via [SeaORM](https://www.sea-ql.org/SeaORM/). The current schema corresponds to the following diagram.

```mermaid
erDiagram
  KEYWORD {
    uuid id PK
    string keyword PK
  }
  BIN {
    uuid id PK
    string bin_name PK
  }
  COLOR {
    uuid id PK
    string color PK
    string accent
  }
  SIZE {
    uuid id PK
    float height PK
    float width PK
  }
  MATERIAL {
    uuid id PK
    string material PK
  }
  IMG {
    uuid id PK
    string img_file PK
  }
  QUANTITY {
    uuid id PK
    int count PK
  }
```

### Migrations



