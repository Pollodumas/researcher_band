import streamlit as st

class UIComponents:
    @staticmethod
    def render_header():
        st.title("Blockchain Research System")
        st.markdown("""
        This system analyzes blockchain technologies using a team of AI agents:
        - 🔍 Blockchain Researcher
        - 🏗️ Architecture Analyst
        - ✅ Technical Validator
        """)

    @staticmethod
    def render_settings():
        with st.sidebar:
            st.header("Agent Settings")
            researcher_temp = st.slider(
                "Researcher Temperature",
                min_value=0.0,
                max_value=1.0,
                value=float(st.session_state.get('researcher_temperature', 0.7)),
                step=0.1,
                help="Higher values make the researcher more creative"
            )
            analyst_temp = st.slider(
                "Analyst Temperature",
                min_value=0.0,
                max_value=1.0,
                value=float(st.session_state.get('analyst_temperature', 0.5)),
                step=0.1,
                help="Higher values make the analyst more explorative"
            )
            validator_temp = st.slider(
                "Validator Temperature",
                min_value=0.0,
                max_value=1.0,
                value=float(st.session_state.get('validator_temperature', 0.3)),
                step=0.1,
                help="Higher values make the validator more flexible"
            )
            
            # Store values in session state
            st.session_state['researcher_temperature'] = researcher_temp
            st.session_state['analyst_temperature'] = analyst_temp
            st.session_state['validator_temperature'] = validator_temp
            
            return {
                "researcher_temperature": researcher_temp,
                "analyst_temperature": analyst_temp,
                "validator_temperature": validator_temp
            }

    @staticmethod
    def render_input_form():
        with st.form("research_form"):
            research_input = st.text_area(
                "Enter research topic, URL, or text",
                help="You can enter a URL, paste text, or type your research topic"
            )
            uploaded_file = st.file_uploader(
                "Upload PDF document",
                type=['pdf'],
                help="Upload a PDF document for analysis"
            )
            submit_button = st.form_submit_button("Start Analysis")
        return research_input, uploaded_file, submit_button

    @staticmethod
    def render_results(result: str):
        st.success("Analysis completed!")
        with st.expander("Research Results", expanded=True):
            st.markdown(result)