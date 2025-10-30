import streamlit as st
import json
from datetime import datetime
from fpdf import FPDF

st.set_page_config(page_title="OT Incident Response Playbook Generator", layout="wide")
st.title("🧠 OT Incident Response Playbook Generator")

st.write("""
This tool generates **ICS/OT Incident Response (IR) playbooks** tailored to your scenario.
Provide a short description (e.g., “PLC firmware tampering” or “Ransomware in historian server”) to get a structured response checklist.
""")

# Load predefined playbooks
with open("data/playbooks.json", "r") as f:
    playbooks = json.load(f)

scenario = st.text_input("Enter incident scenario (e.g., 'Ransomware in historian server')", "")

# simple keyword-based scenario matcher
def match_scenario(user_input):
    if not user_input:
        return None
    text = user_input.lower()
    for key in playbooks:
        if any(word in text for word in playbooks[key]["keywords"]):
            return key
    return "generic"

matched_key = match_scenario(scenario)

if scenario:
    st.markdown("---")
    st.subheader("Generated Incident Response Playbook")

    if matched_key and matched_key in playbooks:
        pb = playbooks[matched_key]
        st.markdown(f"### Incident Type: {pb['title']}")
        st.markdown(f"**Impact Zone:** {pb['impact_zone']}  ")
        st.markdown(f"**Purdue Level:** {pb['purdue_level']}")

        st.markdown("#### 🧭 Detection")
        st.markdown("\n".join([f"- {step}" for step in pb["detection"]]))

        st.markdown("#### 🚧 Containment")
        st.markdown("\n".join([f"- {step}" for step in pb["containment"]]))

        st.markdown("#### 👥 Roles & Responsibilities")
        for role, action in pb["roles"].items():
            st.markdown(f"- **{role}:** {action}")

        st.markdown("#### 📢 Communication Plan")
        st.markdown("\n".join([f"- {c}" for c in pb["communication"]]))

        st.markdown("#### 🔄 Recovery Steps")
        st.markdown("\n".join([f"- {r}" for r in pb["recovery"]]))

        st.markdown("#### 📚 Post-Incident Actions")
        st.markdown("\n".join([f"- {p}" for p in pb["post_incident"]]))

        st.markdown(f"_Aligned with: {pb['frameworks']}_")

        # Export as Markdown
        md_content = f"# OT IR Playbook: {pb['title']}\n\n"
        for section in ["Detection", "Containment", "Roles", "Communication", "Recovery", "Post-Incident"]:
            md_content += f"## {section}\n"
        md_content += f"\nGenerated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"

        st.download_button(
            "⬇️ Download Markdown Playbook",
            md_content,
            file_name=f"{pb['title'].replace(' ', '_')}_playbook.md",
            mime="text/markdown"
        )
    else:
        st.warning("No specific template found. Generated generic playbook.")
else:
    st.info("Enter a scenario above to generate your playbook.")