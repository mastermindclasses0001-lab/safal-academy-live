import streamlit as st
from groq import Groq

# Page Configuration - MOBILE OPTIMIZED
st.set_page_config(
    page_title="SAFAL ACADEMY LIVE",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Vivid Dark CSS Theme with Mobile-Specific Responsiveness
st.markdown("""
    <style>
    /* Hide Streamlit Default Header, Footer, and Sidebar toggle */
    [data-testid="stHeader"] {display: none !important;}
    [data-testid="collapsedControl"] {display: none !important;}
    footer {display: none !important;}
    #MainMenu {visibility: hidden;}
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        margin-top: 0rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    /* Prevent horizontal scrolling */
    .stApp {
        background-color: #050505;
        color: #ffffff;
        overflow-x: hidden;
    }
    
    /* Fixed Branding Header at the Top */
    .fixed-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #050505;
        z-index: 9999;
        padding: 10px 5px 8px 5px;
        border-bottom: 2px solid #10b981;
        box-shadow: 0 4px 15px rgba(0,0,0,0.6);
        text-align: center;
    }
    
    /* Spacer so content doesn't hide under the fixed header */
    .header-spacer {
        margin-top: 90px; 
    }

    .main-title {
        font-size: clamp(20px, 5vw, 28px);
        font-weight: 800;
        color: #00ffcc;
        text-shadow: 0px 0px 15px rgba(0, 255, 204, 0.4);
        margin: 0;
        padding: 0;
    }
    
    .sub-title {
        font-size: clamp(12px, 3vw, 15px);
        font-weight: 600;
        color: #ffcc00;
        margin: 2px 0 0 0;
        padding: 0;
    }
    
    /* Mobile Responsive Form Container */
    .form-container {
        background-color: #111111;
        padding: 15px;
        border-radius: 12px;
        border: 2px solid #ff3333;
        box-shadow: 0 8px 25px rgba(255, 51, 51, 0.2);
        margin: 10px auto;
        max-width: 600px;
    }

    /* Chat Input Text Visible and Clear */
    [data-testid="stChatInput"] textarea {
        color: #ffffff !important;
        background-color: #1a1a1a !important;
        font-size: 16px !important;
    }
    [data-testid="stChatInputContainer"] {
        border: 2px solid #3b82f6 !important;
        border-radius: 10px !important;
    }
    
    .stTextInput input, .stSelectbox select {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
        border: 1px solid #3b82f6 !important;
        border-radius: 8px;
        font-size: 15px !important;
    }
    
    .stButton button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        font-weight: bold;
        border-radius: 8px;
        border: none;
        width: 100%;
        padding: 12px;
        font-size: 16px;
        box-shadow: 0px 4px 15px rgba(16, 185, 129, 0.4);
    }
    
    .stButton button:hover {
        background: linear-gradient(135deg, #059669 100%, #047857 100%);
        color: #ffff00;
    }
    
    /* Chat Message Styling for Mobile & Laptop */
    .chat-message {
        padding: 1.2rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        line-height: 1.6;
        font-size: clamp(15px, 3.5vw, 18px);
        word-wrap: break-word; 
        overflow-x: auto; 
    }
    
    .user-message {
        background-color: #1e3a8a;
        border-left: 4px solid #3b82f6;
    }
    
    .ai-message {
        background-color: #171717;
        border-left: 4px solid #10b981;
    }
    
    .chat-header {
        font-weight: bold;
        margin-bottom: 8px;
        font-size: clamp(16px, 4vw, 19px);
    }
    
    .ai-header {
        color: #10b981;
    }
    
    .user-header {
        color: #60a5fa;
    }

    /* MEDIA QUERY FOR MOBILE DEVICES (Screens smaller than 768px) */
    @media screen and (max-width: 768px) {
        .block-container {
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
        }
        .form-container {
            padding: 10px;
            border: 1px solid #ff3333;
        }
        .header-spacer {
            margin-top: 80px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Fixed App Branding Header
st.markdown('''
    <div class="fixed-header">
        <p class="main-title">🎓 SAFAL ACADEMY LIVE</p>
        <p class="sub-title">By Ravish Sir — Interactive Step-by-Step Tutor</p>
    </div>
    <div class="header-spacer"></div>
''', unsafe_allow_html=True)

# API Key Check
try:
    api_key = st.secrets["GROQ_API_KEY"]
    client = Groq(api_key=api_key)
except KeyError:
    st.error("⚠️ API Key not found! Please configure it in Streamlit Cloud Secrets.")
    st.stop()

# Session State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []
if "test_active" not in st.session_state:
    st.session_state.test_active = False
if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = ""

# MOBILE & LAPTOP OPTIMIZED FORM SCREEN
if not st.session_state.test_active:
    st.markdown("<h4 style='color: #ff3333; text-align: center; margin-bottom: 15px;'>⚙️ Select Your Test Configuration</h4>", unsafe_allow_html=True)
    
    # Responsive container layout
    col1, col2, col3 = st.columns([0.05, 0.9, 0.05])
    with col2:
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        
        student_class = st.selectbox("Select Class", ["Class 7", "Class 8", "Class 9", "Class 10", "Class 11", "Class 12"])
        board = st.selectbox("Select Board", ["CBSE", "ICSE"])
        subject = st.selectbox("Select Subject", ["Physics", "Chemistry", "Mathematics", "Biology"])
        
        if student_class in ["Class 7", "Class 8", "Class 9", "Class 10"]:
            exam_level = st.selectbox("Select Level", ["School / Board", "Olympiad"])
        else:
            exam_level = st.selectbox("Select Level / Exam Target", ["Board Exam (NCERT)", "NEET", "JEE Mains", "JEE Advanced"])
        
        topic = st.text_input("Enter Topic Name (e.g., Aldehydes, Current Electricity):")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚀 Start Interactive Test with Ravish Sir"):
            if not topic:
                st.warning("⚠️ Kripya pehle topic ka naam enter karein!")
            else:
                st.session_state.system_prompt = (
                    f"Your name is Ravish Sir. You are the elite tutor and mentor for SAFAL ACADEMY LIVE. "
                    f"You must strictly act, speak, and refer to yourself as 'Ravish Sir'. Never break character or refer to yourself as an AI. "
                    f"You are conducting a highly rigorous interactive test for {student_class} ({board}), Subject: {subject}, Topic: {topic}, Level: {exam_level}. "
                    f"STRICT RULES:\n"
                    f"1. You must maintain extremely high academic rigor.\n"
                    f"2. Use strictly English medium.\n"
                    f"3. Exclude ALL deleted or outdated NCERT syllabus topics strictly.\n"
                    f"4. For Chemistry, use structural text-based representations (or LaTeX formatting) for reagents. DO NOT mention reaction names or descriptive headings to simulate real exam pressure.\n"
                    f"5. Format all math and chemistry formulas using standard LaTeX enclosed in single $ for inline and double $$ for block equations so Streamlit renders them beautifully.\n\n"
                    f"INTERACTIVE WORKFLOW (CRITICAL):\n"
                    f"- Begin by greeting the student warmly as Ravish Sir and presenting ONLY Question 1. Then STOP and WAIT.\n"
                    f"- The student will attempt to solve it. If the student types 'solve', you must provide ONLY STEP 1 of the solution. Then STOP.\n"
                    f"- If the student types 'N' or 'n', provide the NEXT STEP of the solution. Then STOP.\n"
                    f"- Continue this strictly one step at a time every time the student types 'N'.\n"
                    f"- Once the final answer is reached, declare that the solution is complete.\n"
                    f"- If the student types 'N' after the final answer is complete, generate and present Question 2. Then STOP.\n"
                    f"- NEVER provide the full solution at once."
                )
                
                st.session_state.test_active = True
                st.session_state.messages = [
                    {"role": "system", "content": st.session_state.system_prompt},
                    {"role": "user", "content": "Let's begin. Please give me Question 1."}
                ]
                st.rerun()
                
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # Active Test Interface
    col_a, col_b = st.columns([2.5, 1])
    with col_a:
        st.success("✅ Test Active | Type **solve** or **N**")
    with col_b:
        if st.button("🛑 Reset Test"):
            st.session_state.test_active = False
            st.session_state.messages = []
            st.rerun()

    st.markdown("---")

    # Display Chat History
    for i, msg in enumerate(st.session_state.messages):
        if msg["role"] == "system":
            continue
        if i == 1 and msg["content"] == "Let's begin. Please give me Question 1.":
            continue
        
        if msg["role"] == "user":
            css_class = "user-message"
            header = '<div class="chat-header user-header">👤 You</div>'
        else:
            css_class = "ai-message"
            header = '<div class="chat-header ai-header">🧑‍🏫 Ravish Sir</div>'
            
        st.markdown(f'<div class="chat-message {css_class}">{header}{msg["content"]}</div>', unsafe_allow_html=True)

    # Initial Question Generation
    if len(st.session_state.messages) == 2:
        with st.spinner("Ravish Sir is preparing Question 1..."):
            try:
                chat_completion = client.chat.completions.create(
                    model="qwen/qwen3.8-27b",
                    messages=st.session_state.messages,
                    temperature=0.4,
                    max_tokens=1000
                )
                response = chat_completion.choices[0].message.content
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()
            except Exception as e:
                st.error("⚠️ Connection error. Kripya test ko reset karein ya page refresh karein.")

    # Chat Input Field
    if user_input := st.chat_input("Type your answer, 'solve', or 'N' here..."):
        
        header = '<div class="chat-header user-header">👤 You</div>'
        st.markdown(f'<div class="chat-message user-message">{header}{user_input}</div>', unsafe_allow_html=True)
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        with st.spinner("Ravish Sir is typing..."):
            try:
                chat_completion = client.chat.completions.create(
                    model="qwen/qwen3.8-27b",
                    messages=st.session_state.messages,
                    temperature=0.4,
                    max_tokens=1000
                )
                
                response = chat_completion.choices[0].message.content
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()
            except Exception as e:
                st.error("⚠️ Connection mein thodi dikkat aa rahi hai. Kripya apna answer ya 'N' dobara type karein!")
