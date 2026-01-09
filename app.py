import gradio as gr
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct",
    max_new_tokens=256
)

def generate(topic):
    prompt = f"""
    You are a YouTube Shorts expert.
    Generate:
    1. Catchy Title
    2. Short Description
    3. 15 Trending Hashtags
    Topic: {topic}
    Language: Hinglish
    """
    return generator(prompt)[0]["generated_text"]

gr.Interface(
    fn=generate,
    inputs=gr.Textbox(
        label="Enter your YouTube Shorts topic",
        placeholder="Example: Funny dog video"
    ),
    outputs=gr.Textbox(label="Generated Content"),
    title="🔥 YouTube Shorts Generator",
    description="Get viral title, description & hashtags using AI"
).launch()
