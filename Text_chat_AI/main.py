# Let's create AI chat bot 

from openai import OpenAI

client = OpenAI(base_url= "https://openrouter.ai/api/v1",api_key="Paste your key here from open ai/ open router-> to get free ap")
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



    
