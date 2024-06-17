from transformers import BartForConditionalGeneration, AutoTokenizer

class BartBase():
    def __init__(self, model) -> None:
        self.model = BartForConditionalGeneration.from_pretrained(model)
        self.tokenizer = AutoTokenizer.from_pretrained(model)
    
    def __call__(self, text):
        inputs = self.tokenizer(text, max_length=1024, return_tensors="pt", truncation=True)
        summary_ids = self.model.generate(inputs["input_ids"], num_beams=4, min_length=40, max_length=150, length_penalty=2.0)
        sumary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=False)
        return sumary
    
    