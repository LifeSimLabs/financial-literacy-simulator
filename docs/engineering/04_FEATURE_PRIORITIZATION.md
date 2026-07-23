# 04. Feature Prioritization

## 1. Purpose
This document categorizes all proposed features across the entire project lifecycle, ensuring the engineering team remains strictly focused on the Internship MVP and does not succumb to scope creep.

## 2. Scope
Applies to all GitHub Issues, Epics, and User Stories. Every task must be mapped to one of these phases.

## 3. Definitions
* **MoSCoW Method:** Must Have, Should Have, Could Have, Won't Have (Right now).

## 4. Phase Breakdown

### Phase 1: Must Build (The Engine & Infrastructure)
These features are the absolute minimum required to prove the technical competency of the internship.
* **Features:**
  * Docker + LocalStack Development Environment.
  * Node.js + Express + TypeScript scaffolding.
  * DynamoDB Database Schema (`USER`, `STATE`, `HISTORY`).
  * Pure `SimulationEngine` (Math for Salary, Expenses, Debt Amortization, Compound Interest).
  * API Endpoints for State Retrieval and Advancement.
* **Why:** Without these, the application has no mathematical integrity and no persistence.

### Phase 2: Should Build (The UI & Experiential Loop)
These features deliver the actual user value, satisfying the "experiential learning" requirement.
* **Features:**
  * React + Vite Frontend scaffolding.
  * JWT Authentication (Login/Register).
  * Main Dashboard (Displaying Net Worth, Cash, Assets, Liabilities).
  * Decision Forms (Allocating money to pay off debt or invest).
  * Historical Charts (Recharts line graphs showing the consequences of time).
* **Why:** The engine means nothing if the user cannot interact with it or see the visual compounding over decades.

### Phase 3: Good Enhancement (Friction & Hazards)
These features introduce realism and satisfy the requirement to teach resilience.
* **Features:**
  * Static Random Event Engine.
  * Hardcoded events sourced from `BEAWARE_Modus_Operandi_of_Financial_Fraudsters.md` (e.g., KYC Scam, Medical Emergency).
  * Bankruptcy State (Game Over screen if Debt > Assets * 1.5 and Cash < 0).
* **Why:** Perfect financial progression is unrealistic. Players must learn to build emergency funds to survive these shocks.

### Phase 4: Future Startup Features (Post-Internship)
*DO NOT BUILD THESE DURING THE INTERNSHIP.*
* **Features:**
  * Generative AI NPCs (Dynamic family members demanding money).
  * AI Storyteller (An adaptive engine that punishes over-leverage with targeted recessions).
  * Co-Op Multiplayer Households (Two players managing one budget).
  * Mutual Insurance Pools (Players pooling resources to protect against the Event Engine).
* **Why:** High technical risk, massive scope, undefined APIs. They are excellent startup features but fatal to a time-boxed internship.

## 5. References
* [20_PROJECT_ROADMAP.md](20_PROJECT_ROADMAP.md)
* `docs/methodology/SDLC_2.md`

## 6. Future Considerations
When Phase 4 begins, the team must undergo a complete re-architecture phase to evaluate WebSocket support for multiplayer and asynchronous queue management for LLM inference.
