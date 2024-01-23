# Mysig Inventory Management Application

## Overview

A CRUD application to track inventory information and location. 



```mermaid
stateDiagram-v2
  [*] --> Search: /
  [*] --> Add: /add
  Search --> Results
  state Results {
    View
    Edit 
    Delete
  }
```
