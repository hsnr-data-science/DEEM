# End-To-End ML with LLMs and Semantic Data Management: Experiences from Chemistry 4.0

<p align="center">
  <img src="image/GraphicalAbstract.jpg" alt="Graphical Abstract" width="600"/>
</p>

This repository accompanies the paper:

**"End-To-End ML with LLMs and Semantic Data Management: Experiences from Chemistry 4.0"**  
Sayed Hoseini, Vincent Herrmann, Christoph Quix  
Hochschule Niederrhein University of Applied Sciences, Fraunhofer FIT  
📅 DEEM ’25 — Workshop on Data Management for End-to-End Machine Learning

## 📄 Abstract

Machine Learning (ML) in industrial chemistry is often hindered by the complexity of preprocessing heterogeneous datasets. This proof-of-concept study explores how semantic data management can support **LLM-driven automation** of end-to-end ML pipelines in a real-world Chemistry 4.0 setting.

We use a **semantic model** to provide structured metadata and guide LLMs (e.g., GPT-4, Gemini, LLaMA) via natural language prompts for code generation in data wrangling and Gaussian Process modeling. The results show that, with structured context, larger LLMs can generate functional pipelines with minimal human intervention.

## 🧪 Project Structure

```bash
DEEM/
├── abrasion.csv                   # Raw abrasion test data
├── compare_dataframes.py         # Utility for comparing processed DataFrames
├── data_points.txt               # Example timeline of robotic experiment steps
├── evaluation/                   # LLM output evaluations (ChatGPT, DeepSeek, etc.)
├── measurements/                 # Raw measurement data per product
├── prompts.ipynb                 # Jupyter notebook with prompt examples
├── target.csv                    # Final processed ML-ready dataset
├── Testing_for_Evaluation.ipynb  # Notebook for evaluating LLM outputs
├── SM.txt                        # RDF-style semantic model (data source definition)
├── viskos_means.csv              # Viscosity measurements
└── README.md                     # You're here
