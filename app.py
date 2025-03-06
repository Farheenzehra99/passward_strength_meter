import streamlit as st
import re
import random
import string
from streamlit_extras.let_it_rain import rain
from streamlit_extras.stylable_container import stylable_container

# ======================  Strength Checker ======================
def check_password_strength(password):
    common_passwords = ['password', '123456', 'qwerty']
    length = len(password) >= 8
    upper = bool(re.search(r'[A-Z]', password))
    lower = bool(re.search(r'[a-z]', password))
    digit = bool(re.search(r'[0-9]', password))
    special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    common = password.lower() not in common_passwords
    sequence = not re.search(r'(.)\1{2,}', password)
    
    score = sum([length, upper, lower, digit, special, common, sequence])
    
    if score < 3: return "Weak 🔴", 25
    elif score <5: return "Medium 🟠", 50
    elif score <7: return "Strong 🟢", 75
    else: return "Very Strong 💪", 100

def generate_simple_password(length, use_upper, use_lower, use_digit, use_special):
    chars = ""
    if use_upper: chars += string.ascii_uppercase
    if use_lower: chars += string.ascii_lowercase
    if use_digit: chars += string.digits
    if use_special: chars += "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def generate_pattern_password(pattern):
    return '-'.join(str(random.choice([num*3, num+2])) for num in pattern)

# ====================== Multi-Language Setup ======================

LANGUAGES = {
    "English": {
        "home": "🏠 Home",
        "checker": "🔒 Strength Checker", 
        "generator": "🎲 Simple Generator",
        "pattern": "🔄 Pattern Generator",
        "advanced": "⚡ Advanced Generator"
    },
    "Urdu": {
        "home": "🏠 گھر",
        "checker": "🔒 طاقت چیکر",
        "generator": "🎲 سادہ جنریٹر",
        "pattern": "🔄 پیٹرن جنریٹر",
        "advanced": "⚡ جدید جنریٹر"
    }
}
# ====== Theme Management ======
def apply_theme():
    st.markdown(f"""
    <style>
        /* Hide default header */
        [data-testid="stHeader"] {{ display: none !important; }}
        
        /* Dark/Light Mode */
        [data-testid="stAppViewContainer"] {{
            background: {"#0E1117" if st.session_state.dark_mode else "#FFFFFF"} !important;
            color: {"#FFFFFF" if st.session_state.dark_mode else "#000000"} !important;
        }}
        
        /* Dark Mode Sidebar */
        [data-testid="stSidebar"] {{
            background: {"#1a1a1a" if st.session_state.dark_mode else "#f0f2f6"} !important;
        }}
        
        /* सभी टेक्स्ट को सफेद करें डार्क मोड में */
        [data-testid="stSidebar"] * {{
            color: {"#FFFFFF" if st.session_state.dark_mode else "#000000"} !important;
        }}
        
        /* ग्रेडिएंट टाइटल */
        .gradient-text {{
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: bold !important;
            border-bottom: 2px solid #4ECDC4;
            padding-bottom: 10px;
        }}
        
        /* साइडबार बटन स्टाइल */
        [data-testid="stSidebar"] .stButton > button {{
            background: {"#2d3436" if st.session_state.dark_mode else "#f8f9fa"} !important;
            color: {"#FFFFFF" if st.session_state.dark_mode else "#000000"} !important;
            border: 1px solid {"#4ECDC4" if st.session_state.dark_mode else "#FF6B6B"} !important;
        }}
    </style>
    """, unsafe_allow_html=True)
    
# Show animated stars only on home page
    if st.session_state.page == "home":
        rain(emoji="🌟", font_size=20, falling_speed=5)

def main():
    if 'page' not in st.session_state:
        st.session_state.page = "home"
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = False
    if 'lang' not in st.session_state:
        st.session_state.lang = "Urdu"

    # ====================== Sidebar ======================
    with st.sidebar:
        st.toggle("🌙 Dark Mode", key="dark_mode")
        st.selectbox("🌐 Language", options=LANGUAGES.keys(), key="lang")
        nav = LANGUAGES[st.session_state.lang]
        st.button(nav["home"], on_click=lambda: st.session_state.update(page="home"))
        st.button(nav["checker"], on_click=lambda: st.session_state.update(page="checker"))
        st.button(nav["generator"], on_click=lambda: st.session_state.update(page="generator"))
        st.button(nav["pattern"], on_click=lambda: st.session_state.update(page="pattern"))
        st.button(nav["advanced"], on_click=lambda: st.session_state.update(page="advanced"))

    apply_theme()

    # ====================== Page Content ======================
    current_lang = st.session_state.lang
    nav = LANGUAGES[current_lang]

    if st.session_state.page == "home":
        st.markdown("<h1 class='gradient-text'>🔒 Ultimate Password Tool</h1>", unsafe_allow_html=True)
        st.write("### Features:")
        st.write("- Custom Password Length (6-20 characters)")
        st.write("- Pattern-Based Generation")
        st.write("- Advanced Security Options")

    elif st.session_state.page == "checker":
        st.markdown("<h1 class='gradient-text'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)

        password = st.text_input("پاسورڈ ٹیسٹ کریں:" if current_lang == "Urdu" else "Enter Password:", type="password")
        if password:
            strength, percent = check_password_strength(password)
            st.progress(percent)
            st.subheader(f"{'نتیجہ' if current_lang == 'Urdu' else 'Result'}: {strength}")

    elif st.session_state.page == "generator":
        st.markdown("<h1 class='gradient-text'>🔧 Simple Password Generator</h1>", unsafe_allow_html=True)
        length = st.slider("پاسورڈ کی لمبائی" if current_lang == "Urdu" else "Password Length", 6, 20, 12)
        use_upper = st.checkbox("A-Z", True)
        use_lower = st.checkbox("a-z", True)
        use_digit = st.checkbox("0-9", True)
        use_special = st.checkbox("!@#", True)
        
        if st.button("پاسورڈ بنائیں" if current_lang == "Urdu" else "Generate"):
            password = generate_simple_password(length, use_upper, use_lower, use_digit, use_special)
            st.code(f"Generated Password: {password}")

    elif st.session_state.page == "pattern":
        st.markdown("<h1 class='gradient-text'>🌀 Pattern Password Generator</h1>", unsafe_allow_html=True)

        cols = st.columns(3)
        pattern = []
        for i in range(1,10):
            with cols[(i-1)%3]:
                if st.button(str(i), key=f"btn_{i}"):
                    pattern.append(i)
        if pattern:
            password = generate_pattern_password(pattern)
            st.success(f"{'آپ کا پیٹرن پاسورڈ' if current_lang == 'Urdu' else 'Your Pattern Password'}: {password}")

    elif st.session_state.page == "advanced":
        st.markdown("<h1 class='gradient-text'>🚀 Advanced Password Generator</h1>", unsafe_allow_html=True)

        length = st.slider("لمبائی" if current_lang == "Urdu" else "Length", 12, 50, 16)
        if st.button("Generate" if current_lang == "English" else "بنائیں"):
            password = generate_simple_password(length, True, True, True, True)
            st.success(f"Advanced پاسورڈ: {password}")

if __name__ == "__main__":
    main()