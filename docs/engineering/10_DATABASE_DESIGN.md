# 10. Database Design

## 1. Purpose
This document defines the Amazon DynamoDB schema for the project using a Single-Table Design pattern.

## 2. Scope
Covers the partition keys, sort keys, indexes, and access patterns required to support the MVP APIs.

## 3. Definitions
* **PK:** Partition Key. Determines physical storage node.
* **SK:** Sort Key. Determines sorting order within a partition.
* **GSI:** Global Secondary Index.

## 4. The Single Table: `fls-main-table`

We store multiple entity types (Users, States, Historical snapshots) in the exact same table by using composite keys.

### 4.1 Schema Definition
*   **Partition Key (String):** `PK`
*   **Sort Key (String):** `SK`

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
