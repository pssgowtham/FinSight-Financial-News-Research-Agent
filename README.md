# FinSight-Financial-News-Research-Assistant

FinSight is a user-friendly research assistant designed to simplify financial news analysis. Users can load article URLs, process their content, and interact with an AI system to extract insights related to the stock market and business trends.

## 🚀 Features
- Load and process financial news articles from URLs  
- Summarize articles with sources  
- Ask natural language questions about the stock market and business trends  
- Perform calculations (percentages, growth rates, ratios, etc.)  
- Search the web for the latest financial information  
- Interactive chat-style UI with auto-scroll  

## 📂 Project Structure
```

FinSight/
│── backend/        # All LLM, tools, and retrieval logic
│── frontend/       # Streamlit UI and chat interface
│── requirements.txt
│── app.py         # Entry point
│── .env            # API keys and environment variables

````

## ⚙️ Installation & Setup
```bash
# Clone repo
git clone <your-repo-url>
cd FinSight

# Create virtual environment
python3 -m venv venv
source venv/bin/activate   # (On macOS/Linux)
# venv\Scripts\activate    # (On Windows)

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
````

## ▶️ Run the App

```bash
streamlit run app.py
```

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_api_key_here
```

## 📝 License

This project is for educational and research purposes only.
