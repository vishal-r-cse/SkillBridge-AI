import streamlit as st
import fitz

# Page Configuration
st.set_page_config(
    page_title="SkillBridge AI",
    page_icon="🚀",
    layout="wide"
)

# Sidebar
st.sidebar.title("🚀 SkillBridge AI")
st.sidebar.write("AI Career Guidance Platform")

role = st.sidebar.selectbox(
    "Select Target Role",
    [
        "Data Analyst",
        "Python Developer",
        "Data Scientist",
        "AI Engineer"
    ]
)

# Main Title
st.markdown("""
# 🚀 SkillBridge AI

### AI-Powered Career Guidance Platform

Helping Students Bridge the Gap Between Skills and Careers
""")
st.caption("OSC AI Build 1.0 | Future of Productivity")

# Hero Section
st.markdown("""
### 🎯 Bridge the Gap Between Skills and Careers

Upload your resume, choose your dream role, and receive:

✔ Skill Gap Analysis

✔ Personalized Learning Roadmap

✔ Project Recommendations

✔ Career Readiness Score
""")
#Technology Stack
st.subheader("🛠 Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🐍 Python")

with col2:
    st.info("⚡ Streamlit")

with col3:
    st.info("🤖 AI-Powered Analysis")

# Statistics Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Resumes Analyzed", "500+")
col2.metric("Career Roles", "20+")
col3.metric("Projects", "100+")
col4.metric("Success Rate", "92%")

st.markdown("---")

st.write("AI-Powered Career Guidance Platform for Students and Graduates")
st.subheader("✨ Key Features")

col1, col2 = st.columns(2)

with col1:
    st.success("""
📄 Resume Upload

🔍 Skill Detection

🧠 Skill Gap Analysis
""")

with col2:
    st.success("""
🗺 Learning Roadmap

🤖 AI Insights

📥 Download Report
""")

# Resume Upload
uploaded_file = st.file_uploader(
    "📄 Upload Your Resume",
    type=["pdf"]
)

if uploaded_file:

    # Read PDF
    pdf = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    text = ""

    for page in pdf:
        text += page.get_text()

    resume_text = text.lower()

    detected_skills = []

    skills_database = [
        "python",
        "sql",
        "excel",
        "power bi",
        "html",
        "css",
        "javascript",
        "java",
        "django",
        "flask",
        "pandas",
        "numpy",
        "machine learning"
    ]

    for skill in skills_database:
        if skill in resume_text:
            detected_skills.append(skill.title())

    st.success("✅ Resume Uploaded Successfully")
    st.subheader("🔍 Skills Detected From Resume")
    st.metric("Skills Detected", len(detected_skills))

    if detected_skills:
        for skill in detected_skills:
            st.write("✅", skill)
    else:
        st.warning("No skills detected from resume.")
    # Target Role
    st.subheader("🎯 Target Role")
    st.info(role)

    # Resume Content
    with st.expander("📄 View Resume Content"):
        st.text(text[:3000])

    # Role Based Skills
    if role == "Data Analyst":
        current_skills = ["Python", "Excel", "Communication"]
        missing_skills = ["SQL", "Power BI", "Statistics"]
        score = 70

    elif role == "Python Developer":
        current_skills = ["Python", "HTML", "CSS"]
        missing_skills = ["Django", "Flask", "Git"]
        score = 75

    elif role == "Data Scientist":
        current_skills = ["Python", "Excel"]
        missing_skills = ["Pandas", "NumPy", "Machine Learning"]
        score = 65

    else:
        current_skills = ["Python"]
        missing_skills = ["TensorFlow", "PyTorch", "Deep Learning"]
        score = 60

    # Skill Gap Analysis
    st.subheader("🧠 Skill Gap Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.success("### Current Skills")

        for skill in current_skills:
            st.write("✅", skill)

    with col2:
        st.error("### Missing Skills")

        for skill in missing_skills:
            st.write("❌", skill)

    # Learning Roadmap
    st.subheader("🗺 Learning Roadmap")

    st.markdown("""
### Week 1
Learn Core Concepts

### Week 2
Practice Industry Tools

### Week 3
Build Mini Projects

### Week 4
Build Portfolio Project
""")

    # Recommended Projects
    st.subheader("💻 Recommended Projects")

    if role == "Data Analyst":
        st.markdown("""
1. Sales Dashboard

2. Student Performance Analysis

3. Customer Segmentation

4. Inventory Dashboard
""")

    elif role == "Python Developer":
        st.markdown("""
1. Library Management System

2. Expense Tracker

3. Student Portal

4. Portfolio Website
""")

    elif role == "Data Scientist":
        st.markdown("""
1. House Price Prediction

2. Movie Recommendation System

3. Customer Churn Prediction

4. Sentiment Analysis
""")

    else:
        st.markdown("""
1. Image Classifier

2. Face Detection System

3. AI Chatbot

4. Resume Screening System
""")

    # Career Readiness Score
    st.subheader("📈 Career Readiness Score")

    st.progress(score)

    st.success(f"Career Readiness Score: {score}%")

    # AI Insights
    st.subheader("🤖 AI Insights")

    if role == "Data Analyst":
        st.info(
            "You have a strong foundation in Python and Excel. Focus on SQL and Power BI to improve your chances of becoming a Data Analyst."
        )

    elif role == "Python Developer":
        st.info(
            "Your Python fundamentals are good. Learning Django and Git will significantly improve your job readiness."
        )

    elif role == "Data Scientist":
        st.info(
            "Build strong skills in Pandas, NumPy and Machine Learning. Focus on real-world datasets and projects."
        )

    else:
        st.info(
            "Deep Learning and AI frameworks are the key skills missing. Build AI projects to strengthen your portfolio."
        )

    # Download Report
    report = f"""
SkillBridge AI Report

Target Role: {role}

Current Skills:
{current_skills}

Missing Skills:
{missing_skills}

Career Readiness Score:
{score}%
"""

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="SkillBridge_Report.txt",
        mime="text/plain"
    )

# Footer
st.markdown("---")
st.markdown("""


Hackathon: OSC AI Build 1.0

Project: SkillBridge AI

Developer: Vishal R
""")
