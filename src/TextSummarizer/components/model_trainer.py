from transformers import (TrainingArguments,
                          Trainer,
                          DataCollatorForSeq2Seq,
                          AutoModelForSeq2SeqLM,
                          AutoTokenizer)
from datasets import load_from_disk
import torch
import os

from TextSummarizer.entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        if (torch.cuda.is_available()):
            device = "cuda"
        else:
            device = "cpu"

        tokenizer = AutoTokenizer.from_pretrained(self.config.model_check_point)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_check_point).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model = model_pegasus)

        dataset_samsum = load_from_disk(self.config.data_path)

        trainer_arguments = TrainingArguments(
            output_dir = self.config.root_dir,
            num_train_epochs = self.config.num_train_epochs,
            warmup_steps = self.config.warmup_steps,
            per_device_train_batch_size = self.config.per_device_train_batch_size,
            per_device_eval_batch_size = self.config.per_device_train_batch_size,
            weight_decay = self.config.weight_decay,
            logging_steps = self.config.logging_steps,
            eval_strategy = self.config.eval_strategy,
            eval_steps = self.config.eval_steps,
            save_steps = 1e6,
            gradient_accumulation_steps = self.config.gradient_accumulation_steps
        )

        trainer = Trainer(model = model_pegasus, args = trainer_arguments,
                          tokenizer = tokenizer, data_collator = seq2seq_data_collator,
                          train_dataset = dataset_samsum["test"],
                          eval_dataset = dataset_samsum["validation"])
        trainer.train()

        # Save Model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))

        # Save Tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))