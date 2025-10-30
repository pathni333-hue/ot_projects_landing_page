# OT Incident Response Playbook Generator

This Streamlit app generates ICS/OT-specific incident response playbooks for scenarios like ransomware, firmware tampering, or insider threats.

## Features
- Enter or select scenario (e.g., 'PLC firmware tampering')
- AI-like keyword mapping to predefined playbooks
- Structured output (Detection, Containment, Roles, Communication, Recovery)
- Downloadable Markdown checklist
- Framework mappings (IEC 62443, NIST CSF, SANS ICS IR)

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Cloud
- Push to GitHub
- Deploy app and select `app.py`
