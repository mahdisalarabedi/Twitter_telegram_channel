from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit as st
import re


# Combine all values into one string
text_1 = " "
for i in st.session_state.outcomes.values():
    if i[0]['Body']=='patient body':
        for y in i[1].values():
               cleaned_text = re.sub(r'\bbody\b', '', y[1], flags=re.IGNORECASE)
               text_1 += " " + cleaned_text
# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_1)

# Display in Streamlit
st.title("Word Cloud")
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)
