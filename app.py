import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import CTransformers


# ==============================
# Function: Generate Llama Response
# ==============================
def get_llama_response(input_text, no_words, blog_style):

    llm = CTransformers(
        model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
        model_type='llama',
        config={
            'max_new_tokens': 256,
            'temperature': 0.01
        }
    )

    template = """
    Write a blog for {blog_style} job profile on the topic "{input_text}"
    within {no_words} words.
    """

    prompt = PromptTemplate(
        input_variables=["blog_style", "input_text", "no_words"],
        template=template
    )

    final_prompt = prompt.format(
        blog_style=blog_style,
        input_text=input_text,
        no_words=no_words
    )

    # ✅ NEW WAY
    response = llm.invoke(final_prompt)

    return response


# ==============================
# Streamlit UI
# ==============================

st.set_page_config(
    page_title="Generate Blogs",
    page_icon="🤖",
    layout="centered"
)

st.header("Generate Blogs 🤖")

# Input Fields
input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns(2)

with col1:
    no_words = st.text_input("No of Words")

with col2:
    blog_style = st.selectbox(
        "Writing the blog for",
        ("Researchers", "Data Scientist", "Common People")
    )

submit = st.button("Generate")

# ==============================
# Generate Output
# ==============================
if submit:
    if input_text and no_words:
        with st.spinner("Generating blog..."):
            result = get_llama_response(input_text, no_words, blog_style)
            st.write(result)
    else:
        st.warning("Please fill all fields")
