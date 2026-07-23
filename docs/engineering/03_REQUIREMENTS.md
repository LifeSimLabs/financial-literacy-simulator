# 03. Requirements Analysis

## 1. Purpose
This document extracts, categorizes, and solidifies all requirements for the Financial Literacy Simulator internship MVP.

## 2. Scope
This acts as the absolute source of truth for what must be built to consider the internship successful. Any feature not listed here is out of scope.

## 3. Definitions
* **NFR:** Non-Functional Requirement (Performance, Security, Reliability).
* **FR:** Functional Requirement (What the system actually does).
* **Internship MVP:** The strict boundaries of the current development phase.

## 4. Requirements Breakdown

### 4.1 Business Requirements (BR)
* **BR-01:** The product must align with the experiential learning goals of NSFE 3.0.
* **BR-02:** The project must be open-source and free to use.
* **BR-03:** The simulator must visually demonstrate the consequences of financial decisions over long time horizons.

### 4.2 Functional Requirements (FR)
* **FR-01 (Auth):** Users must be able to create an account and log in.
* **FR-02 (Onboarding):** Users must select a starting Archetype (e.g., Student, Entrepreneur) which defines their initial financial state.
* **FR-03 (Simulation):** The user can advance the simulation one "Turn" (1 Month) at a time.
* **FR-04 (Decisions):** Before advancing, users must be able to allocate available Cash to: Pay Debt, Invest, or Save.
* **FR-05 (Events):** The system must generate random hazard events (e.g., UPI Fraud, Medical Bill) during the monthly progression.
* **FR-06 (Reporting):** The dashboard must display historical line charts tracking Net Worth, Cash, Assets, and Debt.

### 4.3 Non-Functional Requirements (NFR)
* **NFR-01 (Precision):** Financial math must not suffer from floating-point errors. Use integer math (cents/paise) or a decimal library.
* **NFR-02 (Performance):** The `advance-month` API endpoint must return a new state within 500ms to ensure a smooth gameplay loop.
* **NFR-03 (Security):** User endpoints must be secured via JWT. Users cannot modify another user's simulation state.

### 4.4 Technical Requirements (TR)
* **TR-01 (Frontend):** React (Vite) utilizing Recharts for data visualization.
* **TR-02 (Backend):** Node.js with Express.js, written in strict TypeScript.
* **TR-03 (Database):** Amazon DynamoDB utilizing a Single-Table Design.
* **TR-04 (Infrastructure):** Local development via Docker + LocalStack; Production via AWS (S3, AppRunner/ECS).

### 4.5 Engineering & Learning Requirements (ER)
* **ER-01:** Strict adherence to Git flow (Feature branches, Pull Requests).
* **ER-02:** 100% Unit test coverage on the pure mathematical functions inside the `SimulationEngine`.
* **ER-03:** Code must pass automated ESLint and Prettier checks before merging.
* **ER-04:** Demonstration of clean architecture boundaries (Database logic decoupled from Business math).

## 5. References
* `docs/methodology/SDLC_1.MD`
* [07_SIMULATION_ENGINE.md](07_SIMULATION_ENGINE.md)
* [18_TESTING_STRATEGY.md](18_TESTING_STRATEGY.md)

## 6. Future Considerations
Subsequent versions will introduce multiplayer scaling requirements (WebSockets for real-time household budgets) and Generative AI latency constraints (handling LLM response times during state advancement).
