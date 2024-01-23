# Mysig Inventory Management Application

```mermaid
stateDiagram-v2
  [*] --> Search
  [*] --> Add
  Search --> Results
  state Results {
    View
    Edit 
    Delete
  }
```
