mkdir [project folder name]


cd [project folder name]

code . [for openning the vscode in the instance]

## for cloning any repo

git clone [url]

#### git opertions

git add .

git commit -m  "write your message "

git push 


#### MININIMUM REQ for this project

1 LLM model   hugging (free) 
2 embedding model   hugging face (free)
3 vector database
4 



install the setup .py

pip install -e .




Project 1 — FINAL RESUME VERSION
Document Intelligence & Conversational RAG Platform

Python · LangChain · RAG · FAISS · FastAPI · Groq · PyMuPDF · Docker · AWS ECS Fargate

Engineered an end-to-end LLM-powered document intelligence platform supporting automated document analysis, page-level document comparison, and multi-document conversational Q&A through modular FastAPI services.
Built a conversational RAG pipeline using LangChain LCEL and FAISS, implementing recursive text chunking, embedding-based similarity retrieval, configurable top-k search, and contextual question reformulation to support context-aware document conversations.
Implemented session-isolated, incremental vector indexing with persisted FAISS stores and document fingerprinting, enabling dynamic document ingestion while avoiding redundant indexing of previously processed content.
Developed structured LLM workflows for document metadata extraction and page-wise document comparison, using Pydantic schemas and JSON parsing to transform unstructured document content into structured, machine-readable outputs.
Deployed the containerized AI application on AWS ECS Fargate, integrating Amazon ECR, VPC networking, IAM, AWS Secrets Manager, CloudWatch logging, and CloudFormation-based infrastructure provisioning.
| Dimension                      | Evidence in your project                                                         |
| ------------------------------ | -------------------------------------------------------------------------------- |
| **GenAI**                      | LLM workflows, structured generation, prompt architecture                        |
| **RAG**                        | LCEL + embeddings + FAISS + retrieval + contextualization                        |
| **AI Application Engineering** | Multiple document intelligence workflows                                         |
| **Backend Engineering**        | FastAPI REST services                                                            |
| **Production/Cloud**           | Docker + ECR + ECS Fargate + IAM + Secrets Manager + CloudWatch + CloudFormation |


“giving life to documents so users can communicate with them instead of manually searching through topics”—is excellent as a project narrative,

## Project 2 — Final Resume Version
Agentic E-Commerce Product Intelligence & Recommendation System

Python · LangChain · LangGraph · RAG · MCP · AstraDB · FastAPI · AWS EKS · Kubernetes · Docker · GitHub Actions

Engineered an end-to-end agentic product intelligence system that ingests e-commerce product data through an ETL pipeline, indexes product information and reviews in AstraDB, and delivers context-aware product discovery and recommendations through a retrieval-augmented generation (RAG) architecture.
Built a LangGraph-based agentic RAG workflow with conditional retrieval, relevance grading, query rewriting, and response generation, enabling the system to iteratively refine user queries when retrieved product context is insufficient.
Optimized retrieval using AstraDB vector search, MMR-based diversification, and contextual compression, combining semantic retrieval with LLM-driven filtering to provide focused product context to the generation pipeline.
Implemented Model Context Protocol (MCP) tool integration to expose product retrieval and web-search capabilities to the agent, enabling tool-based orchestration between the product knowledge base and external information sources.
Productionized the application on AWS EKS using Docker, Amazon ECR, Kubernetes deployments, LoadBalancer services, CloudFormation-based infrastructure, Kubernetes Secrets, and GitHub Actions CI/CD with automated image publishing and rollout verification.
Integrated RAGAS evaluation workflows for measuring retrieval context precision and response relevancy, establishing an evaluation layer for monitoring RAG quality.
------------------------------------------------------
Data Engineering
→ scraping → ETL → structured product/review data

LLM Engineering
→ prompts → model abstraction → generation

RAG Engineering
→ embeddings → AstraDB → MMR → contextual compression

Agent Engineering
→ LangGraph → state → conditional routing → query rewriting

Tool/Protocol Engineering
→ MCP → product retrieval → web search

Backend
→ FastAPI

MLOps / DevOps
→ Docker → GitHub Actions → ECR → EKS → Kubernetes

Cloud
→ AWS infrastructure → CloudFormation → EKS

Evaluation
→ RAGAS → context precision → response relevancy
-----------------------------------------------------------
| Dimension                            | Evidence in your project                                                                                                                     |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **GenAI / LLM Engineering**          | Multi-provider LLM architecture · OpenAI/Gemini/Groq integrations · Prompt engineering · Context-aware generation                            |
| **RAG Engineering**                  | Embeddings · AstraDB vector search · MMR retrieval · contextual compression · relevance filtering · query rewriting                          |
| **Agentic AI**                       | LangGraph stateful workflow · conditional routing · retrieval grading · iterative query rewriting · tool-based orchestration                 |
| **MCP / Tool Integration**           | Model Context Protocol (MCP) server · product-retrieval tool · web-search tool · MCP client integration with the agent                       |
| **Data Engineering / ETL**           | E-commerce data acquisition · product/review extraction · data validation · transformation into LangChain Documents · vector-store ingestion |
| **Vector Databases**                 | AstraDB vector database · semantic similarity search · metadata-based retrieval                                                              |
| **Backend Engineering**              | FastAPI · REST API architecture · asynchronous MCP/tool interfaces                                                                           |
| **AI Retrieval Optimization**        | MMR diversification · `fetch_k` candidate retrieval · similarity thresholds · LLM-based contextual compression                               |
| **AI Evaluation**                    | RAGAS · context precision evaluation · response relevancy evaluation                                                                         |
| **Cloud / Infrastructure**           | AWS EKS · Amazon ECR · VPC · IAM · CloudFormation · EC2-backed Kubernetes node group                                                         |
| **Containerization / Orchestration** | Docker · Kubernetes Deployments · Kubernetes Secrets · LoadBalancer services · multi-replica deployment                                      |
| **CI/CD / DevOps**                   | GitHub Actions · automated Docker builds · ECR image publishing · Kubernetes deployment updates · rollout verification                       |
| **Security / Configuration**         | GitHub Secrets · Kubernetes Secrets · AWS IAM · externalized API credentials · environment-based configuration                               |
| **Scalable Architecture**            | Stateless containerized application · Kubernetes replica deployment · configurable EKS node-group scaling · decoupled vector database        |
