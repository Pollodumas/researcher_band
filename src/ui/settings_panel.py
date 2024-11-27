import streamlit as st

class SettingsPanel:
    @staticmethod
    def render():
        with st.sidebar:
            st.header("Agent Settings")
            settings = {
                "researcher_temperature": st.slider(
                    "Researcher Temperature",
                    min_value=0.0,
                    max_value=1.0,
                    value=float(st.session_state.get('researcher_temperature', 0.7)),
                    step=0.1,
                    help="Higher values make the researcher more creative"
                ),
                "analyst_temperature": st.slider(
                    "Analyst Temperature",
                    min_value=0.0,
                    max_value=1.0,
                    value=float(st.session_state.get('analyst_temperature', 0.5)),
                    step=0.1,
                    help="Higher values make the analyst more explorative"
                ),
                "validator_temperature": st.slider(
                    "Validator Temperature",
                    min_value=0.0,
                    max_value=1.0,
                    value=float(st.session_state.get('validator_temperature', 0.3)),
                    step=0.1,
                    help="Higher values make the validator more flexible"
                )
            }
            
            # Store values in session state
            for key, value in settings.items():
                st.session_state[key] = value
                
            return settings