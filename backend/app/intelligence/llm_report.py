import requests
from app.core.config import settings

def generate_analyst_report(findings_data: dict) -> str:
    """
    Sends findings to an LLM to generate a defensive intelligence report.
    """
    if not settings.LLM_API_KEY:
        return "LLM_API_KEY not configured. Mock Report:\n- 3 Services Exposed\n- 1 High Risk Port (22)"
        
    prompt = f"Act as a Cyber Defense Analyst. Analyze this internal footprint and suggest hardening tasks: {findings_data}"
    
    # Placeholder for OpenAI / Gemini API call
    # response = requests.post("https://api.openai.com/v1/chat/completions", ...)
    
    return f"LLM Suggested Hardening Strategy based on data: {findings_data}"
