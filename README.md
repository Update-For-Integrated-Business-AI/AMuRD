# <a href="https://arxiv.org/abs/2309.09800">AMuRD</a>: Annotated Multilingual Receipts Dataset for Cross-lingual Key Information Extraction and Classification 






## Abstract

> Key information extraction involves recognizing and extracting text from scanned receipts, 
enabling retrieval of essential content, and organizing it into structured documents. 
This paper presents a novel multilingual dataset for receipt extraction, addressing key challenges in information extraction and item classification. 
The dataset comprises $47,720$ samples, including annotations for item names, attributes like (price, brand, etc.), and classification into $44$ product categories. 
We introduce the InstructLLaMA approach, achieving an F1 score of $0.76$ and an accuracy of $0.68$ for key information extraction and item classification.


## Demo for our Instruct LLama


Explore our Instruct LLama system through our live demo:

[**Demo for our Instruct LLama**](http://18.188.209.98:5003/)


## Examples

| Example | Input                                | Class                 | Brand        | Weight    | Number of units | Size of units  | Price   | T.Price | Pack   | Unit  |
| ------- | ------------------------------------ | ---------------------- | -------------| --------- | ---------------- | --------------- | ------- | ------- | ------ | ----- |
| Example 1| `40.99 20.99 2 chunks sunshine`    | Tins, Jars & Packets   | sunshine     | No Weight | 2                | No Size of units| 20.99   | 40.99   | علبة   | No Unit |
| Example 2| `برسيل اتوماتيك جل روز 2.6`      | Cleaning Supplies      | برسيل       | 2.6ل      | 1                | No Size of units| No Price| No T.Price | عبوة | ل     |
| Example 3| `regina Pasta penne 400g`           | Rice, Pasta & Pulses   | regina       | 400g      | 1                | No Size of units| No Price| No T.Price | كيس   | g     |
| Example 4| `10.00 400g Penne Pasta ElMaleka`   | Rice, Pasta & Pulses   | ElMaleka     | 400g      | 1                | No Size of units| 10      | 10      | كيس   | g     |


## Getting the code


To get started with the code and utilize the AMuRD dataset for your research or projects, you can clone this repository:

### To use our original model on GPU
```bash
git clone https://github.com/yourusername/AMuRD.git
pip install transformers
python test.py
```
To perform key information extraction on item receipts using our models, you can utilize the following pre-trained models:

[abdoelsayed/llama-7b-v2-Receipt-Key-Extraction](https://huggingface.co/abdoelsayed/llama-7b-v2-Receipt-Key-Extraction)

[abdoelsayed/llama-7b-v1-Receipt-Key-Extraction](https://huggingface.co/abdoelsayed/llama-7b-v1-Receipt-Key-Extraction)

### To use our original model on the CPU
```
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
# convert the 7B model to ggml FP16 format
python convert.py path/to/our/model

# quantize the model to 4-bits (using q4_0 method)
./quantize ./path/to/our/model/ggml-model-f32.bin ./path/to/our/model/ggml-model-q4_0.bin q4_0
```

To use the ```ggml-model-q4_0.bin``` on your own desktop, laptop, or low-resource AWS instance, you can follow these general steps:
```

pip install llama-cpp-python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--model", type=str, default="./models/brand_arabic_models/test/ggml-model-q4_0.bin")
args = parser.parse_args()

llm = Llama(model_path=args.model)

output = llm(
    # SeaStar Smoked herrings fillet, 250 gm
    """Below is an instruction that describes a task, paired with an input that provides further context. 
Write a response that appropriately completes the request.\n\n
### Instruction:\n Extract the Brand Name from the following Sentence \n\n### Input:\n   SeaStar Smoked herrings fillet, 250 gm  \n\n### Response: """,
    max_tokens=128,
    stop=["Q:", "\n"],
    echo=True,
)

print(output)
```

## License


Note: The AMuRD Dataset can only be used for non-commercial research purposes. 

