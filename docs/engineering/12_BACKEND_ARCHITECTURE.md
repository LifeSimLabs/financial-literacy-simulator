# 12. Backend Architecture

## 1. Purpose
This document dictates the folder structure, dependency rules, and coding standards for the Node.js/TypeScript backend.

## 2. Scope
Applies exclusively to the code running on the Express.js server.

## 3. Architecture Style: Modular Monolith
The backend uses a layered architecture to strictly separate HTTP concerns from database concerns from business logic.

## 4. Folder Structure (src/)

```text
src/
 ├── controllers/    # Express route handlers. Parses req.body, calls services.
 ├── services/       # Orchestration. Fetches from DB, passes to Engine, saves to DB.
 ├── engine/         # Pure Math. NO DB/HTTP calls. 100% Unit Tested.
 │   ├── math.ts     # Compound interest formulas.
 │   ├── events.ts   # RNG hazard generators.
 │   └── loop.ts     # The monthly state transition function.
 ├── repositories/   # DynamoDB DocumentClient interactions.
 ├── middlewares/    # JWT Auth, Zod Validation, Error handling.
 ├── models/         # TypeScript interfaces (PlayerState, History).
 └── utils/          # Logger, Config, Constants.
```

## 5. The "Dependency Inversion" Rule
The `engine/` folder is the sacred core. 
* Code inside `engine/` is **not allowed** to import anything from `repositories/` or `controllers/`.
* Code inside `engine/` can only rely on native JavaScript/TypeScript features (Math, Arrays, Objects).
* **Why:** This makes the financial simulation logic perfectly testable in isolation.

## 6. Coding Standards
*   **Strict Typing:** `any` is banned. All functions must declare input/output types.
*   **Error Handling:** Controllers must wrap service calls in `try/catch` and pass errors to a global Express error handler middleware via `next(err)`.
*   **Validation:** All incoming POST requests must be validated using `zod` before hitting the controller logic.

## 7. References
* [07_SIMULATION_ENGINE.md](07_SIMULATION_ENGINE.md)
* [10_DATABASE_DESIGN.md](10_DATABASE_DESIGN.md)

## 8. Future Considerations
If the `SimulationEngine` becomes computationally heavy (e.g., calculating millions of nodes for a macro-economy), the `engine/` folder can be extracted into its own Microservice or AWS Lambda function without rewriting any code.
