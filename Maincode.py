def labeling_tweets(temperature,top_p,n_of_tweets):
    import random
    import json
    import ast
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
    with open(r'selected_tweets.json',"r",encoding="utf-8") as f: 
        data=json.load(f)


    random_ids = [random.randint(144370, 144458) for _ in range(n_of_tweets)]
    random_ids.sort()
    list_of_messages=data["messages"]

    messages =[
        ("system", """you are an analyzer and must analyze a corpus of tweets written by physicians about
        patients’ bodies through an integrated 
        framework combining semiotics (Saussure),
        medical anthropology (Scheper-Hughes & Lock), and discourse theory (Laclau & Mouffe). 
        The aim is to visualize how different conceptualizations of the body are constructed, 
        stabilized, or contested within biomedical discourse on social media.
        you will do three tasks as follows:
         1.detecting the Signifiers – the linguistic forms (words/phrases)
         2.detecting the Signifieds – the conceptual meanings implied by the signifiers
         3.Classify each signifier–signified pair into one of five body types, based on Scheper-Hughes and Lock’s framework:
                Biological Body: The body as a physiological and anatomical system, measurable and treatable within biomedical frameworks.
                Psychological Body: The body as the site of emotions, fears, memories, and inner experiences—deeply subjective and affective.
                Individual/Experiential Body: The lived body, shaped by personal experiences, sensations, and everyday embodiment.
                Social Body: The body as a reflection or symbol of social order, cultural norms, gender roles, and collective values.
                Political Body: The body as a target of regulation, power, inequality, or resistance—governed through medical systems or state policies.
        the output must be a dict where the Signifier is a key and the Signifieds and their category 
        as values.
        if the provided text was not directly related to physicians discussing patients' bodies, 
         return a dict that says not related.
         in any case you must retrun a dict, not json or anything else, so our code works fine.
        avoid talking like: the provided post talks about..., the tweet talks about
        answer in english"""),
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
            outcomes[f"id is :{id} and the post {post}"]=ast.literal_eval(response.content)
    return(outcomes)


#import random
#import json
#with open(r'T.json',"r",encoding="utf-8") as f: 
#    data=json.load(f)
#random_ids = [random.randint(34421, 39523) for _ in range(10)]
#random_ids.sort()
#list_of_messages=data["messages"]
#for id in random_ids:
#    text_entities= [the_dict["text_entities"] for the_dict in list_of_messages if the_dict["id"]==id]
#    if len (text_entities)>0:
#        print(text_entities)
# #       posts=[text["text"] for text in text_entities[0] if text["type"]=="plain"]
#        print(posts)
