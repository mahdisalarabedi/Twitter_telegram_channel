import streamlit as st
keys = list(st.session_state.outcomes.keys())
# Initialize position tracker
if "index" not in st.session_state:
    st.session_state.index = 0

# Show current item
if st.session_state.index < len(keys):
    current_key = keys[st.session_state.index]
    current_value = st.session_state.outcomes[current_key]
    st.markdown(
        f"""<div style='direction: rtl; text-align: right; font-size:18px;'>
        the tweet is current{current_key} \n
        </div>
        """,
        unsafe_allow_html=True)
    for x, y in current_value.items():
        st.markdown(
                f"""<div style='direction: ltr; text-align: left; font-size:18px;'>
                the sigfnifier is:\n {x} \n
                the signifed and the category are:
                {y}
                                                </div>
                """,
                unsafe_allow_html=True)




        # Show button to go to next item

    if st.button("➡ Next"):
        st.session_state.index += 1
else:
    st.success("🎉 All items shown.")
    if st.button("🔄 Restart"):
        st.session_state.index = 0
