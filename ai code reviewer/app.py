import streamlit as st
from rag import get_relevant_knowledge, create_vector_db
from groq import Groq
import os
from dotenv import load_dotenv

# ---------- PAGE SETUP ----------
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🤖",
    layout="wide"
)

with st.sidebar:
    st.title("About Project")
    st.info("""
    Features:
    - Multi Agent Review  
    - RAG Knowledge  
    - GitHub Integration  
    - Refactoring  
    """)

load_dotenv()

# ----- RAG DATABASE INITIALIZE -----
if not os.path.exists("db"):
    create_vector_db()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("🤖 AI Powered Code Reviewer (Multi-Agent + RAG)")

# ---------- GITHUB SECTION ----------
st.markdown("## 📂 Review from GitHub")

repo_url = st.text_input("Enter GitHub Repo URL")

selected_code = ""

if repo_url:
    from github_helper import get_repo_files, get_file_content

    files = get_repo_files(repo_url)

    file = st.selectbox("Select File", files)

    if file:
        selected_code = get_file_content(repo_url, file)
        st.code(selected_code)

# ---------- CODE INPUT ----------
code = selected_code if selected_code else st.text_area("Paste your code here")

# ---------- REVIEW BUTTON ----------
if st.button("Review Code"):

    with st.spinner("AI Agents analyzing code..."):

        # ----- RAG CONTEXT -----
        context = get_relevant_knowledge(code)

        # =============== AGENT PROMPTS ===============

        bug_prompt = f"""
        You are BUG DETECTION AGENT.
        Use this knowledge base:
        {context}

        Find:
        - syntax errors
        - logical bugs
        - edge cases
        - bad practices

        Code:
        {code}
        """

        security_prompt = f"""
        You are SECURITY AGENT.
        Use this knowledge base:
        {context}

        Find:
        - hardcoded secrets
        - input validation issues
        - authentication problems
        - vulnerabilities

        Code:
        {code}
        """

        performance_prompt = f"""
        You are PERFORMANCE AGENT.
        Use this knowledge base:
        {context}

        Suggest:
        - time complexity improvements
        - loop optimization
        - memory issues
        - better structures

        Code:
        {code}
        """

        refactor_prompt = f"""
        You are REFACTOR AGENT.
        Use this knowledge base:
        {context}

        Return ONLY improved version of code with best practices.

        Code:
        {code}
        """

        # =============== CALL AGENTS ===============

        bug_res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": bug_prompt}]
        )

        sec_res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": security_prompt}]
        )

        perf_res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": performance_prompt}]
        )

        ref_res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": refactor_prompt}]
        )

    # =============== OUTPUT SECTION ===============

    st.subheader("🔍 Multi-Agent Review Result")

    st.markdown("## 🐞 Bugs (Bug Agent)")
    st.write(bug_res.choices[0].message.content)

    st.markdown("## 🔐 Security (Security Agent)")
    st.write(sec_res.choices[0].message.content)

    st.markdown("## ⚡ Performance (Performance Agent)")
    st.write(perf_res.choices[0].message.content)

    st.markdown("## ✨ Refactored Code (Refactor Agent)")
    st.code(ref_res.choices[0].message.content)
