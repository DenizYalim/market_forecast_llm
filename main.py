from LLMExamine import getResponse

print("main")

# LINKS = 
# Scrape headlines
# headlines = {}
# Send headlines to llm, get stock analysis
# stock analysis = {stock:string, tendency:{DECREASE, INCREASE}}

# print("Headlines of today at xxx: ")

current_context = ""
current_prompt = ""
while True:
    new_context = input("Context: ")
    if new_context and new_context != "" :
        current_context = new_context
    
    new_prompt = input("Prompt: ")
    if new_prompt and new_prompt != "":
        current_prompt = new_prompt
    
    print(getResponse(current_prompt, current_context), end='\n\n')
    

"""
Context: You are tasked to only return headlines, and headlines only
Prompt: give me RECENT news headlines related to finance

headlines given are still before 2024, which means scrapers are still needed to be set up -.-
"""