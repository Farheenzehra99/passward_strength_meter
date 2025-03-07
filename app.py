# import streamlit as st
# import re
# import random
# import string
# from streamlit_extras.let_it_rain import rain
# from streamlit_extras.stylable_container import stylable_container

# # ======================  Strength Checker ======================
# def check_password_strength(password):
#     common_passwords = ['password', '123456', 'qwerty']
#     length = len(password) >= 8
#     upper = bool(re.search(r'[A-Z]', password))
#     lower = bool(re.search(r'[a-z]', password))
#     digit = bool(re.search(r'[0-9]', password))
#     special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
#     common = password.lower() not in common_passwords
#     sequence = not re.search(r'(.)\1{2,}', password)
    
#     score = sum([length, upper, lower, digit, special, common, sequence])
    
#     if score < 3: return "Weak 🔴", 25
#     elif score <5: return "Medium 🟠", 50
#     elif score <7: return "Strong 🟢", 75
#     else: return "Very Strong 💪", 100

# def generate_simple_password(length, use_upper, use_lower, use_digit, use_special):
#     chars = ""
#     if use_upper: chars += string.ascii_uppercase
#     if use_lower: chars += string.ascii_lowercase
#     if use_digit: chars += string.digits
#     if use_special: chars += "!@#$%^&*"
#     return ''.join(random.choice(chars) for _ in range(length))

# def generate_pattern_password(pattern):
#     # Convert pattern to keyboard-like coordinates
#     key_mapping = {
#         1: 'qw', 2: 'er', 3: 'ty',
#         4: 'as', 5: 'df', 6: 'gh',
#         7: 'zx', 8: 'cv', 9: 'bn'
#     }
    
#     password = ''
#     for num in pattern:
#         # Add special characters at even positions
#         if len(password) % 2 == 0:
#             password += random.choice('!@#$%^&*')
#         password += random.choice(key_mapping[num])
#         # Add numbers at every 3rd position
#         if len(password) % 3 == 0:
#             password += str(random.randint(0,9))
    
#     return password[:16]  # Limit to 16 characters
# # ====================== Multi-Language Setup ======================

# LANGUAGES = {
#     "English": {
#         "home": "🏠 Home",
#         "checker": "🔒 Strength Checker", 
#         "generator": "🎲 Simple Generator",
#         "pattern": "🔄 Pattern Generator",
#         "advanced": "⚡ Advanced Generator",
#          "welcome": "Welcome to Ultimate Password Tool",
#         "features": ["Custom Length (6-20)", "Pattern-Based", "Advanced Security"],
#         "generate": "Generate",
#         "clear": "Clear Pattern"
#     },
#     "Urdu": {
#         "home": "🏠 گھر",
#         "checker": "🔒 طاقت چیکر",
#         "generator": "🎲 سادہ جنریٹر",
#         "pattern": "🔄 پیٹرن جنریٹر",
#         "advanced": "⚡ جدید جنریٹر",
#          "welcome": "پاسورڈ ٹول میں خوش آمدید",
#         "features": ["مخصوص لمبائی (6-20)", "پیٹرن بیسڈ", "اعلی سیکیورٹی"],
#         "generate": "بنائیں",
#         "clear": "پیٹرن صاف کریں"
#     },
#     "Arabic": {
#         "home": "🏠 الرئيسية",
#         "checker": "🔒 فحص القوة",
#         "generator": "🎲 مولد بسيط", 
#         "pattern": "🔄 مولد النمط",
#         "advanced": "⚡ مولد متقدم",
#         "welcome": "مرحبا بكم في أداة كلمات المرور",
#         "features": ["طول مخصص (6-20)", "نمط مبتكر", "أمان متقدم"],
#         "generate": "إنشاء",
#         "clear": "مسح النمط"
#     }
# }
# # ====== Theme Management ======
# def apply_theme():
#     st.markdown(f"""
#     <style>
#         /* Hide default header */
#         [data-testid="stHeader"] {{ display: none !important; }}
        
#         /* Dark/Light Mode */
#         [data-testid="stAppViewContainer"] {{
#             background: {"#0E1117" if st.session_state.dark_mode else "#FFFFFF"} !important;
#             color: {"#FFFFFF" if st.session_state.dark_mode else "#000000"} !important;
#         }}
        
#         /* Dark Mode Sidebar */
#         [data-testid="stSidebar"] {{
#             background: {"#1a1a1a" if st.session_state.dark_mode else "#f0f2f6"} !important;
#         }}
        
#         /*side bar*/
#         [data-testid="stSidebar"] * {{
#             color: {"#FFFFFF" if st.session_state.dark_mode else "#000000"} !important;
#         }}
        
#         /* Gradient Text */
#         .gradient-text {{
#             background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
#             -webkit-background-clip: text;
#             -webkit-text-fill-color: transparent;
#             font-weight: bold !important;
#             border-bottom: 2px solid #4ECDC4;
#             padding-bottom: 10px;
#         }}
        
#         /* Sidebar Button */
#         [data-testid="stSidebar"] .stButton > button {{
#             background: {"#2d3436" if st.session_state.dark_mode else "#f8f9fa"} !important;
#             color: {"#FFFFFF" if st.session_state.dark_mode else "#000000"} !important;
#             border: 1px solid {"#4ECDC4" if st.session_state.dark_mode else "#FF6B6B"} !important;
#         }}
#     </style>
#     """, unsafe_allow_html=True)
    
# # Show animated stars only on home page
#     if st.session_state.page == "home":
#         rain(emoji="🌟", font_size=20, falling_speed=5)

# def main():
#     if 'page' not in st.session_state:
#         st.session_state.page = "home"
#     if 'dark_mode' not in st.session_state:
#         st.session_state.dark_mode = True
#     if 'lang' not in st.session_state:
#         st.session_state.lang = "English"
#     if 'pattern' not in st.session_state:
#         st.session_state.pattern = []    

#     # ====================== Sidebar ======================
#     with st.sidebar:
#         st.toggle("🌙 ڈارک موڈ" if st.session_state.lang == "Urdu" else "🌙 Dark Mode", 
#                 key="dark_mode")
#         st.selectbox("🌐 زبان" if st.session_state.lang == "Urdu" else "🌐 Language", 
#                    options=LANGUAGES.keys(), key="lang")        
#         nav = LANGUAGES[st.session_state.lang]
#         st.button(nav["home"], on_click=lambda: st.session_state.update(page="home"))
#         st.button(nav["checker"], on_click=lambda: st.session_state.update(page="checker"))
#         st.button(nav["generator"], on_click=lambda: st.session_state.update(page="generator"))
#         st.button(nav["pattern"], on_click=lambda: st.session_state.update(page="pattern"))
#         st.button(nav["advanced"], on_click=lambda: st.session_state.update(page="advanced"))

#     apply_theme()

#     # ====================== Page Content ======================
#     current_lang = st.session_state.lang
#     nav = LANGUAGES[current_lang]

#     if st.session_state.page == "home":
#         st.markdown("<h1 class='gradient-text'>🔒 Ultimate Password Tool</h1>", unsafe_allow_html=True)
#         st.write("<p>Welcome to the Ultimate Password Tool! This app provides a suite of tools to help you generate and check the strength of your passwords.</p>", unsafe_allow_html=True)
#         st.write("### Features:")
#         st.write("- Custom Password Length (6-20 characters)")
#         st.write("- Pattern-Based Generation")
#         st.write("- Advanced Security Options")

#     elif st.session_state.page == "checker":
#         st.markdown("<h1 class='gradient-text'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)

#         password = st.text_input("پاسورڈ ٹیسٹ کریں:" if current_lang == "Urdu" else "Enter Password:", type="password")
#         if password:
#             strength, percent = check_password_strength(password)
#             st.progress(percent)
#             st.subheader(f"{'نتیجہ' if current_lang == 'Urdu' else 'Result'}: {strength}")

#     elif st.session_state.page == "generator":
#         st.markdown("<h1 class='gradient-text'>🔧 Simple Password Generator</h1>", unsafe_allow_html=True)
#         length = st.slider("پاسورڈ کی لمبائی" if current_lang == "Urdu" else "Password Length", 6, 20, 12)
#         use_upper = st.checkbox("A-Z", True)
#         use_lower = st.checkbox("a-z", True)
#         use_digit = st.checkbox("0-9", True)
#         use_special = st.checkbox("!@#", True)
        
#         if st.button("پاسورڈ بنائیں" if current_lang == "Urdu" else "Generate"):
#             password = generate_simple_password(length, use_upper, use_lower, use_digit, use_special)
#             st.code(f"Generated Password: {password}")

#     elif st.session_state.page == "pattern":
#         st.markdown("<h1 class='gradient-text'>🌀 Pattern Password Generator</h1>", unsafe_allow_html=True)
    
#     # Create 3x3 grid for pattern input
#     col1, col2, col3 = st.columns(3)
#     pattern = st.session_state.get('pattern', [])
    
#     with col1:
#         if st.button('1', key='btn1'): pattern.append(1)
#         if st.button('4', key='btn4'): pattern.append(4)
#         if st.button('7', key='btn7'): pattern.append(7)
    
#     with col2:
#         if st.button('2', key='btn2'): pattern.append(2)
#         if st.button('5', key='btn5'): pattern.append(5)
#         if st.button('8', key='btn8'): pattern.append(8)
    
#     with col3:
#         if st.button('3', key='btn3'): pattern.append(3)
#         if st.button('6', key='btn6'): pattern.append(6)
#         if st.button('9', key='btn9'): pattern.append(9)

#     # Pattern actions
#     st.write(f"منتخب نمونہ: {'-'.join(map(str, st.session_state.pattern))}")    
#     if st.button("Generate Password" if current_lang == "English" else "پاسورڈ بنائیں"):
#         if len(pattern) < 3:
#             st.error("Minimum 3 points required!" if current_lang == "English" else "کم از کم 3 نقاط درکار ہیں!")
#         else:
#             password = generate_pattern_password(pattern)
#             st.success(f"{'آپ کا پیٹرن پاسورڈ' if current_lang == 'Urdu' else 'Your Pattern Password'}: {password}")
    
#     if st.button("Clear Pattern" if current_lang == "English" else "پیٹرن صاف کریں"):
#         st.session_state.pattern = []
#         st.rerun()  # Updated method for Streamlit >=1.12.0 

#     elif st.session_state.page == "advanced":
#         st.markdown("<h1 class='gradient-text'>🚀 Advanced Password Generator</h1>", unsafe_allow_html=True)

#         length = st.slider("لمبائی" if current_lang == "Urdu" else "Length", 12, 50, 16)
#         if st.button("Generate" if current_lang == "English" else "بنائیں"):
#             password = generate_simple_password(length, True, True, True, True)
#             st.success(f"Advanced پاسورڈ: {password}")

# if __name__ == "__main__":
#     main()

import streamlit as st
import re
import random
import string
from streamlit_extras.let_it_rain import rain
from streamlit_extras.stylable_container import stylable_container

# ====================== Strength Checker ======================
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
    elif score < 5: return "Medium 🟠", 50
    elif score < 7: return "Strong 🟢", 75
    else: return "Very Strong 💪", 100

def generate_simple_password(length, use_upper, use_lower, use_digit, use_special):
    chars = ""
    if use_upper: chars += string.ascii_uppercase
    if use_lower: chars += string.ascii_lowercase
    if use_digit: chars += string.digits
    if use_special: chars += "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def generate_pattern_password(pattern):
    # Convert pattern to keyboard-like coordinates
    key_mapping = {
        1: 'qw', 2: 'er', 3: 'ty',
        4: 'as', 5: 'df', 6: 'gh',
        7: 'zx', 8: 'cv', 9: 'bn'
    }
    
    password = ''
    for num in pattern:
        # Add special characters at even positions
        if len(password) % 2 == 0:
            password += random.choice('!@#$%^&*')
        password += random.choice(key_mapping[num])
        # Add numbers at every 3rd position
        if len(password) % 3 == 0:
            password += str(random.randint(0, 9))
    
    return password[:16]  # Limit to 16 characters

# ====================== Multi-Language Setup ======================
LANGUAGES = {
    "English": {
        "home": "🏠 Home",
        "checker": "🔒 Strength Checker", 
        "generator": "🎲 Simple Generator",
        "pattern": "🔄 Pattern Generator",
        "advanced": "⚡ Advanced Generator",
        "welcome": "Welcome to Ultimate Password Tool",
        "features": ["Custom Length (6-20)", "Pattern-Based", "Advanced Security"],
        "generate": "Generate",
        "clear": "Clear Pattern"
    },
    "Urdu": {
        "home": "🏠 گھر",
        "checker": "🔒 طاقت چیکر",
        "generator": "🎲 سادہ جنریٹر",
        "pattern": "🔄 پیٹرن جنریٹر",
        "advanced": "⚡ جدید جنریٹر",
        "welcome": "پاسورڈ ٹول میں خوش آمدید",
        "features": ["مخصوص لمبائی (6-20)", "پیٹرن بیسڈ", "اعلی سیکیورٹی"],
        "generate": "بنائیں",
        "clear": "پیٹرن صاف کریں"
    },
    "Arabic": {
        "home": "🏠 الرئيسية",
        "checker": "🔒 فحص القوة",
        "generator": "🎲 مولد بسيط", 
        "pattern": "🔄 مولد النمط",
        "advanced": "⚡ مولد متقدم",
        "welcome": "مرحبا بكم في أداة كلمات المرور",
        "features": ["طول مخصص (6-20)", "نمط مبتكر", "أمان متقدم"],
        "generate": "إنشاء",
        "clear": "مسح النمط"
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
        
        /* Sidebar */
        [data-testid="stSidebar"] * {{
            color: {"#FFFFFF" if st.session_state.dark_mode else "#000000"} !important;
        }}
        
        /* Gradient Text */
        .gradient-text {{
            background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: bold !important;
            border-bottom: 2px solid #4ECDC4;
            padding-bottom: 10px;
        }}
        
        /* Sidebar Button */
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
        st.session_state.dark_mode = True
    if 'lang' not in st.session_state:
        st.session_state.lang = "English"
    if 'pattern' not in st.session_state:
        st.session_state.pattern = []    

    # ====================== Sidebar ======================
    with st.sidebar:
        st.toggle("🌙 ڈارک موڈ" if st.session_state.lang == "Urdu" else "🌙 Dark Mode",
                  key="dark_mode")
        st.selectbox("🌐 زبان" if st.session_state.lang == "Urdu" else "🌐 Language",
                     options=LANGUAGES.keys(), key="lang")        
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
        st.write("<p>Welcome to the Ultimate Password Tool! This app provides a suite of tools to help you generate and check the strength of your passwords.</p>", unsafe_allow_html=True)
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
    
        # Create 3x3 grid for pattern input
        col1, col2, col3 = st.columns(3)
        pattern = st.session_state.get('pattern', [])
        
        with col1:
            if st.button('1', key='btn1'): pattern.append(1)
            if st.button('4', key='btn4'): pattern.append(4)
            if st.button('7', key='btn7'): pattern.append(7)
    
        with col2:
            if st.button('2', key='btn2'): pattern.append(2)
            if st.button('5', key='btn5'): pattern.append(5)
            if st.button('8', key='btn8'): pattern.append(8)
    
        with col3:
            if st.button('3', key='btn3'): pattern.append(3)
            if st.button('6', key='btn6'): pattern.append(6)
            if st.button('9', key='btn9'): pattern.append(9)

        # Pattern actions
        st.write(f"منتخب نمونہ: {'-'.join(map(str, st.session_state.pattern))}")    
        if st.button("Generate Password" if current_lang == "English" else "پاسورڈ بنائیں"):
            if len(pattern) < 3:
                st.error("Minimum 3 points required!" if current_lang == "English" else "کم از کم 3 نقاط درکار ہیں!")
            else:
                password = generate_pattern_password(pattern)
                st.success(f"{'آپ کا پیٹرن پاسورڈ' if current_lang == 'Urdu' else 'Your Pattern Password'}: {password}")
    
        if st.button("Clear Pattern" if current_lang == "English" else "پیٹرن صاف کریں"):
            st.session_state.pattern = []
            st.rerun()  # Updated method for Streamlit >=1.12.0 

    elif st.session_state.page == "advanced":
        st.markdown("<h1 class='gradient-text'>🚀 Advanced Password Generator</h1>", unsafe_allow_html=True)

        length = st.slider("لمبائی" if current_lang == "Urdu" else "Length", 12, 50, 16)
        if st.button("Generate" if current_lang == "English" else "بنائیں"):
            password = generate_simple_password(length, True, True, True, True)
            st.success(f"Advanced پاسورڈ: {password}")

if __name__ == "__main__":
    main()
