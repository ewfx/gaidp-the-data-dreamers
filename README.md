# 🚀 Gen AI SQL Chatbot

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
The AI-Powered SQL Chatbot is an intelligent assistant designed to allow users to interact with databases using natural language (NL). This chatbot enables non-technical users, or those without advanced SQL knowledge, to access and retrieve data from a database simply by asking questions in conversational language. It helps businesses and teams to gain insights from their data without needing to write complex SQL queries themselves

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) attached in the artifacts under demo folder (both .mp4 & webm formats)  
🖼️ Screenshots:

<img width="239" alt="image" src="https://github.com/user-attachments/assets/250789e9-c592-4236-a532-4e23e3b42fd5" />


## 💡 Inspiration
This solution combines natural language processing (NLP) with SQL query generation to convert user queries into database-compatible SQL statements. Whether the data resides in relational databases, data warehouses, or cloud-based services, the chatbot can connect, interpret, and query the data to return relevant insights

**Target Audience who will get benefits from this solution :**

**Business Intelligence (BI)**: Enables teams to quickly access and interpret business data (e.g., sales, revenue, user engagement) without needing advanced technical skills.

**Customer Support**: Helps customer service teams quickly retrieve relevant customer data or product information.

**Marketing Analytics**: Marketing teams can ask the chatbot about campaign performance, customer behavior, or sales trends without manually running SQL queries.

**Product Development**: Teams can use the chatbot to access product usage data, customer feedback, or bug reports.

**Finance and Accounting:** Finance teams can quickly query financial data (e.g., profits, expenses, forecasts) and produce ad-hoc reports.

## ⚙️ What It Does
<img width="823" alt="image" src="https://github.com/user-attachments/assets/e8e3deac-a3e4-4402-ab44-1acf80a2f3c6" />


## 🛠️ How We Built It
We built this project using a modern tech stack to ensure scalability, efficiency, and a smooth user experience.

• **Frontend:** We used HTML for a responsive and aesthetically pleasing user interface. 

• **Backend:** The backend is powered by FastAPI & Gen AI, a high-performance Python framework that understands users queries in natural language (NLP) which connects to Microsoft SQL server and get accurate result efficiently.

• **Database:** We chose Microsoft SQL Server as our database due to its flexible & relation based storage, which is well-suited for handling AI-generated content and embeddings.

This stack allowed us to build a responsive, AI-powered application that seamlessly integrates natural language processing with a robust and scalable architecture.

## 🚧 Challenges We Faced
1. Retrieving accurate context from NLP to Database
2. Validating syntax and generating precise step definitions
3. Reducing latency in generating results responses from Natural Language questions (NLP)
4. Free version of Gen AI having some limitations on free infrastructure.


## 🏃 How to Run

##Set Up a Virtual Environment

    python -m venv venv
    venv\Scripts\activate

1️⃣ Install Dependencies:
Make sure you have Python installed, then install the required packages:
for local: You also need Ollama installed: (https://ollama.com/download/windows)
pip install fastapi uvicorn pyodbc ollama

2️⃣ Start the FastAPI Backend
Run the FastAPI server using:

uvicorn main:app --reload OR python -m uvicorn main:app --reload
By default, it will be available at:
🔗 http://127.0.0.1:8000

3️⃣ Start the UI
Open index.html in a browser.

The chatbot will welcome you and allow you to ask SQL-related queries.

🔍 Testing the API
You can manually test the API using:



## 🏗️ Tech Stack
- 🔹 Frontend: HTML
- 🔹 Backend: Fast API / Gen AI / Python Scripts
- 🔹 Database: Microsoft SQL Server


## 👥 Team
1. Venkat Panepalli
2. Srinivasaraju Kalidindi
3. Gowrisankar Gunasekaran
4. Narenkumar N
5. Maruthi Janyavula

