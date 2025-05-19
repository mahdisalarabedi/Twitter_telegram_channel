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
        ("system", "You will be provided with a chat between two or more Pancreatice cancer patients, care givers or family members. And assign an English label to the theme of their conversation"),
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