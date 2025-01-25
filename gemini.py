import google.generativeai as genai

genai.configure(api_key="AIzaSyA7ZyBsBf9RgIkyBNcapRlmr7OWC5aelQ8")
model = genai.GenerativeModel("gemini-1.5-flash")

location = "Cleveland, Ohio"
pre_prompt = f"Recommend some plants native to {location} that also fulfills the following requirements. "
prompt = "plant type: flower; plant height: short; flower color: yellow; maintenance: low."
post_prompt = " Respond with a list of plants, their scientific name, and a medium-length description. Do not include any other information. For each plant, give your response in the following format: plant name (scientific name): description."
prompt = pre_prompt + prompt + post_prompt

response = model.generate_content(prompt).text
print(response)
