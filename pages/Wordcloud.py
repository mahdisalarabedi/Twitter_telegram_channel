from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit as st


# Combine all values into one string
text = " ".join(st.session_state.outcomes.values())

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display in Streamlit
st.title("Word Cloud")
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)
