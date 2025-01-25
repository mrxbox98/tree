# pip3 install -q -U google-generativeai

import google.generativeai as genai

api_key = "" # go to https://docs.google.com/document/d/1QcAMJKvMPwxMO1G_pKUr9XzOeZturz-Ikk0yMArQH7c/edit?usp=sharing to find the api key

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

location = "Cleveland, Ohio"
pre_prompt = f"Recommend some plants native to {location} that also fulfills the following requirements. "
prompt = "plant type: flower; plant height: short; flower color: yellow; maintenance: low."
post_prompt = " Respond with a list of plants, their scientific name, and a medium-length description. Do not include any other information. For each plant, give your response in the following format: plant name (scientific name): description."
prompt = pre_prompt + prompt + post_prompt

response = model.generate_content(prompt).text
print(response)
