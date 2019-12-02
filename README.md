# Amazon Review Generator
Feng Zheng (feng1013), Jiawei Wang (jwang96)
## Important Dates
- Poster Date: December 2, 2019
- Delivery Date: December 4, 2019
## Project Pipeline
- [x] make project repository
- [x] assign job
- [x] obtain dataset
  - [x] download *Amazon review dataset* from [here](https://nijianmo.github.io/amazon/index.html)
    - [x] Book Dataset (1M extracted)
    - [x] Electronic Dataset (1M extracted)
  - [x] figure out how we can make use of these data
- [x] project implementation
  - [x] discuss which technique we should use to the project, and who should implement them
  - model implementation list
    - [x] RNN -> Jiawei Wang
    - [x] GPT-2 -> Feng Zhang
- [x] project evaluation
  - [x] discuss how to evaluate the work
    - [Here](https://www.cs.brandeis.edu/~cs136a/CS136a_Slides/stent-columbia-EvaluationGeneration.pdf) provides several ways in evaluating text generators
  - [x] Human judgements
  - [x] Grammar Checker [Grammarly](https://app.grammarly.com/)
- [x] project presentation
  - [x] make poster
  - [x] prepare for the presentation
- [ ] deliver the work

## Usage
### Requirements
> gpt-2-simple
> textgenrnn

Since our work requires installing additional packages via `pip`, you will need to create a virtual environment and install the required packages if you intended to run it on Cheaha.

### Corpus generation
```bash
> python corpus_generator.py
```
### RNN
#### Fine-tuning RNN model
```bash
> python rnn-train.py
```
`rnn_train.job`, `rnn_train.sh` is used to train the model using Cheha's computing resources. you can run the following command line to initiate the training process (You will need to first `ssh` to Cheaha):
> sbatch rnn_train.job
#### Demonstration on RNN model
see `RNN_Demo.ipynb`.

### GPT-2
#### Fine-tuning GPT-2 model
```bash
usage: GPT2_train.py [-h] [--name NAME] [--corpus CORPUS] [--model MODEL]

GPT-2 training utility.

optional arguments:
  -h, --help            show this help message and exit
  --name NAME, -n NAME  Name for the trained model
  --corpus CORPUS, -c CORPUS
                        Corpus to fine-tune the model
  --model MODEL, -m MODEL
                        Pretrained Model name for fine-tuning
```
`gpt2_train.job`, `gpt2_train.sh` is used to train the model using Cheha's computing resources. you can run the following command line to initiate the training process (You will need to first `ssh` to Cheaha):
> sbatch gpt2_train.job

#### Demonstration of GPT-2 model
see `GPT-2_Demo.ipynb`.
#### Possible Exceptions in `GPT-2_Demo.ipynb` (and how to solve it)
In this notebook we demonstrated models fine-tuned two different datasets at a time. Since gpt2 only allows loading one model at each session, **restart your kernel is required** if you have already loaded one model and wants to load another one.

## Reference
- Ni, J. 2019. Amazon review data. Nijianmo.github.io. https://nijianmo.github.io/amazon/index.html.
- Alammar, J. 2019. The Illustrated GPT-2 (Visualizing Transformer Language Models). Jalammar.github.io. http://jalammar.github.io/illustrated-gpt2/.
- Woolf, M. 2019. minimaxir/textgenrnn. GitHub. https://github.com/minimaxir/textgenrnn.
- Woolf, M. 2019. minimaxir/gpt-2-simple. GitHub. https://github.com/minimaxir/gpt-2-simple.
- Write your best with Grammarly. 2019. Grammarly.com. https://grammarly.com/.
