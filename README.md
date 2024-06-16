# Sumarization
Use the Pubmed dataset to refine the BartBase model and aid in its learning of text summarization.
## Desciption
The goal of this project is to use the Pubmed dataset to fine-tune the bart-base model to help it learn to summarize text. The primary goal project is to generate concise and accurate summaries from PubMed dataset, facilitating simpler understanding and knowledge extraction for researchers and professionals.
## Getting started
### Dependencies  
- Data: [Pubmed](https://huggingface.co/datasets/ccdv/pubmed-summarization)
- Libraries: Libraries: Flask 2.2.5, Transformers 4.41.2, Pytorch 2.3.0+cu121, Datasets 2.19.2, Tokenizers 0.19.1
- Model: [Bart-base](https://huggingface.co/facebook/bart-base)
### Install
```
git clone https://github.com/Quanhcmus/sumarization.git
```
### Executing program
- Explanation of each file
  1. Fine_tune.ipynb: Fine-tune the model with the selected data set
  2. Load_model.py: This file loads the model and performs text summarization with the BartBase class
  3. main.ipynb: This file is used to test the newly refined model with arbitrary text.
  4. app.py: This file is used to deploy the model to the web for users to enter text and return summarized results.
- Step-by-step bullets
  1. Open google colab and upload fine_tune.ipynb select TPU(T4) and press ctrl + F9 (Remember to change the hub link back to save the model after fine-tuning).
  2. Test or run app
     - To perform the test, simply change the path to the model you saved in the hub in the main.ipynb file
     - To deploy to the web, simply change the path to the model and run ```python app.py runserver```
## Authors
- Name: Nguyen Minh Quan
- Gmail: [minhquannguyen20022002@gmail.com](minhquannguyen20022002@gmail.com)
## Refrences
- Data: [https://huggingface.co/datasets/ccdv/pubmed-summarization](https://huggingface.co/datasets/ccdv/pubmed-summarization)
- Model: [https://huggingface.co/facebook/bart-base](https://huggingface.co/facebook/bart-base)
- ChatGPT
