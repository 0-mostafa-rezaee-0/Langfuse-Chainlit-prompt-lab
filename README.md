<h1 align="center">LangFuse + Chainlit POC</h1>

This is a minimal proof-of-concept connecting Chainlit with LangFuse for prompt tracking and observability.

## 1. Overview

Non-technical users can test prompts in a chat interface. All inputs/outputs are logged to LangFuse for versioning and analysis.

## 2. Setup

### 2.1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2.2. Configure Environment Variables

Create a `.env` file in the project root with your API keys:

```bash
OPENAI_API_KEY=sk-xxxx
LANGFUSE_PUBLIC_KEY=pk-xxxx
LANGFUSE_SECRET_KEY=sk-xxxx
LANGFUSE_HOST=https://cloud.langfuse.com
```

You can copy the template:

```bash
cp .env.example .env
```

Then edit `.env` and replace the placeholder values with your actual keys.

## 3. Run

Start the Chainlit application:

```bash
chainlit run app.py -w
```

Then open `http://localhost:8000` in your browser.

## 4. Verify

1. Send a message in the chat interface (e.g., "Explain adaptive learning in one paragraph.")
2. Go to [LangFuse → Traces](https://cloud.langfuse.com)
3. Confirm a new trace named **prompt_test** appears with:
   - Input text (your message)
   - Output text (LLM response)
   - Model name (gpt-4o-mini)
   - Latency and cost metrics

## 5. Validation Checklist

| Step             | Verification                                       |
| ---------------- | -------------------------------------------------- |
| ✅ Environment    | All packages install successfully                  |
| ✅ API Keys       | `.env` loaded correctly                            |
| ✅ LangFuse trace | Appears under your project with name `prompt_test` |
| ✅ Response       | Chat returns coherent text                         |
| ✅ Repeat         | Multiple sessions logged as separate traces        |

## 6. Next Phase

Phase 2 will introduce:

- Editable system prompt field
- Streamlit interface
- Feedback logging to LangFuse
