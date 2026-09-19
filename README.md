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

