def labeling_tweets(temperature,top_p,n_of_tweets):
    import random
    import json
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import (
        ChatPromptTemplate,
        FewShotChatMessagePromptTemplate)
    import pandas as pd
    import os

    #launching the LLM

    llm=ChatOpenAI(
     model='gpt-4o',
     temperature=temperature,
     top_p=top_p)

    #loading the history of the Twitter channel
    with open(r'T.json',"r",encoding="utf-8") as f: 
        data=json.load(f)


    random_ids = [random.randint(34421, 39523) for _ in range(n_of_tweets)]
    random_ids.sort()
    list_of_messages=data["messages"]

    messages =[
        ("system", """you are an analyzer and must analyze a corpus of tweets written by physicians about
        patients’ bodies through an integrated 
        framework combining semiotics (Saussure),
        medical anthropology (Scheper-Hughes & Lock), and discourse theory (Laclau & Mouffe). 
        The aim is to visualize how different conceptualizations of the body are constructed, 
        stabilized, or contested within biomedical discourse on social media."""),
        ("human", "{sentence}")]

    prompt_template = ChatPromptTemplate.from_messages(messages)
    outcomes={}
    for id in random_ids:
        text_entities= [the_dict["text_entities"] for the_dict in list_of_messages if the_dict["id"]==id]
        if len (text_entities)>0:    
            posts=[text["text"] for text in text_entities[0] if text["type"]=="plain"]
            post=""
            for sententce in posts:
                post+=sententce
            prompt = prompt_template.invoke({"sentence":post})
            response=llm.invoke(prompt)
            outcomes[f"the post id is :{id} and the post {post}"]=response.content
    return(outcomes)


import random
import json

with open(r'T.json',"r",encoding="utf-8") as f: 
    data=json.load(f)
random_ids = [random.randint(34421, 39523) for _ in range(10)]
random_ids.sort()
list_of_messages=data["messages"]
for id in random_ids:
    text_entities= [the_dict["text_entities"] for the_dict in list_of_messages if the_dict["id"]==id]
    if len (text_entities)>0:
        print(text_entities)
        posts=[text["text"] for text in text_entities[0] if text["type"]=="plain"]
        print(posts)
