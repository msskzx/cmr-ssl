# Automated Cardiac Diagnosis Challenge (ACDC)

## Outline

- ACDC dataset
- FCT model
- Bias Audit for BMI

## ACDC Dataset

Automated Cardiac Diagnosis Challenge Dataset available [here](https://www.creatis.insa-lyon.fr/Challenge/acdc/index.html).

Visualizations, analysis were performed to get a better understanding of the dataset.

## FCT Model

he The Fully Convolutional Transformer (`FCT`) proposed by this [paper](https://arxiv.org/abs/2206.00566) is used in this project. The model is trained on the `ACDC` dataset using the `PyTorch` code variant available [here](https://github.com/kingo233/FCT-Pytorch). 

Trained the model for 120 epochs which took around 3 hours on a `NVIDIA Tesla T4` GPU. Then, the model was saved for further analysis and auditing.

## Bias Audit for BMI

The `FCT` model was evaluated on the test set for 4 BMI categories.