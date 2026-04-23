from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import re 
from fastapi.templating import Jinja2Templates # UI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Text Summarizer App", description="Text Summarization using T5", version="1.0")

model = T5ForConditionalGeneration.from_pretrained("./saved_summary_model")
tokenizer = T5Tokenizer.from_pretrained("./saved_summary_model")

# device
if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

model.to(device)

templates = Jinja2Templates(directory="templates")

class DialogueInput(BaseModel):
    dialogue: str

def clean_data(text):
    text = re.sub(r"\r\n", " ", text) # lines
    text = re.sub(r"\s+", " ", text) # spaces
    text = re.sub(r"<.*?>", " ", text) # html tags <p> <h1>
    text = text.strip()
    return text

def post_process_summary(text):
    if not text:
        return ""
    # Capitalize the first letter
    text = text.capitalize()
    # Add a period at the end if it's missing
    if text and text[-1] not in ".!?":
        text += "."
    # Ensure capitalization after periods
    text = re.sub(r"([.!?]\s+)([a-z])", lambda m: m.group(1) + m.group(2).upper(), text)
    return text

def summarize_dialogue(dialogue : str) -> str:
    dialogue = clean_data(dialogue) # clean
    
    # Add T5 prefix
    t5_input = "summarize: " + dialogue

    # tokenize
    inputs = tokenizer(
        t5_input,
        padding="max_length",
        max_length=512,
        truncation=True,
        return_tensors="pt"
    ).to(device)

    # generate the summary => token ids
    model.to(device)
    targets = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=150,
        num_beams=4,
        early_stopping=True
    )
    
    # decoded our output
    summary = tokenizer.decode(targets[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
    return post_process_summary(summary)


# API endpoints
@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):
    if not dialogue_input.dialogue.strip():
        return {"summary": "Please provide some text to summarize."}
    try:
        summary = summarize_dialogue(dialogue_input.dialogue)
        return {"summary": summary}
    except Exception as e:
        return {"summary": f"Error during summarization: {str(e)}"}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")