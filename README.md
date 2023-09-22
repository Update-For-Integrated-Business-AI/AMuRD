# <a href="https://arxiv.org/abs/2309.09800">AMuRD</a>: Annotated Multilingual Receipts Dataset for Cross-lingual Key Information Extraction and Classification 

by
Abdelrahman Abdallah,
Mahmoud Abdalla,
Mohamed Elkasaby,
Yasser Elbendary, 
Adam Jatowt




![](images/model.png)




## Abstract

> Key information extraction involves recognizing and extracting text from scanned receipts, 
enabling retrieval of essential content, and organizing it into structured documents. 
This paper presents a novel multilingual dataset for receipt extraction, addressing key challenges in information extraction and item classification. 
The dataset comprises $47,720$ samples, including annotations for item names, attributes like (price, brand, etc.), and classification into $44$ product categories. 
We introduce the InstructLLaMA approach, achieving an F1 score of $0.76$ and an accuracy of $0.68$ for key information extraction and item classification.


## Demo for our Instruct LLama


Explore our Instruct LLama system through our live demo:

[**Demo for our Instruct LLama**](http://18.188.209.98:5052/)


## Examples

| Example | Input                                | Class                 | Brand        | Weight    | Number of units | Size of units  | Price   | T.Price | Pack   | Unit  |
| ------- | ------------------------------------ | ---------------------- | -------------| --------- | ---------------- | --------------- | ------- | ------- | ------ | ----- |
| Example 1| `40.99 20.99 2 chunks sunshine`    | Tins, Jars & Packets   | sunshine     | No Weight | 2                | No Size of units| 20.99   | 40.99   | علبة   | No Unit |
| Example 2| `برسيل اتوماتيك جل روز 2.6`      | Cleaning Supplies      | برسيل       | 2.6ل      | 1                | No Size of units| No Price| No T.Price | عبوة | ل     |
| Example 3| `regina Pasta penne 400g`           | Rice, Pasta & Pulses   | regina       | 400g      | 1                | No Size of units| No Price| No T.Price | كيس   | g     |
| Example 4| `10.00 400g Penne Pasta ElMaleka`   | Rice, Pasta & Pulses   | ElMaleka     | 400g      | 1                | No Size of units| 10      | 10      | كيس   | g     |


## Getting the code

To get started with the code and utilize the AMuRD dataset for your research or projects, you can clone this repository:

```bash
git clone https://github.com/yourusername/AMuRD.git
pip install transformers
python test.py
```
To perform key information extraction on item receipts using our models, you can utilize the following pre-trained models:
```
abdoelsayed/llama-7b-v2-Receipt-Key-Extraction

abdoelsayed/llama-7b-v1-Receipt-Key-Extraction
```

## Citation 
Please consider to cite our paper:
```
@misc{abdallah2023amurd,
    title={AMuRD: Annotated Multilingual Receipts Dataset for Cross-lingual Key Information Extraction and Classification},
    author={Abdelrahman Abdallah and Mahmoud Abdalla and Mohamed Elkasaby and Yasser Elbendary and Adam Jatowt},
    year={2023},
    eprint={2309.09800},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

## License


Note: The AMuRD Dataset can only be used for non-commercial research purposes. 
For researchers who want to use the AMuRD database, please first fill
in this [Application Form](Application_Form/Application_Form_for_AMuRD.doc) 
and send it via email to us ([m.abdallah@discoapp.ai](mailto:m.abdallah@discoapp.ai), [Yelbendary@discoapp.ai](mailto:Yelbendary@discoapp.ai), [abdoelsayed2016@gmail.com](mailto:abdoelsayed2016@gmail.com)). 


