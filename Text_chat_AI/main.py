# Let's create AI chat bot 

from openai import OpenAI

client = OpenAI(base_url= "https://openrouter.ai/api/v1",api_key="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")
messages =[{"role":"system","content":"You are good in eveything with perfect answers."}]
while True:
    input_user= input("You: ")
    if input_user =="exit":
        break
    messages.append ({"role":"user","content": input_user})

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini", 
                   messages = messages
    )
    reply =response.choices[0].message.content
    messages.append ({"role":"assistant","content": reply})
    print("Ai:",reply)


    