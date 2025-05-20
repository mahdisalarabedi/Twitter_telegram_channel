import streamlit as st 

st.markdown(
    "<h1 style='direction: rtl; text-align: right;'>معرفی برنامه</h1>",
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style='direction: rtl; text-align: right; font-size:18px;'>
     با سلام
     این برنامه تعداد دلخواهی از توییتر‌های موجود در کانال توییتر دانشجویان علوم پزشکی را به صورت تصادفی،
     انتخاب میکند. و از مدل زبانی شرکت OpenAI, gpt-4o
     میپرسد در هر یک از این توییت‌ها درمورد چه چیزی صحبت شده است. 
     برای شروع ابتدا به صفحه setting بروید.
     پس از مشخص کردن پارامتر های روی Let's do it! کلیک کنید. 
     منتظر بمانید تا آنالیز انجام شود. 
     سپس در صفحه Individual_conversation_label میتوانید هر توییت با پاسخی که مدل داده را مشاهده کنید. 
     در صفحه wordcloud نیز میتوانید ابر کلمات پاسخ‌های مدل را مشاهده کنید. 
    </div>
    """,
    unsafe_allow_html=True
)
