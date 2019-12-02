# Corpus Generator.
import json

def main():
    output_file = '/data/scratch/jwang96/books.large'
    def extract_corpus(data_file, n):
        corpus = ""
        with open(data_file, 'r') as f:
            for i in range(n):
                line = f.readline()
                try:
                    js = json.loads(line)
                    revtxt = js['reviewText']
                    score = js['overall']
                    revtxt = revtxt.replace('\n', ' ')
                    corpus += str(score)+': '+revtxt
                    corpus += ' <|endoftext|>\n\n'
                except:
                    continue
        return corpus
    with open(output_file, 'w') as f:
        f.write(extract_corpus(data_file, 1000000))

if __name__ == '__main__':
    main()
