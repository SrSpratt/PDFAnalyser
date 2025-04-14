from collections import Counter
import re
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

class WordCounter():
    def __init__(self, text):
        self.Text = text 
    
    def GenerateFreq(self):
        self.Words = re.findall(r'\b\w+\b', self.Text.lower())
        stopWords = set(stopwords.words('english'))
        self.Words = [word for word in self.Words if word not in stopWords]
        self.WordCounts = Counter(self.Words)

    def GenerateText(self):
        self.GenerateFreq()
        with open("frequenciesTxt.txt", 'w', encoding='utf-8') as output:
            for word, count in self.WordCounts.most_common():
                print("Aqui")
                output.write(f"{word}: {count}\n")
        print("Aqui")