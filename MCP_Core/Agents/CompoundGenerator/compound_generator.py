from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from transformers import AutoTokenizer
model_name = "jonghyunlee/MolGPT_pretrained-by-ZINC15"
tokenizer = AutoTokenizer.from_pretrained("jonghyunlee/MolGPT_pretrained-by-ZINC15")

model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_compounds(target: str, num_return_sequences: int = 3):
    prompt = f"{target}:"
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(
            input_ids=inputs["input_ids"],
            max_length=64,
            num_return_sequences=num_return_sequences,
            do_sample=True,
            temperature=0.9,
            top_k=50,
            top_p=0.95
            )
        smiles_list = [tokenizer.decode(g, skip_special_tokens=True).strip() for g in output]
        return {
            "target": target,
            "generated_compounds": smiles_list
            }
