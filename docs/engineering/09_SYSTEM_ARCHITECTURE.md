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

    subgraph AWS_Cloud [AWS Production Environment]
        CDN[CloudFront] --> S3[S3 Bucket - Frontend Assets]
        Web --> |API Requests (JWT)| API_GW[API Gateway]
        API_GW --> AppRunner[AWS AppRunner / ECS]
        AppRunner --> DDB[(Amazon DynamoDB)]
    end

    subgraph Local_Dev [Local Developer Environment]
        Vite[Vite Dev Server] --> Express[Node.js Local Server]
        Express --> LocalDB[(LocalStack DynamoDB)]
    end
```

## 5. Component Breakdown

### 5.1 Frontend (Presentation Layer)
A React Single Page Application (SPA) compiled with Vite. It handles routing locally, manages UI state, and visualizes the math via Recharts. Deployed as static files to S3.

### 5.2 Backend (Application Layer)
A Node.js/Express.js RESTful API. It acts as the gateway between the database and the frontend, validating inputs, checking JWT authorization, and executing the `SimulationEngine`. Deployed in a Docker container on AWS AppRunner.

### 5.3 Database (Persistence Layer)
Amazon DynamoDB. A NoSQL database chosen for its extreme read/write scaling capability and perfect fit for time-series snapshot data (storing game states).

## 6. References
* [12_BACKEND_ARCHITECTURE.md](12_BACKEND_ARCHITECTURE.md)
* [13_FRONTEND_ARCHITECTURE.md](13_FRONTEND_ARCHITECTURE.md)

## 7. Future Considerations
For multiplayer (Co-Op households), we will need to introduce API Gateway WebSockets and Amazon ElastiCache (Redis) to manage real-time synchronized state.
