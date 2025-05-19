import streamlit as st
from Maincode import labeling_tweets
st.markdown(
    """
    <div style='direction: rtl; text-align: right; font-size:18px;'>
    لطفا پارامترهای زیر را تنظیم کنید</div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style='direction: rtl; text-align: right; font-size:18px;'>
    تعداد توییت‌هایی که میخواهید آنالیز شون را مشخص کنید</div>
    """,
    unsafe_allow_html=True
)
st.session_state.number_of_tweets=st.number_input(label="", min_value=50)
st.markdown(
    """
    <div style='direction: rtl; text-align: right; font-size:18px;'>
    دو پارامتر زیر میزان خلاقیت مدل را مشخص میکنند.\n هرچه قدر بیشتر باشند مدل پاسخ‌های خلاقانه تری میدهد</div>
    """,
    unsafe_allow_html=True
)
st.session_state.outcomes={}
st.session_state.temperature=st.number_input(label="temperature",min_value=0.0, max_value=1.0, step=0.1)
st.session_state.top_p=st.number_input(label="top_p", min_value=0.0, max_value=1.0,step=0.1)
if st.button(label="Let's label conversations"):
    st.session_state.outcomes=labeling_tweets(st.session_state.top_p,
                                              st.session_state.temperature,
                                              st.session_state.number_of_tweets)
