from transformers import pipeline

fill = pipeline('fill-mask', model='bert-configs', tokenizer='bert-configs')

text2 = f"line temporal {fill.tokenizer.mask_token} / / / / 23 190 207 1 . 0 / / 0 . 8 / / / / / / / / / / / / / / / / / / / / / / / /"
text =f"bar categorical quantitative / / / / / / / / / / / / / / / / / / / / / / / / / / 202 178 214 1 . 0 / / / / {fill.tokenizer.mask_token} 399 9e750d"

print(fill(text2))
print(fill(text))