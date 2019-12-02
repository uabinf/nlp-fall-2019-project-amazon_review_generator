# Training process of GPT-2.
import os
import argparse

# Usage: python GPT2_train.py -n gpt-books -c /data/scratch/jwang96/books.large
def main():
    parser = argparse.ArgumentParser(description='GPT-2 training utility.')
    parser.add_argument('--name', '-n', help='Name for the trained model')
    parser.add_argument('--corpus', '-c', help='Corpus to fine-tune the model')
    parser.add_argument('--model', '-m', help='Pretrained Model name for fine-tuning', default='124M')
    args = parser.parse_args()

    import gpt_2_simple as gpt2
    # Download the pretrained model if not exists in models
    if not os.path.exists(os.path.join('models',args.model)):
        gpt2.download_gpt2(model_name=args.model)

    sess = gpt2.start_tf_sess()
    gpt2.finetune(sess,
        dataset=args.corpus,
        model_name=args.model,
        steps=1000,
        restore_from='fresh',
        run_name=args.name,
        print_every=10,
        sample_every=100,
        save_every=50)


if __name__ == '__main__':
    main()
