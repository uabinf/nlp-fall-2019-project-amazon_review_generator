from textgenrnn import textgenrnn
result_model = 'rnn-10k'
corpus_file = '/data/scratch/jwang96/books.10k'

textgen = textgenrnn(name=result_model)
textgen.train_from_file(
    file_path=corpus_file,
    num_epochs=10,
    gen_epochs=1,
    batch_size=1024,
    train_size=0.8,
    dropout=0.0,
    validation=True,
    rnn_layers=3,
    rnn_size=128,
    rnn_bidirectional=False,
    max_length=30,
    dim_embeddings=100)
