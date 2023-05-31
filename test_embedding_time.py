from datetime import datetime
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('sentence-transformers/all-roberta-large-v1')

text = ''
with open("Y://scripts_devs//embed_try//magyar_1202_chr.txt", 'r', encoding="utf-8", errors="ignore") as file:
    text = file.read()

start_time = datetime.now()
embedding = model.encode(text)
end_time = datetime.now()
time_diff = end_time-start_time
print(embedding)
print (time_diff)