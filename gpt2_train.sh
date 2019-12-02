#!/bin/bash
export PYTHONUNBUFFERED=1

python ./GPT2_train.py -n gpt-books -c /data/scratch/jwang96/books.large
python ./GPT2_train.py -n gpt-elec -c /data/scratch/jwang96/elec.large