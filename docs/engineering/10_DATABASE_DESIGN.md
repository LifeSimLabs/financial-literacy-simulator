# 10. Database Design

## 1. Purpose
This document defines the database schema for the project. While we are currently using **MongoDB Atlas (Free Tier)** for the MVP, the schema is designed using a **Single-Table (Single-Collection) Design** pattern to ensure a seamless future migration to **Amazon DynamoDB**.

## 2. Scope
Covers the core entity keys, indexes, and access patterns required to support the MVP APIs.

## 3. Definitions
* **PK (Partition Key):** In MongoDB, this acts as the primary indexed field for grouping related documents.
* **SK (Sort Key):** In MongoDB, this is the secondary indexed field used for sorting or filtering within a partition.
* **GSI (Global Secondary Index):** Alternative indexes created on other fields.

## 4. The Single Collection: `fls_main_collection`

We store multiple entity types (Users, States, Historical snapshots) in the exact same collection by using composite keys (PK and SK).

### 4.1 Schema Definition
*   **Partition Key Field (String):** `PK`
*   **Sort Key Field (String):** `SK`

### 4.2 Entity Mapping

#### A. User Profile Entity
Stores permanent user details.
*   **PK:** `USER#<userId>`
*   **SK:** `PROFILE`
*   *Attributes:* `email`, `createdAt`, `passwordHash`, `archetype`

#### B. Current State Entity
Stores the *current* month's financial data. Heavily overwritten.
*   **PK:** `USER#<userId>`
*   **SK:** `STATE`
*   *Attributes:* `currentMonth`, `cash`, `netWorth`, `assets` (JSON), `liabilities` (JSON)

#### C. Historical Snapshot Entity
Appended every time a month advances. Used to draw line charts.
*   **PK:** `USER#<userId>`
*   **SK:** `HISTORY#<month_id>` (e.g., `HISTORY#001`, `HISTORY#002`)
*   *Attributes:* `netWorth`, `cash`, `eventTriggered`

## 5. Access Patterns

| Access Pattern | Query / Operation |
| :--- | :--- |
| **Get User Profile** | `GetItem(PK="USER#123", SK="PROFILE")` |
| **Get Current Game State** | `GetItem(PK="USER#123", SK="STATE")` |
| **Save New Game State** | `PutItem(PK="USER#123", SK="STATE")` |
| **Log Historical Month** | `PutItem(PK="USER#123", SK="HISTORY#024")` |
| **Fetch Full History Chart** | `Query(PK="USER#123" AND SK begins_with "HISTORY#")` |

## 6. References
* [11_API_SPECIFICATION.md](11_API_SPECIFICATION.md)

## 7. Future Considerations
If we implement a Global Leaderboard or Economy System, we will need a GSI (Global Secondary Index) that partitions by `SCORE` rather than `USER_ID`.
