# 🤖 AI Powered Code Reviewer

A smart multi-agent AI system that reviews code, detects bugs, security issues, performance problems and generates refactored code using **Groq LLM** with GitHub integration.

---

## 🚀 Live Demo

👉 **Deployed App:** *<https://ai-code-reviewer-weqt5bvaapkgsx8w9pny8f.streamlit.app/>*

---

## ✨ Features

* 🐞 **Bug Detection Agent** – Finds logical & syntax issues
* 🔐 **Security Agent** – Detects vulnerabilities & bad practices
* ⚡ **Performance Agent** – Suggests optimization
* 🛠 **Refactor Agent** – Generates improved code
* 📂 **GitHub Integration** – Review any public repository
* 🧠 **Multi-Agent Architecture** – Specialized AI roles
* ☁ **Cloud Friendly Deployment**

---

## 🏗 Architecture

```
User Code / GitHub Repo
        │
        ▼
 Multi-Agent Prompts
        │
        ▼
     Groq LLM
        │
        ▼
Structured Review Output
```

**Agents Used**

* Bug Detection Agent
* Security Review Agent
* Performance Agent
* Refactoring Agent

---

## 🛠 Tech Stack

* **Python**
* **Streamlit**
* **Groq API (llama-3.3-70b)**
* **GitHub API**
* **Multi-Agent Prompting**

---

## 📦 Installation (Local)

```bash
git clone <your-repo-url>
cd AI-Code-Reviewer
pip install -r requirements.txt
streamlit run app.py
```

---

## 🔐 Environment Variables

Create `.env` file:

```
GROQ_API_KEY=your_key
GITHUB_TOKEN=your_token
```

For Streamlit Cloud → add in **Secrets**

---

## 🧪 Usage

### 1. Paste Code

* Enter any code snippet
* Click **Review Code**

### 2. GitHub Review

* Paste repo URL
* Select file
* Get AI analysis

### Output Includes

* Bugs
* Security Issues
* Performance Tips
* Refactored Code

---

## 🎯 Example

**Input**

```python
password="123"
for i in range(100000):
    for j in range(100000):
        print(i,j)
```

**AI Output**

* Hardcoded secret detected
* Inefficient nested loop
* Optimized refactor suggested

---

## 🧠 Design Decisions

* Multi-Agent separation for better accuracy
* Lightweight cloud inference
* Local RAG supported version
* Secure API key handling

---

## 🚧 Limitations

* Heavy RAG runs in local version
* Dependent on LLM responses
* GitHub rate limits apply

---

## 📈 Future Scope

* Full RAG microservice
* CI/CD plugin
* VS Code extension
* Custom rule engine

---

## 👩‍💻 Author

**Aastha Yadav**
AI/ML Enthusiast | Developer

---

## ⭐ If you like this project, give it a star!
