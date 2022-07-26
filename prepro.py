import spacy


nlp = spacy.load("ru_core_news_sm")

f = open("learn\\2956.txt")
text = f.read().strip()

doc = nlp(text)
token_list = [token for token in doc]

print(token_list)
print(len(token_list))

# получение списка стоп-слов
# stopw = nlp.Defaults.stop_words3
# print(stopw)

print()
filtered_tokens = [token for token in doc if not token.is_stop]
print(filtered_tokens)
print(len(filtered_tokens))


lemmas = [
    f"Token: {token}, lemma: {token.lemma_}"
    for token in filtered_tokens
]

print(lemmas)