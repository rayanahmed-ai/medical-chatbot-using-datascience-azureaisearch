

# ❤️ Heart Disease Semantic Retrieval using Azure AI Search & LLMs

## 📌 Overview

This project implements a **Retrieval-Augmented, data-centric AI pipeline** for **heart disease prediction and semantic querying**. Multiple heterogeneous medical datasets are unified through feature engineering, enriched using **LLM-generated natural language queries**, and indexed using **Azure AI Search** to enable semantic retrieval over structured tabular data.

The system bridges **structured medical data** with **natural language search**, following a **RAG-style architecture** commonly used in applied AI systems.

---

## 🧠 Problem Statement

Traditional machine learning pipelines operate on structured datasets but lack intuitive natural-language interaction. Conversely, LLM-based systems excel at language understanding but struggle with structured tabular data.

This project addresses the gap by:

* Converting structured medical data into a **semantically searchable format**
* Enabling **natural-language queries** over clinical datasets
* Applying **LLMs as weak supervisors** for query generation

---

## 🗂️ Datasets

* Combined **three independent heart disease datasets**
* Resolved schema inconsistencies across datasets
* Unified features into a single structured format

---

## 🔧 Feature Engineering

* Standardized clinical attributes (e.g., age, cholesterol, blood pressure)
* Handled missing values and categorical encoding
* Normalized features for downstream retrieval and modeling
* Created a final **consolidated dataset** suitable for both prediction and search

---

## 🤖 LLM-Based Synthetic Query Generation

To enable semantic retrieval over structured data:

* Used a **Large Language Model (LLM)** to generate **10–20 clinically meaningful natural-language queries per data record**
* Queries represent realistic patient or clinician questions (e.g., symptom-based, risk-factor-based)
* This synthetic query corpus acts as **weak supervision** for search and retrieval

---

## ☁️ Azure Architecture

The system leverages Microsoft Azure services:

### Components

* **Azure Table Storage**

  * Stores feature-engineered structured records
  * Stores LLM-generated natural-language queries
* **Azure AI Search**

  * Indexes Azure Tables
  * Enables semantic search over structured medical data
* **LLM (Query Generation)**

  * Generates query variants for each record
  * Enhances retrieval relevance

---

## 🔁 Retrieval Workflow

1. Structured heart disease records are stored in Azure Tables
2. LLM generates multiple natural-language queries per record
3. Azure AI Search indexes the tables
4. User queries are semantically matched against indexed data
5. Relevant records are retrieved for downstream analysis or generation

---

## 🧩 Architecture Pattern

This system follows a **Retrieval-Augmented Generation (RAG)** inspired design:

* Structured data → semantic enrichment → indexed retrieval
* LLMs used for **query synthesis**, not hallucinated answers
* Cloud-native, scalable, and modular

---

## 🧪 Key Technologies

* Python
* Azure Table Storage
* Azure AI Search
* Large Language Models (LLMs)
* Feature Engineering & Data Integration

---

## 🎯 Key Contributions

* Demonstrated semantic retrieval over structured medical datasets
* Applied LLMs for synthetic query generation and weak supervision
* Designed a scalable Azure-based search architecture
* Bridged tabular clinical data with natural-language interaction


