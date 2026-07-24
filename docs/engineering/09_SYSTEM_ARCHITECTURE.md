# 09. System Architecture

## 1. Purpose
This document provides a high-level overview of the entire hardware and software ecosystem required to run the Financial Literacy Simulator.

## 2. Scope
Covers the macro-level architecture, cloud components, and deployment environments for the internship MVP.

## 3. Definitions
* **VPC:** Virtual Private Cloud.
* **SPA:** Single Page Application.
* **LocalStack:** A fully functional local AWS cloud stack used to develop offline without incurring cloud costs.

## 4. High-Level Architecture Diagram

```mermaid
graph TD
    subgraph Client [User Devices]
        Web[Web Browser (React SPA)]
    end

    subgraph Cloud_Deployment [Production Environment]
        Vercel[Vercel - Frontend Hosting]
        Web --> |API Requests (JWT)| Render[Render - Backend API]
        Render --> MongoDB[(MongoDB Atlas)]
        Render --> Supabase[(Supabase Storage)]
    end

    subgraph Local_Dev [Local Developer Environment]
        Vite[Vite Dev Server] --> Express[Node.js Local Server / Docker]
        Express --> LocalDB[(MongoDB Atlas / Community)]
    end
```

## 5. Component Breakdown

### 5.1 Frontend (Presentation Layer)
A React Single Page Application (SPA) compiled with Vite. It handles routing locally, manages UI state, and visualizes the math via Recharts. UI/UX design is managed through Stitch. Deployed on **Vercel**.

### 5.2 Backend (Application Layer)
A Node.js/Express.js RESTful API. It acts as the gateway between the database and the frontend, validating inputs, checking JWT authorization, and executing the `SimulationEngine`. Containerized using Docker and deployed on **Render**.

### 5.3 Database & Storage (Persistence Layer)
- **Database**: **MongoDB Atlas** (Free Tier). A NoSQL document database perfectly suited for storing JSON game states.
- **Storage**: **Supabase Storage** (Free Tier) for managing file assets and images.

## 6. Testing & CI/CD
- **Testing**: Postman (API) + Jest (Unit tests).
- **Version Control**: Git & GitHub.

## 7. References
* [12_BACKEND_ARCHITECTURE.md](12_BACKEND_ARCHITECTURE.md)
* [13_FRONTEND_ARCHITECTURE.md](13_FRONTEND_ARCHITECTURE.md)

## 8. Future AWS Migration
As the project scales out of its MVP phase, the current stack is designed to be migrated to an enterprise AWS environment:
- **MongoDB Atlas** → **Amazon DynamoDB**
- **Supabase Storage** → **Amazon S3**
- **Vercel** → **AWS S3 + CloudFront**
- **Render** → **AWS App Runner / ECS**
- **JWT** → **AWS Cognito / IAM**
- **Logs** → **AWS CloudWatch**

## 9. Future Considerations
For multiplayer (Co-Op households), we will need to introduce API Gateway WebSockets and Amazon ElastiCache (Redis) to manage real-time synchronized state.
