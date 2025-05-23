from data_loader import df
import nltk
nltk.download('punkt_tab')
nltk.download('wordnet')
import re


def get_sentences_around_lemma(df, lemma, pattern, sentences_before, sentences_after):
    """
  Returns sentences surrounding lemma
  """
    found_sentences = []

    for i, row in df.iterrows():
        if lemma in str(row['lemmas']):
            word_entries = re.findall(pattern, row.text0)
            text = nltk.sent_tokenize(row.text0)

            for j, sentence in enumerate(text):
                for term in word_entries:
                    if re.search(term, sentence):
                        all_sent_data = [' '.join(text[j - sentences_before:j + sentences_after + 1]), row.author,
                                         row.year, 1]
                        if all_sent_data not in found_sentences:
                            found_sentences.append(all_sent_data)
        print(i)

    return found_sentences


sentences = get_sentences_around_lemma(df, 'фобия', re.compile(r'\b[Фф]оби[яиюей]'), sentences_before=1, sentences_after=1)

last_info = None
i = 0
for ind, sentence in enumerate(sentences):
    if sentence[1] != last_info:
        i += 1
        last_info = sentence[1]
        print(f'{i}. {sentence[0]} [{sentence[1]}, {sentence[2]}]', end='\n\n')
    else:
        sentence[3] = sentences[ind - 1][3] + 1
        last_info = sentence[1]
        print(f'{i}.{sentence[3]} {sentence[0]} [{sentence[1]}, {sentence[2]}].', end='\n\n')

print('Overall uses:', len(sentences))
print('IPM:', len(sentences)/137745737*1000000)


with open('output.txt', 'w', encoding='utf-8') as file:
    for item in sentences:
        file.write(item[0] + '\n')
      
