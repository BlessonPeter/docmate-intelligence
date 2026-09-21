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

------------------------------------------------------------------------------------------------------------------
| Project                      | Primary signal                                                                |
| ---------------------------- | ----------------------------------------------------------------------------- |
| **1. Document Intelligence** | RAG · Document AI ·LLM structured outputs . FAISS · AWS ECS                                           |
| **2. E-Commerce Assistant**  | Agentic RAG · LangGraph · MCP · Retrieval Optimization · RAGAS . EKS/Kubernetes                                |
| **3. Research Generator**    | Multi-Agent AI · Human-in-the-Loop · Web Grounding · Azure                    |
| **4. Semantic Image Search** | **Multimodal AI · CLIP · Vector Search · Qdrant · LLM Query Rewriting · AWS** |
| **5. Fine-Tuning on AWS** | **LLM Fine-Tuning · QLoRA · PEFT · SageMaker · Model Serving · RAG** |


Project 1 — FINAL RESUME VERSION
Document Intelligence & Conversational RAG Platform

Python · LangChain · RAG · FAISS · FastAPI · Groq · PyMuPDF · Docker · AWS ECS Fargate

* Engineered an end-to-end LLM-powered document intelligence platform supporting automated document analysis, page-level document comparison, and multi-document conversational Q&A through modular FastAPI services.
* Built a conversational RAG pipeline using LangChain LCEL and FAISS, implementing recursive text chunking, embedding-based similarity retrieval, configurable top-k search, and contextual question reformulation to support context-aware document conversations.
* Implemented session-isolated, incremental vector indexing with persisted FAISS stores and document fingerprinting, enabling dynamic document ingestion while avoiding redundant indexing of previously processed content.
* Developed structured LLM workflows for document metadata extraction and page-wise document comparison, using Pydantic schemas and JSON parsing to transform unstructured document content into structured, machine-readable outputs.
* Deployed the containerized AI application on AWS ECS Fargate, integrating Amazon ECR, VPC networking, IAM, AWS Secrets Manager, CloudWatch logging, and CloudFormation-based infrastructure provisioning.
  
| Dimension                      | Evidence in your project                                                         |
| ------------------------------ | -------------------------------------------------------------------------------- |
| **GenAI**                      | LLM workflows, structured generation, prompt architecture                        |
| **RAG**                        | LCEL + embeddings + FAISS + retrieval + contextualization                        |
| **AI Application Engineering** | Multiple document intelligence workflows                                         |
| **Backend Engineering**        | FastAPI REST services                                                            |
| **Production/Cloud**           | Docker + ECR + ECS Fargate + IAM + Secrets Manager + CloudWatch + CloudFormation |


“giving life to documents so users can communicate with them instead of manually searching through topics”—is excellent as a project narrative,
-----------------------------------------------------------------------------------------------------------------------

 Project 2 — Final Resume Version
Agentic E-Commerce Product Intelligence & Recommendation System

Python · LangChain · LangGraph · RAG · MCP · AstraDB · FastAPI · AWS EKS · Kubernetes · Docker · GitHub Actions

* Engineered an end-to-end agentic product intelligence system that ingests e-commerce product data through an ETL pipeline, indexes product information and reviews in AstraDB, and delivers context-aware product discovery and recommendations through a retrieval-augmented generation (RAG) architecture.
* Built a LangGraph-based agentic RAG workflow with conditional retrieval, relevance grading, query rewriting, and response generation, enabling the system to iteratively refine user queries when retrieved product context is insufficient.
* Optimized retrieval using AstraDB vector search, MMR-based diversification, and contextual compression, combining semantic retrieval with LLM-driven filtering to provide focused product context to the generation pipeline.
* Implemented Model Context Protocol (MCP) tool integration to expose product retrieval and web-search capabilities to the agent, enabling tool-based orchestration between the product knowledge base and external information sources.
* Productionized the application on AWS EKS using Docker, Amazon ECR, Kubernetes deployments, LoadBalancer services, CloudFormation-based infrastructure, Kubernetes Secrets, and GitHub Actions CI/CD with automated image publishing and rollout verification.
* Integrated RAGAS evaluation workflows for measuring retrieval context precision and response relevancy, establishing an evaluation layer for monitoring RAG quality.
-------------------------------------------------------------------------------------------------------
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

---------------------------------------------------------------------------------------------------------------------------


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

-------------------------------------------------------------------------------------------------------------------------------
Project 3 — Final Resume Version
### Multi-Agent Autonomous Research & Report Generation System

*Python · LangGraph · OpenAI GPT-OSS-120B · Tavily · Wikipedia API · FastAPI · Pydantic · Docker · Azure Container Apps · Jenkins*

* **Engineered an end-to-end multi-agent research system** that dynamically generates specialized analyst personas, conducts independent web-grounded research, and synthesizes multiple perspectives into structured, downloadable research reports.

* **Orchestrated stateful multi-agent workflows with LangGraph**, using parallel analyst dispatch, structured agent states, conditional workflow transitions, and persistent thread-based execution to coordinate independent research perspectives before final synthesis.

* **Implemented human-in-the-loop agent execution** with interruptible LangGraph workflows, enabling users to review generated analyst perspectives, submit feedback, update workflow state, and resume report generation without restarting the pipeline.

* **Built a multi-source web-grounded research pipeline using Tavily Search and the Wikipedia API**, dynamically generating research queries from analyst conversations and incorporating retrieved source context into analyst-specific research and report synthesis.

* **Developed automated DOCX/PDF report generation** that assembles synthesized research, introductions, conclusions, and source references into downloadable artifacts through a FastAPI backend.

* **Productionized the multi-agent application on Azure Container Apps**, containerizing the system with Docker and implementing Jenkins CI/CD automation for Azure Container Registry image publishing, deployment, secret configuration, replica management, and post-deployment health verification.


| Dimension                        | Evidence in your project                                                                                  |
| -------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Multi-Agent AI**               | Dynamic analyst personas · specialized research agents · independent perspectives · multi-agent synthesis |
| **Agentic AI**                   | LangGraph StateGraph · conditional workflows · agent dispatch · iterative research workflow               |
| **Parallel Agent Orchestration** | LangGraph `Send` dispatch for independent analyst research                                                |
| **LLM Engineering**              | OpenAI GPT-OSS-120B · structured outputs · prompt architecture · configurable model providers             |
| **Web-Grounded AI**              | **Tavily Search + Wikipedia API** · dynamically generated search queries · source-aware research context  |
| **External Tool Integration**    | Multiple knowledge-source integrations · external API consumption · retrieval/tool orchestration          |
| **Human-in-the-Loop**            | Workflow interruption · analyst review · feedback submission · state modification · workflow resumption   |
| **Stateful AI Systems**          | LangGraph state management · MemorySaver · thread IDs · resumable execution                               |
| **Structured Generation**        | Pydantic schemas · structured LLM outputs · typed analyst/search objects                                  |
| **AI Research & Synthesis**      | Independent research perspectives → analyst sections → synthesized report                                 |
| **Document Generation**          | Automated DOCX/PDF generation · source/reference compilation                                              |
| **Backend Engineering**          | FastAPI · REST APIs · authentication · report generation/status/download                                  |
| **Data Persistence**             | SQLAlchemy · SQLite · user/session persistence                                                            |
| **Containerization**             | Docker · multi-stage builds · Uvicorn · health checks                                                     |
| **CI/CD**                        | Jenkins · automated image/deployment workflow · rollout verification                                      |
| **Cloud / Deployment**           | Azure Container Apps · Azure Container Registry · external ingress · configurable replicas                |
| **Security / Configuration**     | Environment-based secrets · Azure/Jenkins credentials · externalized API configuration                    |
| **Reliability / Operations**     | Health endpoint · deployment verification · structured logging · exception handling                       |
--------------------------------------------------------------------------------------------------------------------------
project 4
### Multimodal Semantic Image Search & Retrieval System

*Python · OpenCLIP/CLIP · Qdrant · OpenAI · FastAPI · Streamlit · Docker · AWS*

* **Engineered a multimodal semantic image retrieval system** supporting natural-language-to-image and image-to-image search by mapping text and visual inputs into a shared CLIP embedding space and retrieving semantically similar images from Qdrant.

* **Built an end-to-end vector search pipeline with OpenCLIP and Qdrant**, implementing image/text embedding generation, cosine-similarity retrieval, Top-K ranking, metadata filtering, persistent vector storage, and batch image indexing.

* **Implemented LLM-powered query translation with OpenAI**, transforming conversational or ambiguous user queries into concise, image-oriented descriptions optimized for CLIP-based semantic retrieval.

* **Developed both REST and interactive interfaces** using FastAPI and Streamlit, supporting image ingestion, folder-based batch indexing, text search, image-upload search, configurable Top-K retrieval, and similarity-score visualization.

* **Optimized the application architecture for repeated inference and retrieval workloads** through reusable embedding/model components, lazy initialization, structured logging, environment-based configuration, and centralized exception handling.

* **Containerized and deployed the multimodal search application on AWS**, integrating the computer-vision retrieval pipeline, FastAPI backend, Qdrant vector database, and interactive search interface into a cloud-hosted application.


| Dimension                    | Evidence in your project                                                                              |
| ---------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Multimodal AI**            | Shared text/image embedding space · text-to-image retrieval · image-to-image retrieval                |
| **Computer Vision**          | OpenCLIP/CLIP · image embeddings · visual semantic similarity                                         |
| **Embedding Engineering**    | Text embeddings · image embeddings · normalized vector representations                                |
| **Semantic Search**          | Natural-language search → embedding → vector similarity → ranked image results                        |
| **Vector Database**          | **Qdrant** · cosine similarity · persistent vectors · collection management                           |
| **Retrieval Engineering**    | Top-K retrieval · similarity scoring · metadata/category filtering                                    |
| **LLM Engineering**          | **OpenAI query translation** · conversational query rewriting · CLIP-oriented prompt construction     |
| **Data / Indexing Pipeline** | Image ingestion · folder-based batch indexing · batch embedding generation · metadata extraction      |
| **Backend Engineering**      | **FastAPI** · REST endpoints · image upload handling · search APIs                                    |
| **Frontend / Application**   | **Streamlit** · interactive text search · image upload search · Top-K controls · result visualization |
| **ML Architecture**          | Separation of embedding, ingestion, retrieval, query translation, and API layers                      |
| **Production Engineering**   | Lazy model initialization · reusable components · structured logging · centralized exception handling |
| **Containerization**         | Docker · containerized backend/application deployment                                                 |
| **Cloud / Deployment**       | **AWS** · cloud deployment of multimodal retrieval application                                        |
| **Configuration / Security** | Environment-based configuration · externalized API credentials                                        |
| **Scalability Foundation**   | Batch indexing architecture · persistent vector storage · configurable retrieval parameters           |

-----------------------------------------------------------------------------------------------------------
project 5

### Domain-Specific LLM Fine-Tuning & Cloud Inference Pipeline

*Python · Hugging Face Transformers · TinyLlama 1.1B · QLoRA · PEFT · AWS SageMaker · S3 · API Gateway · Lambda · DynamoDB · Streamlit*

* **Fine-tuned the TinyLlama 1.1B causal language model for domain-specific pharmaceutical instruction following using 4-bit QLoRA/LoRA**, implementing parameter-efficient adaptation with targeted attention-layer updates while minimizing trainable parameters and GPU memory requirements.

* **Built the complete supervised fine-tuning pipeline**, transforming instruction/input/response data into tokenized causal-LM training sequences and configuring Hugging Face Trainer with gradient accumulation, evaluation strategy, checkpointing, and reproducible training parameters.

* **Provisioned and executed GPU-based model training on Amazon SageMaker**, managing Hugging Face training jobs, model artifacts, S3 output storage, and cloud-based compute for the fine-tuning lifecycle.

* **Deployed the fine-tuned model as a managed SageMaker inference endpoint** with a custom Hugging Face inference handler, then exposed model predictions through an **API Gateway → AWS Lambda → SageMaker** serverless inference architecture.

* **Implemented inference observability with DynamoDB-backed request/response logging** and built a Streamlit client for interactive model inference, error handling, timeout management, and API response visualization.

* **Extended the fine-tuned model with a lightweight RAG inference workflow**, retrieving relevant domain context before generation to augment the model's responses to technical pharmaceutical queries.

-------------------------------------------------------------------------------------------------------------------------------------

| Dimension                           | Evidence in your project                                                                                         |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **LLM Fine-Tuning**                 | TinyLlama 1.1B · supervised instruction tuning · causal language modeling                                        |
| **Parameter-Efficient Fine-Tuning** | **QLoRA · LoRA · PEFT · 4-bit quantization**                                                                     |
| **Model Optimization**              | Quantized model loading · targeted LoRA adaptation · reduced trainable parameter footprint                       |
| **Training Engineering**            | Hugging Face Trainer · tokenization · gradient accumulation · checkpointing · configurable training parameters   |
| **Dataset Engineering**             | Instruction/input/response formatting · tokenization · sequence truncation/padding                               |
| **GPU / Cloud Training**            | **Amazon SageMaker GPU training jobs · `ml.g5.xlarge`**                                                          |
| **Model Lifecycle / MLOps**         | Training → checkpoint/artifact generation → S3 → model deployment → endpoint inference                           |
| **Model Registry / Artifacts**      | S3-based model artifact storage and deployment workflow                                                          |
| **Model Serving**                   | SageMaker Hugging Face endpoint · custom inference handler                                                       |
| **Serverless AI Architecture**      | **API Gateway → Lambda → SageMaker Endpoint**                                                                    |
| **Inference Engineering**           | Generation parameters · request validation · error handling · timeout handling                                   |
| **AI + RAG**                        | Lightweight retrieval-augmented inference layered on top of the fine-tuned model                                 |
| **Observability**                   | DynamoDB inference logging · request IDs · timestamps · prompt/response persistence                              |
| **Frontend / Demo**                 | Streamlit interactive inference application                                                                      |
| **AWS Engineering**                 | SageMaker · S3 · Lambda · API Gateway · DynamoDB · IAM                                                           |
| **GenAI Engineering**               | Domain adaptation · instruction following · controlled text generation                                           |
| **End-to-End ML Lifecycle**         | Data preparation → fine-tuning → cloud training → artifact management → deployment → API inference → application |
