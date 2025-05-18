# End to End NLP Text Summarizer

A lightweight and effective NLP-based text summarization tool built using Python and Hugging Face Transformers. This project allows you to condense long texts into concise summaries using state-of-the-art transformer models.

---

## Features

- Summarize large text files and articles  
- Leverages pre-trained Hugging Face transformer models (e.g., BART, T5)  
- Simple command-line interface for ease of testing  
- Modular code structure for easy expansion and experimentation
  
---

## Tech Stack

- Python 3.10+

- Hugging Face Transformers

- Tokenizers

## Project Workflow
1. Update `config.yaml`
2. Update `params.yaml`
3. Update the "enity"
4. Update the configuration manager in `src.config.configuration.py`
5. Update `components` [data_ingestion, data_validation, data_transformation, model_training]
6. Create the pipeline in `src.pipeline`
7. Update `main.py`
8. Update `app.py`

---

## Future Improvements

1. Web interface using Streamlit or Flask

2. Integration with PDF and DOCX inputs

3. Model benchmarking across datasets

4. Batch processing for multiple files


