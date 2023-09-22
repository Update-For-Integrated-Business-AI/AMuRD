# pip install -q transformers

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, GenerationConfig

checkpoint = "abdoelsayed/llama-7b-v1-Receipt-Key-Extraction"
device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(checkpoint, model_max_length=512,
        padding_side="right",
        use_fast=False,)
model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

def generate_response(instruction, input_text, max_new_tokens=100, temperature=0.1,  num_beams=4 ,top_k=40):
    prompt = f"Below is an instruction that describes a task, paired with an input that provides further context.\n\n### Instruction:\n{instruction}\n\n### Input:\n{input_text}\n\n### Response:"
    inputs = tokenizer(prompt, return_tensors="pt")
    input_ids = inputs["input_ids"].to(device)
    generation_config = GenerationConfig(
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            num_beams=num_beams,
        )
    with torch.no_grad():
        outputs = model.generate(input_ids,generation_config=generation_config, max_new_tokens=max_new_tokens)
    outputs = tokenizer.decode(outputs.sequences[0])
    return output.split("### Response:")[-1].strip().replace("</s>","")

instruction = "Extract the class, Brand, Weight, Number of units, Size of units, Price, T.Price, Pack, Unit from the following sentence"
input_text = "Americana Okra zero 400 gm"

response = generate_response(instruction, input_text)
print(response)
