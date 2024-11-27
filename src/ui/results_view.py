import streamlit as st

class ResultsView:
    @staticmethod
    def render(result: str):
        st.success("Analysis completed!")
        with st.expander("Research Results", expanded=True):
            st.markdown(result)