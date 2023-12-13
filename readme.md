# Automated Cardiac Diagnosis Challenge (ACDC)

Semi-supervised learning for medical image segmentation in the Cardiac Magnetic Resonance domain. Performing different experiments on the UK Biobank and ACDC datasets to achieve better performance while maintaining fairness, and auditing the models for bias.

## Outline

- ACDC dataset
- FCT
- UniMatch

## ACDC Dataset

Automated Cardiac Diagnosis Challenge Dataset available [here](https://www.creatis.insa-lyon.fr/Challenge/acdc/index.html).

Visualizations, analysis were performed to get a better understanding of the dataset.

## UK Biobank Dataset

UK Biobank (UKBB) Dataset available [here](https://www.ukbiobank.ac.uk/).

## FCT

A supervised model was trained on the ACDC and UKBB datasets and analyzed for bias. This experiment is available [here](https://github.com/msskzx/fct).

## UniMatch

A semi-supervised model was trained on the ACDC and UKBB datasets and analyzed for bias. This experiment is available [here](https://github.com/msskzx/unimatch).