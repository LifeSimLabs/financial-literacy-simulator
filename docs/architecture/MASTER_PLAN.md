# Software Development Master Plan: Financial Literacy Simulator

## 1. Executive Summary
The **Financial Literacy Simulator (FLS)** is a gamified life-simulation engine designed to transition financial education from passive theory to experiential learning, aligning with the NCFE's NSFE 3.0. 

As the Principal Software Architect, this Master Plan prioritizes the **internship requirements above all else**. The primary objective is to deliver a robust, well-engineered, stateful time-based system that models real-world financial domains. All "startup" aspirations (Generative AI, dynamic storytellers, multiplayer pools) have been ruthlessly excised from the MVP and isolated in the Future Roadmap to guarantee on-time delivery, clean architecture, and absolute engineering quality.

---

## 2. Requirement Analysis

*   **Business Requirements:** Align with NCFE NSFE 3.0 to deliver an open-source, experiential financial "sandbox" for Indian youth.
*   **Functional Requirements:** Users must be able to create an account, select an archetype/life-stage, process monthly financial decisions (budget, invest, pay loans), and view their compounding net worth.
*   **Non-Functional Requirements:** High mathematical precision (no floating-point drift), sub-second API response times for state updates, and an intuitive, mobile-first responsive dashboard.
*   **Technical Requirements:** React frontend, Node.js + Express backend (TypeScript), Amazon DynamoDB (Single Table Design), AWS deployment, GitHub CI/CD, LocalStack for dev.
*   **Learning Requirements:** The system must teach compounding interest, the dangers of high-interest debt, the necessity of emergency funds, and the impact of inflation.
*   **Simulation Requirements:** 1 Real-World Week = 1 Simulated Month. The engine must support a deterministic monthly state progression loop.
*   **Financial Requirements:** Must accurately reflect basic Indian financial systems (simplified Income Tax slabs, EPF/PPF equivalents, SIP mutual funds).
*   **Engineering Requirements:** Strict Git workflow, Pull Request reviews, 100% test coverage on pure financial math functions, modular DDD (Domain-Driven Design) where appropriate.
*   **Deployment Requirements:** Automated GitHub Actions pipeline deploying to AWS (e.g., S3/CloudFront for frontend, AppRunner/ECS for backend).
*   **Testing Requirements:** Unit tests for math/engine logic, integration tests for API endpoints, manual UI testing.

---

## 3. Research Synthesis

*   **Repeated Concepts:** Gamification increases engagement by 150%; learning by consequence is superior to rote memorization; time compression is key to seeing consequences.
*   **Missing Concepts:** Exact mathematical formulas (e.g., exact tax brackets, specific mutual fund alpha/beta) are vaguely referenced but not hardcoded in the research.
*   **Conflicting Recommendations:** The deep research heavily pushes an *AI Storyteller (Generative LLMs)*, while the internship presentation mandates a *deterministic, stateful time-based system*. 
    *   *Resolution:* We will use a deterministic Random Event Generator for the MVP. AI is unpredictable and introduces massive testing risk for an internship project.
*   **Weak Assumptions:** Assuming users will want to read long paragraphs of text during a game. The UI must rely on charts and immediate numerical feedback.
*   **Strong Evidence:** SDT (Self-Determination Theory) proves that intrinsic mastery (watching net worth grow) retains users better than extrinsic rewards (badges/points).
*   **Reusable Ideas:** The "Factorio" automated pipeline concept (sweeping salary into investments automatically) is highly reusable for UI design.
*   **Ideas suitable for MVP:** Strict state progression, basic archetypes, localized Indian context, deterministic hazard events (frauds/scams).
*   **Ideas suitable after MVP:** Dynamic LLM narrative generation, cooperative multiplayer households, mutual insurance pools.

---

## 4. Knowledge Map

```text
[NCFE Framework & SDT Psychology]
       │
       ▼
[Experiential Learning Model] ──▶ [Time Abstraction: 1 Week = 1 Month]
       │                                     │
       ▼                                     ▼
[Domain Knowledge (Books)]            [Simulation Engine]
 ├── Archetypes (Farmers, Youth)       ├── Monthly Cashflow
 ├── Scams & Frauds                    ├── Asset Appreciation
 └── Tax & Savings Rules               └── Debt Amortization
```

---

## 5. Feature Prioritization

*   **Phase 1: Must Build (The Engine)**
    *   *Features:* User Auth, Core State Machine, Monthly Advancement Logic, Basic Income/Expense math.
    *   *Why:* Without the mathematical core, the simulator cannot function.
*   **Phase 2: Should Build (The UI & Persistence)**
    *   *Features:* React Dashboard, DynamoDB persistence, Historical Net Worth Charts.
    *   *Why:* Fulfills the requirement for users to visualize the compounding consequences of their decisions.
*   **Phase 3: Good Enhancement (The Friction)**
    *   *Features:* Static Random Event Engine (e.g., Medical Emergency, Job Loss, Fraud Scams).
    *   *Why:* Introduces real-world uncertainty, teaching the value of emergency funds.
*   **Phase 4: Future Startup Feature (The Polish)**
    *   *Features:* Generative AI NPCs, Peer-to-Peer Insurance Pools, Macro-economic cycles.
    *   *Why:* Highly complex, non-essential for proving the core educational thesis.

---

## 6. Domain Engineering

*   **Player Domain:** 
    *   *Purpose:* Manages user identity and archetype.
    *   *State:* Demographics, Current Life Stage, Well-being score.
*   **Financial Domain (Ledger):**
    *   *Purpose:* The single source of truth for money.
    *   *State:* Cash, Net Worth, Total Income, Total Expenses.
*   **Asset Domain:**
    *   *Purpose:* Tracks appreciating investments.
    *   *State:* Equities (Mutual Funds), Fixed Deposits, Physical Assets (Real Estate).
*   **Liability Domain:**
    *   *Purpose:* Tracks depreciating or interest-bearing debt.
    *   *State:* Credit Cards, Personal Loans, Home Loans (Principal, Interest Rate, EMI).
*   **Event Domain:**
    *   *Purpose:* Generates and applies life shocks.
    *   *State:* Event History, Active Penalties (e.g., Hospital Bill).
*   **Simulation Domain:**
    *   *Purpose:* Orchestrates the advancement of time.
    *   *State:* Current Simulated Month, Simulation Status (Active, Bankrupt, Retired).

---

## 7. Business Rules

1.  **Time Rule:** 1 turn = 1 simulated month.
2.  **Salary Rule:** Salary is credited on tick 1 of the month. Annual increments occur every 12 simulated months based on Career Level.
3.  **Expense Rule:** Mandatory expenses (rent, food) are deducted automatically. If Cash < Mandatory Expenses, trigger Auto-Debt (Credit Card).
4.  **Loan Rule:** EMIs are deducted automatically. Unpaid credit card balances compound at 3% monthly (36% annualized).
5.  **Investment Rule:** Equities grow/shrink based on a randomized market return array (averaging 12% annually, but volatile month-to-month). Fixed Deposits grow at a guaranteed 7% annually (0.56% monthly).
6.  **Tax Rule:** Applied annually (every 12 months) based on a simplified 3-slab Indian tax regime.
7.  **Bankruptcy Rule:** If Total Debt > (Total Assets * 1.5) AND Cash is negative, trigger Game Over.
8.  **Net Worth Calculation:** `(Cash + Assets) - (Total Debt)`.

---

## 8. Simulation Design

**The Monthly State Update Loop:**
1.  **Pre-computation:** Fetch current `SimulationState` from DB.
2.  **Income Phase:** Add `Salary` to `Cash`.
3.  **Deduction Phase:** Subtract `Fixed Expenses` and `Loan EMIs` from `Cash`.
4.  **Growth Phase:** Apply `Monthly Interest` to `Debt` and `Market Returns` to `Assets`.
5.  **Event Phase:** Roll RNG (10% chance). If hit, pull event from `EventLog` (e.g., "Car Repair: -₹15,000") and apply to `Cash`.
6.  **Resolution Phase:** Recalculate `Net Worth`.
7.  **Persistence:** Save updated `SimulationState` to DynamoDB.

---

## 9. Software Architecture

*   **Style:** Modular Monolith (Backend) + Single Page Application (Frontend).
*   **Layered Architecture (Backend):**
    *   `Controllers` (Handle HTTP requests, extract args).
    *   `Services` (Business logic, orchestration).
    *   `Engine` (Pure functions for financial math. NO database dependencies here).
    *   `Repositories` (DynamoDB interactions).
*   **Design Principles:**
    *   **SOLID & Clean Architecture:** The `Engine` is entirely isolated. It takes a JSON state in, and returns a JSON state out. It does not know about Express or DynamoDB. This makes it 100% unit-testable.
    *   **DRY:** Standardize math utilities (e.g., `calculateCompoundInterest(principal, rate, time)`).

---

## 10. Database Design

**Amazon DynamoDB - Single Table Design (`fls-main-table`)**

*   **Partition Key (PK):** `USER#<userId>`
*   **Sort Key (SK):** Identifies the entity type.
    *   `PROFILE` -> User profile data (Email, Archetype).
    *   `STATE` -> Current simulation state JSON.
    *   `HISTORY#<month_id>` -> Historical snapshot of state for charting.

*   *Persistence Strategy:* Every time the month advances, update the `STATE` record, and append a new `HISTORY#<month_id>` record. This allows the frontend to fetch the entire history for line charts by querying `PK = USER#123 AND begins_with(SK, 'HISTORY#')`.

---

## 11. API Design

*   **`POST /api/auth/register` & `POST /api/auth/login`**: Returns JWT.
*   **`GET /api/simulation/state`**: Returns the current financial state.
*   **`POST /api/simulation/decisions`**: 
    *   *Request:* `{ "investAmount": 5000, "payoffDebtAmount": 2000 }`
    *   *Validation:* Zod schema ensures amounts are positive integers and do not exceed available cash.
*   **`POST /api/simulation/advance-month`**: Triggers the Engine loop. Returns the new state and any Random Events that occurred.
*   **`GET /api/simulation/history`**: Returns array of historical net worth for charts.

---

## 12. Implementation Roadmap

### Phase 1: Foundation & Domain Modeling
*   **Objective:** Setup repo and extract strict rules from NCFE books.
*   **Deliverables:** GitHub repo, Docker + LocalStack, Vite React app, Express TS app. Finalized JSON schema for state.
*   **Complexity:** Low.

### Phase 2: Core Simulation Engine
*   **Objective:** Build the pure math brain.
*   **Deliverables:** `engine.ts` with 100% test coverage for compounding, taxes, and loop logic.
*   **Complexity:** High (Mathematical rigor required).

### Phase 3: Persistence & APIs
*   **Objective:** Connect the brain to the database and web.
*   **Deliverables:** DynamoDB integration, Express routes, JWT Auth, Input Validation.
*   **Complexity:** Medium.

### Phase 4: Frontend Dashboard
*   **Objective:** Visualize the simulation.
*   **Deliverables:** React UI, Recharts integration, Decision forms, Event modals.
*   **Complexity:** High (State management and UX).

### Phase 5: Polish & Deployment
*   **Objective:** Ship it.
*   **Deliverables:** AWS deployment (S3 + AppRunner), final QA, presentation prep.
*   **Complexity:** Medium.

---

## 13. Engineering Documents

Before writing code, the following must exist in the repo:
1.  `docs/architecture/ARCHITECTURE.md` (Detailing the clean architecture boundaries).
2.  `docs/architecture/DATABASE.md` (DynamoDB PK/SK access patterns).
3.  `docs/architecture/API_SPEC.md` (OpenAPI/Swagger definitions).
4.  `docs/gameplay/SIMULATION_RULES.md` (The exact math formulas used in the Engine).
5.  `CONTRIBUTING.md` (Git workflows and PR requirements).

---

## 14. Testing Strategy

*   **Unit Tests (Jest/Vitest):** Absolute focus on the `Engine`. Test inputs like negative balances, edge-case tax brackets, and 120-month compound interest drift.
*   **Integration Tests (Supertest):** Verify API endpoints correctly validate JWTs and reject malformed JSON.
*   **Database Testing:** Use LocalStack to test DynamoDB queries locally.

---

## 15. Deployment Strategy

*   **Local:** `docker-compose up` spins up Node, React, and LocalStack.
*   **CI/CD:** GitHub Actions triggers on PR to `main`. Runs `npm run lint`, `npm run test`, and `npm run build`.
*   **Production:** 
    *   Frontend: AWS S3 Bucket hosted via CloudFront (or Vercel for student ease).
    *   Backend: AWS AppRunner (fully managed container service) or ECS.
    *   Database: Amazon DynamoDB (Pay-per-request billing).

---

## 16. Risk Analysis

| Risk | Type | Likelihood | Impact | Mitigation |
| :--- | :--- | :--- | :--- | :--- |
| **Floating Point Math Errors** | Technical | High | High | Use integer math (store values in paise/cents) or use `decimal.js`. |
| **Scope Creep (AI Features)** | Scope | High | Critical | Enforce strict Definition of Done. Reject non-MVP PRs. |
| **DynamoDB Query Inefficiency** | Arch | Medium | Medium | Map all access patterns in `DATABASE.md` before creating tables. |
| **Over-complex UI** | UX | Medium | High | Rely on simple Recharts instead of custom D3 animations. |

---

## 17. Future Roadmap (POST-INTERNSHIP)

*DO NOT MIX THESE WITH MVP.*
1.  **AI Storyteller:** Replace static events with LLM-generated macro-economic crises.
2.  **Generative AI Narrative Layer:** Dynamic NPC family members that react to your financial choices.
3.  **Ethical Multiplayer:** Co-op household budgets and mutual insurance resilience pools.
4.  **Dynamic Economy:** Real-time simulated stock market shared across all players.

---

## 18. Definition of Done

A task is officially "Done" when:
1.  Code is written and strictly follows ESLint/Prettier rules.
2.  Pure functions have unit tests passing.
3.  Pull Request is reviewed and approved by at least one other engineer.
4.  Feature works end-to-end locally against LocalStack.
5.  No architectural boundaries (e.g., Engine calling Database directly) are violated.

---

## 19. Engineering Milestones

*   **M1: Infrastructure Ready** (Dev environments and CI/CD active).
*   **M2: Engine Complete** (Mathematical core passes all tests).
*   **M3: Backend Complete** (APIs and DB fully integrated).
*   **M4: MVP Playable** (Frontend connects to Backend; full loop achievable).
*   **M5: Public Launch** (Deployed to AWS, presentation ready).

---

## 20. Final Execution Order

1.  Write `DATABASE.md` and `API_SPEC.md`.
2.  Initialize repo with Docker/LocalStack.
3.  Develop `SimulationEngine` (Test-Driven Development).
4.  Develop DynamoDB Repositories.
5.  Develop Express Controllers & Auth.
6.  Develop React UI (Static components).
7.  Integrate React with APIs.
8.  Deploy to AWS.
