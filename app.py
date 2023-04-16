import openai
import gradio as gr

openai.api_key = "key here"

messages = [
    {"role": "system", "content": "You are a professional gym trainer ai who helps the user to ful fill their fitness needs. Provide the user with fitness tips, information about proper nutrition, and all kinds of dietary tips. Be respectful, but casual to the user."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)
