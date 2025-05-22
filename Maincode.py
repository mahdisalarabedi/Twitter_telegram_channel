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

#structuring the output
#from langchain.output_parsers import ResponseSchema, StructuredOutputParser

#response_schema = [
#    ResponseSchema(
#        name='dict_1',
#        description='A dictionary with one item. The key is always "Body", and the value is the body type discussed in the post: "patient body", "doctor body", or "not related".'
#    ),
#    ResponseSchema(
#        name='dict_2',
#        description=(
#            'A dictionary with multiple items. Each key is a "signifier", and the value is a list with two items: '
#            'the first is the "signified", and the second is the "category" (e.g., Biological, Social, Political, Experiential/Individual, Psychological etc.).'
#        )
#    )
#]
#output_parser = StructuredOutputParser.from_response_schemas(response_schema)







    random_ids = [random.randint(144370, 144458) for _ in range(n_of_tweets)]
    random_ids.sort()
    list_of_messages=data["messages"]
    messages =[
    ("system", """you are an analyzer and must analyze a corpus of tweets written by physicians about
    patients’ or their own bodies through:
    an integrated framework combining semiotics (Saussure),medical anthropology (Scheper-Hughes & Lock), and discourse theory (Laclau & Mouffe). 
    The aim is to visualize how different conceptualizations of the body are constructed, 
    stabilized, or contested within biomedical discourse on social media.
    you will do three tasks as follows:
    1.detecting whether the tweet talks about 'doctors' or 'patients' 
     and in some talks about the patients/community
    2.detecting the Signifiers – the linguistic forms (words/phrases)
    3.detecting the Signifieds – the conceptual meanings implied by the signifiers
    4.Classify each signifier–signified pair into one of five body types, based on Scheper-Hughes and Lock’s framework, don't say body at
    the end just the type:
        Biological: The body as a physiological and anatomical system, measurable and treatable within biomedical frameworks.
        Psychological: The body as the site of emotions, fears, memories, and inner experiences—deeply subjective and affective.
        Individual/Experiential: The lived body, shaped by personal experiences, sensations, and everyday embodiment.
        Social: The body as a reflection or symbol of social order, cultural norms, gender roles, and collective values.
        Political Body: The body as a target of regulation, power, inequality, or resistance—governed through medical systems or state policies 
        You must return only a List of two dictionaries and notice, if the value of first dict was 'not related' don't proceed the next dict:
        a list of one dict in this case:\n
         {{'Body': <one of: patient body, doctor body, or not related>}}
         {{signifier: [signified, category], ...}}.
    """),
    ("human", "here's the tweet:{sentence}")]

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
        #parsed_response=output_parser.parse(response.content)
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
