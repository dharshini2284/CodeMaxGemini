#to find the models available in Google's Generative AI API
import google.generativeai as genai

genai.configure(api_key="API_KEY")

models = genai.list_models()
for model in models:
    print(model.name)
