from flask import Flask, request, render_template
import google.generativeai as genai


app = Flask(__name__)



genai.configure(api_key="AIzaSyDkJgyGe5g_Cqma16QaRhcORYsGaBtZAq8")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)


@app.route("/")
def main():
    return render_template("index.html")


while True:
    app.run(debug=True)
    