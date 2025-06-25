from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load BioMedLM (from Hugging Face)
model_name = "stanford-crfm/BioMedLM"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def identify_target(disease: str):
    prompt = f"What is the most relevant biological target (gene, protein, or pathway) associated with {disease}?"

    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=100, do_sample=True, temperature=0.7)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Optional: Extract only the answer part from the response
    answer = response.split("?")[-1].strip()
    
    return {
        "disease": disease,
        "suggested_target": answer
    }
