# 11. API Specification

## 1. Purpose
This document acts as the contract between the Frontend React application and the Backend Node.js server.

## 2. Scope
Defines the REST endpoints required for the MVP. Auth is handled via JWT Bearer tokens in the `Authorization` header.

## 3. Endpoints

### 3.1 Authentication
**POST `/api/auth/register`**
*   **Request Body:** `{ "email": "a@b.com", "password": "xxx", "archetype": "STUDENT" }`
*   **Response (200):** `{ "token": "jwt_string", "user": {...} }`

**POST `/api/auth/login`**
*   **Request Body:** `{ "email": "a@b.com", "password": "xxx" }`
*   **Response (200):** `{ "token": "jwt_string", "user": {...} }`

### 3.2 Simulation State
**GET `/api/simulation/state`**
*   **Headers:** `Authorization: Bearer <token>`
*   **Response (200):** Returns the `PlayerState` JSON object defined in `15_PLAYER_STATE.md`.

### 3.3 Engine Execution
**POST `/api/simulation/advance-month`**
*   **Headers:** `Authorization: Bearer <token>`
*   **Request Body:** 
    ```json
    {
      "decisions": {
        "payCreditCard": 2000,
        "investEquities": 5000,
        "investFixedDeposit": 0
      }
    }
    ```
*   **Response (200):**
    ```json
    {
      "success": true,
      "eventTriggered": {
         "title": "Medical Emergency",
         "deduction": 15000
      },
      "newState": { ... PlayerState JSON ... }
    }
    ```
*   **Error Responses:** 
    *   `400 Bad Request`: If `payCreditCard + investEquities > CurrentCash`.
    *   `403 Forbidden`: If user is Bankrupt or Retired.

### 3.4 Historical Data
**GET `/api/simulation/history`**
*   **Headers:** `Authorization: Bearer <token>`
*   **Response (200):**
    ```json
    {
      "history": [
        { "month": 1, "netWorth": 10000, "cash": 5000 },
        { "month": 2, "netWorth": 11000, "cash": 6000 }
      ]
    }
    ```

## 4. References
* [15_PLAYER_STATE.md](15_PLAYER_STATE.md)
* [08_GAME_LOOP.md](08_GAME_LOOP.md)

## 5. Future Considerations
GraphQL may be considered for post-internship scaling, but REST is strictly enforced for the MVP due to the simple nature of the data access patterns.
