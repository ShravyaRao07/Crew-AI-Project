import streamlit as st

st.set_page_config(page_title="AI Trend Intelligence", layout="wide")

st.title("🤖 AI Trend Research Assistant")

topic = st.text_input("Enter a topic to research:")

if st.button("Generate Report"):
    if topic:
        with st.spinner("Researching... Please wait ⏳"):

            # Lazy import
            from crew import run_crew

            result = run_crew(topic)

            # Convert CrewOutput to pure string
            report_text = str(result)

        st.success("Report Generated!")

        st.markdown("## 📄 Final Report")
        st.markdown(report_text)   # ✅ USE STRING

        st.download_button(
            label="Download Report as Markdown",
            data=report_text.encode("utf-8"),  # ✅ USE STRING BYTES
            file_name="report.md",
            mime="text/markdown"
        )
    else:
        st.warning("Please enter a topic.")