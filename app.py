import streamlit as st

st.set_page_config(page_title="OT Cybersecurity Toolkit", page_icon="🛠️", layout="wide")

st.title("🛡️ OT Cybersecurity Toolkit")
st.subheader("Practical, Open-Source Tools for ICS & OT Security Professionals")
st.markdown(
    "A unified collection of tools designed to enhance visibility, resilience, "
    "and security in industrial control system environments."
)

projects = [
    {
        "emoji": "🔌",
        "title": "ICS Network Segmentation Visualizer",
        "desc": "Visualize Purdue Model segmentation and detect nonadjacent or risky OT network connections.",
        "url": "https://ics-network-visualizer-ztakadu2epfhdmfxhzksrb.streamlit.app/"
    },
    {
        "emoji": "🧩",
        "title": "OT Asset Risk Scoring Tool",
        "desc": "Automate asset discovery, risk ranking, and reporting based on OT metrics and vulnerabilities.",
        "url": "https://ot-asset-risk-scoring-tool-m2xxtsgvkgvglzqcphsbn9.streamlit.app/"
    },
    {
        "emoji": "⚔️",
        "title": "OT Threat Modeling Tool",
        "desc": "Use MITRE ATT&CK for ICS and STRIDE overlays to identify threats and visualize mitigations.",
        "url": "https://otthreatmodelingtool-vcywqukdfjr8jxxr2osjpx.streamlit.app/"
    },
    {
        "emoji": "🧭",
        "title": "OT Cyber Hygiene Dashboard",
        "desc": "Assess patching, credentials, and backup readiness mapped to IEC 62443-2-1 or NIST CSF.",
        "url": "https://otcyberhygienedashboard-tyjcwuxbhavxtzx6y4crfo.streamlit.app/"
    },
    {
        "emoji": "🧠",
        "title": "OT Incident Response Playbook Generator",
        "desc": "Generate structured IR checklists and playbooks for ICS-specific scenarios.",
        "url": "https://otincidentresponseplaybookgenerator-at2p6k8jmtnqoey66qjpxv.streamlit.app/"
    },
]

st.markdown("---")
cols = st.columns(3)
for i, project in enumerate(projects):
    col = cols[i % 3]
    with col:
        st.markdown(f"### {project['emoji']} {project['title']}")
        st.write(project["desc"])
        st.markdown(f"[👉 Open App]({project['url']})", unsafe_allow_html=True)
        st.markdown("---")

st.header("📘 About This Toolkit")
st.markdown(
    "This collection brings together practical, demo-ready OT cyber projects for professionals and researchers. "
    "Each tool focuses on visibility, risk assessment, and response automation aligned with **ISA/IEC 62443** and **NIST CSF** frameworks."
)

st.markdown("---")
st.write("🔗 **Created by Pat** | [GitHub](https://github.com/) | [LinkedIn](https://linkedin.com/)")

