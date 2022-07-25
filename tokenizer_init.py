from transformers import BertTokenizer, BertForMaskedLM
import json

tokenizer = BertTokenizer.from_pretrained('allVoc.txt')


vocab=tokenizer.vocab
with open("student.json", "w") as write_file:
    json.dump(vocab, write_file, indent=4)



text1="line temporal quantitative / / / / 23 190 207 1 . 0 / / 0 . 8 / / / / / / / / / / / / / / / / / / / / / / / /"
t= tokenizer.tokenize(text1)
t1= tokenizer.encode(text1)

print(t)
print(t1)

print(tokenizer.mask_token_id)
print(tokenizer.all_special_ids)

tokenizer.save_pretrained('bert-configs')




