from transformers import BertTokenizer, BertForMaskedLM, BertConfig, AdamW, pipeline
import torch
from tqdm.auto import tqdm

tokenizer = BertTokenizer.from_pretrained("./bert-configs")


# print(tokenizer.all_special_ids)



def mlm(tensor):
    rand = torch.rand(tensor.shape)
    mask_arr = (rand < 0.15) * (tensor > 3) * (tensor!=5)
    for i in range(tensor.shape[0]):
        selection = torch.flatten(mask_arr[i].nonzero()).tolist()
        tensor[i, selection] = 4
        return tensor


path = "text_dataset.txt"
input_ids = []
mask = []
labels = []

with open(path, 'r', encoding='utf-8') as f:
    lines = f.read().split('\n')
sample = tokenizer(lines, max_length=44, padding='max_length', truncation=True, return_tensors='pt')
labels.append(sample.input_ids)
mask.append(sample.attention_mask)
input_ids.append(mlm(sample.input_ids.detach().clone()))

input_ids = torch.cat(input_ids)
mask = torch.cat(mask)
labels = torch.cat(labels)

encodings = {
    'input_ids': input_ids,
    'attention_mask': mask,
    'labels': labels
}


class Dataset(torch.utils.data.Dataset):
    def __init__(self, encodings):
        self.encodings = encodings

    def __len__(self):
        return self.encodings['input_ids'].shape[0]

    def __getitem__(self, item):
        return {
            # 'input_ids': self.encodings['input_ids'][item]
            key: tensor[item] for key, tensor in self.encodings.items()
        }


dataset = Dataset(encodings)

dataloader = torch.utils.data.DataLoader(dataset, batch_size=16, shuffle=True)

config = BertConfig(
    vocab_size=tokenizer.vocab_size,
    max_position_embeddings=46,
    hidden_size=768,
    num_attention_heads=12,
    num_hidden_layers=12,
    type_vocab_size=1
)
# model = BertForMaskedLM(config)

# to continue training
model = BertForMaskedLM.from_pretrained("./bert-configs")


device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

model.to(device)

optim = AdamW(model.parameters(), lr=1e-4)

epochs = 500

for epoch in range(epochs):
    loop = tqdm(dataloader, leave=True)
    for batch in loop:
        optim.zero_grad()
        input_ids = batch['input_ids'].to(device)
        mask = batch['attention_mask'].to(device)
        labels = batch['labels'].to(device)
        outputs = model(input_ids, attention_mask=mask, labels=labels)
        loss = outputs.loss
        loss.backward()
        optim.step()

        loop.set_description(f'Epoch: {epoch}')
        loop.set_postfix(loss=loss.item())
model.save_pretrained('./bert-configs')

torch.save(model.state_dict(), './model.pth')


