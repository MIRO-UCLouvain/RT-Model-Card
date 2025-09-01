"""Module for the main application screen."""

from __future__ import annotations

import streamlit as st

ABOUT_TEXT = (
    "This model card aims to **enhance transparency and standardize the "
    "reporting of artificial intelligence (AI)-based applications** in "
    "the field of **Radiation Therapy**. It is designed for use by "
    "professionals in both research and clinical settings to support "
    "these objectives. Although it includes items useful for current"
    " regulatory requirements, **it does not replace or fulfill "
    "regulatory requirements such as the EU Medical Device Regulation"
    " or equivalent standards**."
)

# Main page
def main() -> None:
    """Main page for the application."""
    st.markdown(
        """
        <style>
        .block-container p, .block-container li {
            text-align: justify;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("## About Model Cards")

    st.markdown(ABOUT_TEXT)

    st.markdown("<br>", unsafe_allow_html=True)

    # Lazy imports used to avoid circular imports
    if st.button("Create a Model Card", use_container_width=True):
        from app.ui.screens.task_selector import (  # noqa: PLC0415
            task_selector_page,
        )

        st.session_state.runpage = task_selector_page
        st.rerun()

    if st.button("Load a Model Card", use_container_width=True):
        from app.ui.screens.load_model_card import (  # noqa: PLC0415
            load_model_card_page,
        )

        st.session_state.runpage = load_model_card_page
        st.rerun()
