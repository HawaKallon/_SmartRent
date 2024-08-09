import google.generativeai as genai

genai.configure(api_key='YOUR_API_KEY')
model = genai.GenerativeModel("gemini-1.5-flash")

def test_api():
    prompt = "Generate a sample description."
    response = model.generate_content(prompt)
    print("API Response:", response)

test_api()
