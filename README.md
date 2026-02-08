# Llama 2 Chatbot with Streamlit and LangChain

This project utilizes the Llama 2 Large Language Model (LLM) to generate blog content based on user input. It features a simple web interface built with Streamlit and uses LangChain for LLM integration.

![Streamlit App Screenshot](images/app_screenshot.png)

![Streamlit App Screenshot](images/app_screenshot.png)

## Features

- **Blog Generation**: Generate blogs for different target audiences (Researchers, Data Scientists, Common People).
- **Customizable**: Specify the blog topic and word count.
- **Local LLM**: Runs locally using the quantized Llama 2 model (GGML format).

## Prerequisites

- Python 3.9 or higher
- 8GB+ RAM recommended

## Setup Instructions

1.  **Clone the repository** (if applicable) or navigate to the project directory.

2.  **Download the Model**:
    - Create a directory named `models` in the root folder.
    - Download the Llama 2 model file `llama-2-7b-chat.ggmlv3.q8_0.bin` from Hugging Face and place it in the `models/` directory.
    - [Download Link](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q8_0.bin)

3.  **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

4.  **Activate the Virtual Environment**:
    - **Windows**:
      ```bash
      venv\Scripts\activate
      ```
    - **Mac/Linux**:
      ```bash
      source venv/bin/activate
      ```

5.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the Streamlit app, execute the following command in your terminal:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501` (or another port if 8501 is busy).

## Project Structure

- `app.py`: Main application script containing the Streamlit UI and LangChain logic.
- `models/`: Directory to store the downloaded Llama 2 model.
- `requirements.txt`: List of Python dependencies.
- `venv/`: Virtual environment directory (excluded from git).
