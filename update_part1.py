import re

file_path = "/Users/rahul/Desktop/financial-literacy-simulator/docs/engineering/PHASE_WISE_DEVELOPMENT_PLAN.md"
with open(file_path, "r") as f:
    content = f.read()

# 1. Product Vision -> Target Audience
target_audience_replacement = """## Target Audience
- **Primary:** High school and college students (16-24 years) entering the workforce.
- **Secondary:** Young professionals (25-35 years) struggling with debt management and early-career financial planning.

### Socio-Economic Framework and Demographic Modeling
**Purpose**: To design an educational system that addresses financial behavior, the simulator's computational frameworks must be built on the demographic realities of its target user base. 

**Design Rationale**: National surveys conducted by the National Centre for Financial Education (NCFE) indicate that while the general literacy rate in India has reached approximately 75%, the baseline financial literacy rate remains at only 27%. This knowledge gap is highly stratified by region, gender, and socio-economic background. Financial literacy drops to 24% in rural areas, 24% among women, and 21% among rural women.

At the same time, national inclusion initiatives have rapidly integrated the population into the formal banking system. Over 58 crore Jan Dhan accounts have been opened, with four-fifths situated in semi-urban or rural areas and 55% owned by women. This rapid digitization has pushed the Reserve Bank of India (RBI) Financial Inclusion Index to 67, signaling high access alongside low financial capability. This mismatch exposes first-time digital users to substantial financial risks, as they often lack the skills to evaluate products or spot digital fraud.

To model these challenges, the simulator structures its starting conditions around three distinct financial archetypes defined in national research.

| Demographic Archetype | Starting Assets (₹) | Starting Debt / Liabilities (₹) | Regular Monthly Income (₹) | Inherent Behavioral Biases |
| :--- | :--- | :--- | :--- | :--- |
| **The Student** | Cash: 15,000 | Education Loan: 3,50,000 | Stipend: 5,000 | Hyperbolic Discounting: High propensity to prioritize short-term lifestyle consumption over early-stage debt repayment. |
| **The New Entrant** | Cash: 50,000 | Credit Card Debt: 45,000 | Salary: 65,000 | Herding Behaviors: Strong tendency to copy peers by investing in speculative, high-frequency instruments. |
| **The Farmer / Gig Worker** | Cash: 20,000 | Informal Lender Debt: 1,20,000 | Variable Harvest: 18,000 (Avg) | Loss and Ambiguity Aversion: Rejection of structured savings and insurance products, viewing premiums as net losses. |

## Behavioral Design Mechanics
**Purpose**: The simulator's core mechanics are designed to counter three primary behavioral biases that prevent sustainable household wealth accumulation.

**1. Loss Aversion and Ambiguity Avoidance**
In agricultural and rural settings, households tend to hold capital-guaranteed instruments, such as gold, real estate, and fixed deposits, while actively avoiding diversified equities. Research in rural regions shows that 68% of farmers reject crop insurance, framing the recurring premium payments as a certain "loss" rather than a risk-mitigation strategy. The simulator implements this by letting users experience crop-failure or health-hazard events that wipe out non-insured capital, demonstrating the mathematical utility of risk-shifting mechanisms.

**2. Hyperbolic Discounting**
Low-income cohorts consistently prioritize short-term consumption over long-term security. For instance, roughly 73% of low-income earners opt for immediate lump-sum withdrawals from provident funds instead of securing structured, long-term annuities. The simulator penalizes high-discounting behaviors by introducing progressive mid-life inflation and health-care cost spikes that severely punish players who fail to build compound-interest engines in early game years.

**3. Herding Behaviors**
The rapid proliferation of simplified trading applications and social media forums has catalyzed speculative trading among novice investors. The simulator replicates this by generating localized "hot-asset bubbles" (e.g., speculative meme-tokens or unregulated chit funds). It utilizes a randomized decay algorithm where players who herd without analyzing underlying cash flows suffer severe capital losses."""

content = re.sub(r'## Target Audience.*?- \*\*Archetypes:\*\*.*?\n\n', target_audience_replacement + '\n\n', content, flags=re.DOTALL)

# 3. Technology Strategy -> Database & Storage (Single-Collection Polymorphic Schema)
db_replacement = """## Persistent Storage Design & Single-Collection Polymorphic Schema
**Purpose**: Group related user records in the same physical partition to speed up lookups and simplify state updates.
**Architecture Decisions**: The persistent data model relies on a single-collection pattern in MongoDB to store user profiles, simulation states, and transactional ledger entries. This design eliminates relational joins, keeping read/write response times under ten milliseconds.

```mermaid
graph TD
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px;
    classDef db fill:#f9d0c4,stroke:#333,stroke-width:2px;
    
    Collection[simulator_entities]:::db
    
    Collection --> Doc1["Document 1: pk=USER#9b1, sk=PROFILE<br/>(Metadata, Avatar, Settings)"]
    Collection --> Doc2["Document 2: pk=USER#9b1, sk=STATE#001<br/>(Month 1 Cash, Assets, Liabilities)"]
    Collection --> Doc3["Document 3: pk=USER#9b1, sk=LEDGER#100b<br/>(Historical SIP transactions, EMI payments)"]
```
*Purpose: Demonstrates how multiple distinct document types are stored together for a single user.*
*Data Flow: A single query on `pk=USER#9b1` returns the profile, current state, and full transaction history.*
*Scalability Considerations: Automatically partitions data by User ID across horizontal shards in MongoDB Atlas.*

### Complete Schema Document Models
**User Profile Document Type**
```json
{
  "_id": { "$oid": "60c72b2f9b1d4f4d2c8b4567" },
  "pk": "USER#9b1d4f4d2c8b",
  "sk": "PROFILE",
  "doc_type": "profile",
  "email": "rohan.sharma@domain.in",
  "password_hash": "$argon2id$v=19$m=65536,t=3,p=4$...",
  "display_name": "Rohan Sharma",
  "avatar_id": "vector_avatar_03",
  "archetype": "NEW_ENTRANT",
  "onboarding_complete": true,
  "created_at": { "$date": "2026-03-31T23:59:59Z" }
}
```

**Monthly State Document Type**
```json
{
  "_id": { "$oid": "60c72b2f9b1d4f4d2c8b4568" },
  "pk": "USER#9b1d4f4d2c8b",
  "sk": "STATE#001",
  "doc_type": "state",
  "month_index": 1,
  "cash_balance": 4500000,
  "credit_score": 750,
  "assets": { "equity_mf_units": 120.45, "mutual_fund_valuation": 3500000 },
  "liabilities": { "education_loan_principal": 35000000 }
}
```

**Historical Ledger Transaction Document Type**
```json
{
  "_id": { "$oid": "60c72b2f9b1d4f4d2c8b4569" },
  "pk": "USER#9b1d4f4d2c8b",
  "sk": "LEDGER#100b53c",
  "doc_type": "ledger",
  "transaction_type": "DEBIT",
  "amount": 150000,
  "category": "HAZARD_EVENT",
  "description": "UPI Collect Request Scam Loss"
}
```

### Index Optimizations
To support swift lookups on the polymorphic collection, a primary compound index is established:
```javascript
db.simulator_entities.createIndex(
  { "pk": 1, "sk": 1 },
  { name: "PrimaryPartitionIndex" }
);
```"""

content = content.replace("## Database & Storage", db_replacement + "\n\n## Database & Storage")

# 4. Auth & Security
auth_replacement = """## Authentication Architecture
**Purpose**: Protect user progress and preserve leaderboard integrity. We utilize a secure authentication system built on standard JWT patterns and one-way password hashing.
**Security Considerations**: Designed to resist side-channel & GPU attacks while maintaining fast application response times.

```mermaid
sequenceDiagram
    title Registration Flow Architecture
    actor User
    participant Auth as Auth API
    participant Mail as Amazon SES
    participant DB as MongoDB Atlas
    
    User->>Auth: Signup Request (Email, Password)
    Auth->>Auth: Zod Payload Validation
    Auth->>Auth: Argon2id Hashing
    Auth->>DB: Save User (Status: PENDING)
    Auth->>Mail: Transmit 6-digit Email Token
    Mail-->>User: Delivery of OTP
    User->>Auth: Verify OTP
    Auth->>DB: Update Status to ACTIVE
```
*Purpose: Outlines the steps taken to verify a new user identity before establishing a permanent record.*
*Security Considerations: The system secures registration by requiring a 6-character OTP sent via secure SMTP services before changing the account status.*

### Dual-Token Lifecycle and Token Storage
To protect user sessions, the backend uses a dual-token JWT architecture:

```mermaid
graph TD
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:2px;
    classDef security fill:#ffcccc,stroke:#cc0000,stroke-width:2px;
    
    Login[User Login] --> Creds{Validate Credentials}
    Creds -->|Valid| Tokens[Generate Token Pair]
    Tokens --> Access[Access Token<br/>Response Body]:::security
    Tokens --> Refresh[Refresh Token<br/>HttpOnly Cookie]:::security
```
*Purpose: Demonstrates the separation of token lifecycles.*
*Security Considerations: The short-lived access token expires after 15 minutes and is kept only in client memory to protect against XSS. The long-lived refresh token is an HttpOnly, Secure, SameSite=Strict cookie protecting against client-side scripts.*

### Authenticated State Variables
| Storage Layer Location | Lifecycle Horizon | Exposing Targets | Defensive Countermeasures |
| :--- | :--- | :--- | :--- |
| **User Access Token** | 15 Minutes | Client memory space | Prevent local storage write-outs to stop XSS extraction. |
| **Refresh Identity Token** | 7 Days | Network Cookie Engine | Enforce SameSite=Strict, Secure, and HttpOnly attributes. |
| **Password Entropy Values** | Indefinite | Database Hash | Use Argon2id iterations to slow down GPU cracking. |
| **OTP Code** | 15 Minutes | External SMTP payload | Apply short expirations, single-use codes, and strict rate limits. |

### Refresh Token Rotation with Automatic Reuse Detection
To secure long-lived sessions, the platform uses Refresh Token Rotation (RTR) with automatic reuse detection. This strategy groups all tokens issued to a user session into a single tracking lineage defined by a `family_id`.

If a refresh token is reused (indicating a potential breach), the entire token family is revoked immediately:
```typescript
app.post('/auth/refresh', async (req, res) => {
  const refreshToken = req.cookies.refreshToken;
  // Verify token and check DB...
  if (tokenRecord.consumed) {
    // Reuse detected: Revoke the entire token family immediately
    await db.deleteMany({ familyId: tokenRecord.familyId });
    res.clearCookie('refreshToken');
    return res.status(401).json({ error: 'Security breach detected.' });
  }
  // Issue new pair and mark current as consumed...
});
```

### Argon2id Computational Parameters
Passwords are protected using Argon2id. Parameters are tuned to balance security and server performance:
```typescript
import argon2 from 'argon2';

const hashConfig = {
  type: argon2.argon2id,         // Resist side-channel & GPU attacks
  memoryCost: 65536,             // 64 MiB memory hardness
  timeCost: 3,                   // 3 iterations over memory lanes
  parallelism: 4,                // 4 parallel execution threads
  saltLength: 16,                // Minimum 128-bit unique salt value
  hashLength: 32,                // 256-bit output hash width
};
```"""

# Remove old auth flows
content = re.sub(r'## Authentication Flows.*?\n## Security Architecture', auth_replacement + '\n\n## Security Architecture', content, flags=re.DOTALL)

with open(file_path, "w") as f:
    f.write(content)
print("update_part1.py executed.")
