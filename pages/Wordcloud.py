from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit as st


# Combine all values into one string
text_1 = " "
for i in st.session_state.outcomes.values():
    for x, y in i.items():
        if isinstance(y, dict) and 'Category' in y:
            text_1 += " " + y['Category']
# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_1)

# Display in Streamlit
st.title("Word Cloud")
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)
