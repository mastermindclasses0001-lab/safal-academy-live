import streamlit as st
from groq import Groq

# Page Configuration - MOBILE NATIVE FEEL
st.set_page_config(
    page_title="SAFAL ACADEMY LIVE",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ultra-Premium Native Android Dark Theme CSS
st.markdown("""
    <style>
    /* 1. HIDE ALL STREAMLIT GARBAGE */
    [data-testid="stHeader"] {display: none !important;}
    [data-testid="collapsedControl"] {display: none !important;}
    footer {display: none !important;}
    #MainMenu {visibility: hidden;}
    
    /* 2. TRUE EDGE-TO-EDGE FULL SCREEN */
    .block-container {
        padding-top: 5rem !important; /* Space for fixed header */
        padding-bottom: 6rem !important; /* Space for chat input */
        padding-left: 0.8rem !important;
        padding-right: 0.8rem !important;
        max-width: 100% !important;
    }

    /* 3. APP BACKGROUND & SCROLLING */
    .stApp {
        background-color: #0A0A0A !important;
        color: #FFFFFF !important;
        overflow-x: hidden;
    }
    
    /* 4. FIXED TOP APP BAR (BRANDING) */
    .fixed-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: rgba(10, 10, 10, 0.95);
        backdrop-filter: blur(10px);
        z-index: 9999;
        padding: 12px 10px;
        border-bottom: 2px solid #00E5FF;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 229, 255, 0.15);
    }
    .main-title {
        font-size: clamp(20px, 6vw, 26px);
        font-weight: 900;
        color: #00E5FF;
        letter-spacing: 1px;
        margin: 0;
        text-transform: uppercase;
    }
    .sub-title {
        font-size: clamp(12px, 3.5vw, 14px);
        font-weight: 600;
        color: #FFD700;
        margin: 2px 0 0 0;
    }
    
    /* 5. NATIVE APP FORM CONTAINER (NO WHITE BOXES) */
    .setup-card {
        background: linear-gradient(145deg, #121212, #1A1A1A);
        border-radius: 16px;
        padding: 20px 15px;
        border: 1px solid #333333;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-top: 10px;
    }
    
    /* 6. FIXING THE THIN WHITE BOXES - FORCING DARK INPUTS */
    div[data-baseweb="select"] > div, input[type="text"] {
        background-color: #1E1E1E !important;
        border: 1px solid #00E5FF !important;
        border-radius: 12px !important;
        color: #FFFFFF !important;
        font-size: 16px !important;
        padding: 12px !important;
        box-shadow: none !important;
    }
    
    /* Dropdown text color fix */
    div[data-baseweb="popover"] {
        background-color: #1E1E1E !important;
    }
    li[role="option"] {
        color: #FFFFFF !important;
        font-size: 16px !important;
    }
    
    /* 7. CHAKACHAK BUTTONS */
    .stButton > button {
        background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%) !important;
        color: #000000 !important;
        font-weight: 900 !important;
        font-size: 18px !important;
        border-radius: 12px !important;
        border: none !important;
        width: 100% !important;
        padding: 12px !important;
        text-transform: uppercase;
        box-shadow: 0 4px 15px rgba(0, 201, 255, 0.4) !important;
    }
    .stButton > button:active {
        transform: scale(0.98);
    }
    
    /* Reset Button Style Hack */
    div:nth-child(2) > .stButton > button {
        background: linear-gradient(90deg, #FF416C 0%, #FF4B2B 100%) !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 15px rgba(255, 65, 108, 0.4) !important;
    }

    /* 8. CHAT INTERFACE & TYPOGRAPHY */
    .chat-message {
        padding: 1.2rem;
        border-radius: 14px;
        margin-bottom: 15px;
        line-height: 1.5;
        font-size: 17px;
        letter-spacing: 0.3px;
        word-wrap: break-word; 
        overflow-x: auto; 
    }
    .user-message {
        background: #112240;
        border-left: 4px solid #64FFDA;
        border-top-right-radius: 4px;
    }
    .ai-message {
        background: #1E1E1E;
        border-left: 4px solid #00E5FF;
        border-top-left-radius: 4px;
    }
    .chat-header {
        font-weight: 800;
        margin-bottom: 8px;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .ai-header { color: #00E5FF; }
    .user-header { color: #64FFDA; }
    
    /* 9. CHAT INPUT AT BOTTOM (Dark Mode) */
    [data-testid="stChatInput"] {
        background-color: #0A0A0A !important;
        padding-bottom: 10px !important;
    }
    [data-testid="stChatInput"] textarea {
        background-color: #1E1E1E !important;
        color: #FFFFFF !important;
        border: 1px solid #333333 !important;
        font-size: 16px !important;
        border-radius: 20px !important;
    }
    [data-testid="stChatInputContainer"] {
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# App Branding Bar (Fixed at Top)
st.markdown('''
    <div class="fixed-header">
        <p class="main-title">🎓 SAFAL ACADEMY LIVE</p>
        <p class="sub-title">By Ravish Sir — Interactive Step-by-Step Tutor</p>
    </div>
''', unsafe_allow_html=True)

# API Key Connection
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

# ==========================================
# SCREEN 1: NATIVE APP SETUP FORM
# ==========================================
if not st.session_state.test_active:
    
    st.markdown('<div class="setup-card">', unsafe_allow_html=True)
    st.markdown("<h4 style='color: #00E5FF; text-align: center; margin-bottom: 20px; font-weight: 800;'>TEST CONFIGURATION</h4>", unsafe_allow_html=True)
    
    student_class = st.selectbox("CLASS", ["Class 7", "Class 8", "Class 9", "Class 10", "Class 11", "Class 12"])
    board = st.selectbox("BOARD", ["CBSE", "ICSE", "State Board"])
    subject = st.selectbox("SUBJECT", ["Physics", "Chemistry", "Mathematics", "Biology"])
    
    if student_class in ["Class 7", "Class 8", "Class 9", "Class 10"]:
        exam_level = st.selectbox("LEVEL", ["School / Board", "Olympiad"])
    else:
        exam_level = st.selectbox("EXAM TARGET", ["Board Exam (NCERT)", "NEET", "JEE Mains", "JEE Advanced"])
    
    topic = st.text_input("TOPIC NAME (e.g., Aldehydes, Electrostatics):")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🚀 GENERATE & START TEST"):
        if not topic:
            st.error("⚠️ Please enter a Topic Name to begin!")
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

# ==========================================
# SCREEN 2: ACTIVE LIVE CHAT
# ==========================================
else:
    # Always visible Reset Button at the top of the chat
    if st.button("🛑 END & RESET TEST"):
        st.session_state.test_active = False
        st.session_state.messages = []
        st.rerun()

    st.markdown("<hr style='border-top: 1px solid #333;'>", unsafe_allow_html=True)

    # Display Chat History
    for i, msg in enumerate(st.session_state.messages):
        if msg["role"] == "system":
            continue
        if i == 1 and msg["content"] == "Let's begin. Please give me Question 1.":
            continue
        
        if msg["role"] == "user":
            css_class = "user-message"
            header = '<div class="chat-header user-header">👤 Student</div>'
        else:
            css_class = "ai-message"
            header = '<div class="chat-header ai-header">🧑‍🏫 Ravish Sir</div>'
            
        st.markdown(f'<div class="chat-message {css_class}">{header}{msg["content"]}</div>', unsafe_allow_html=True)

    # Initial Question Generation Loader
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
                st.error("⚠️ Connection error. Please tap Reset and try again.")

    # Native App Style Chat Input Field (Fixed at bottom by Streamlit)
    if user_input := st.chat_input("Type your answer, 'solve', or 'N'..."):
        
        header = '<div class="chat-header user-header">👤 Student</div>'
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
                st.error("⚠️ Slow connection! Kripya apna answer ya 'N' dobara type karein.")
