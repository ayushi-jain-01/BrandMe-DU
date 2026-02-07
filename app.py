import streamlit as st
from analyzer import analyze_text_basic, analyze_text_openai

st.set_page_config(page_title="BrandMe DU", layout="centered")

st.title("💼 BrandMe DU: AI Resume & LinkedIn Review Bot")

st.write("Upload your resume or paste your LinkedIn bio to get personalized feedback.")

# Sidebar for OpenAI toggle
use_openai = st.sidebar.checkbox("Use OpenAI (GPT-4)", value=False)
openai_key = st.sidebar.text_input("OpenAI API Key", type="password") if use_openai else None

# Input method
input_method = st.radio("Choose input method:", ("Upload Resume (.txt/.pdf)", "Paste LinkedIn Bio"))

uploaded_file = None
user_text = ""

if input_method == "Upload Resume (.txt/.pdf)":
    uploaded_file = st.file_uploader("Upload a text or PDF file", type=["txt", "pdf"])
    if uploaded_file:
        if uploaded_file.name.endswith(".txt"):
            user_text = uploaded_file.read().decode("utf-8")
        elif uploaded_file.name.endswith(".pdf"):
            import PyPDF2
            reader = PyPDF2.PdfReader(uploaded_file)
            user_text = "\n".join([page.extract_text() for page in reader.pages])
else:
    user_text = st.text_area("Paste your LinkedIn bio or resume content here:")

if st.button("Analyze"):
    if not user_text.strip():
        st.warning("Please upload a file or paste your text.")
    else:
        with st.spinner("Analyzing..."):
            if use_openai and openai_key:
                result = analyze_text_openai(user_text, openai_key)
            else:
                result = analyze_text_basic(user_text)

        st.subheader("📊 Score")
        st.write(f"**{result['score']} / 100**")

        st.subheader("💡 Suggestions")
        for tip in result["suggestions"]:
            st.markdown(f"- {tip}")

# Canva bonus suggestion
st.markdown("---")
st.subheader("🎨 Bonus: Canva Resume Templates")
st.markdown("Want a polished look? Try one of these Canva resume templates:")
st.markdown("[🖌️ Modern Resume Template](https://www.canva.com/resumes/templates/modern/)")
st.markdown("[🎯 Professional Resume Template](https://www.canva.com/resumes/templates/professional/)")
st.markdown("[🌈 Creative Resume Template](https://www.canva.com/resumes/templates/creative/)")
