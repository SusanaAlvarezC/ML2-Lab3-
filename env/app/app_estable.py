from flask import Flask, render_template, request
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
from nltk.tokenize import sent_tokenize
import os
import nltk
import numpy as np

app = Flask(__name__)

class QAModel:
    def __init__(self, model_name, tale, questions):
        nltk.download('punkt')  # Download the 'punkt' resource

        self.model_name = model_name
        self.tale = tale
        self.questions = questions
        self.sentences = self.preprocess_sentences(tale)
        
        if "sentence-transformers" in model_name.lower():
            # Use SentenceTransformer for MiniLM or other embeddings
            self.model = SentenceTransformer(model_name)
            self.sentence_embeddings = self.model.encode(self.sentences)
            self.qa_pipeline = None  # No QA pipeline for SentenceTransformer
        elif "roberta" in model_name.lower():
            # Use Hugging Face transformers for RoBERTa-based QA
            self.model = AutoModelForQuestionAnswering.from_pretrained(model_name)
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.qa_pipeline = pipeline('question-answering', model=self.model, tokenizer=self.tokenizer)
            self.sentence_embeddings = None  # No sentence embeddings for Hugging Face transformers

    def preprocess_sentences(self, tale):
        sentences = sent_tokenize(tale)
        i = 0
        while i < len(sentences):
            if len(sentences[i]) < 3:
                sentences.pop(i)
            i += 1
        return sentences

    def find_most_relevant_sentences(self, question, top_k=5):
        if self.sentence_embeddings is not None:
            question_embedding = self.model.encode([question])
            similarities = cosine_similarity(question_embedding, self.sentence_embeddings)
            most_similar_indices = similarities[0].argsort()[-top_k:][::-1]
            return [self.sentences[i] for i in most_similar_indices]
        else:
            return None  # Handle the case when using Hugging Face transformers

    def get_answer(self, question):
        if self.qa_pipeline is not None:
            # Use QA pipeline for RoBERTa-based QA
            QA_input = {'question': question, 'context': self.tale}
            answer = self.qa_pipeline(QA_input)
            return answer['answer']
        else:
            return "This model does not support question-answering."

# Method to read the tale from a file
def read_tale_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Configuration
#model_name = 'sentence-transformers/all-MiniLM-L6-v2'  # or 
model_name = 'deepset/roberta-base-squad2'
current_directory = os.path.dirname(os.path.abspath(__file__))
tale_path = os.path.join(current_directory, 'cuento.txt')

questions = [
    "What is the Shoemaker's name?",
    "Which was Fyodor's work?",
    "Who dragged Fyodor to hell?",
    "What does Fyodor want?",
    "What does the evil spirit want?"
]

# Create an instance of QAModel with the tale read from the file
qa_model = QAModel(model_name, read_tale_from_file(tale_path), questions)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = {
        'titulo': 'LAB3 - ML2',
        'bienvenida': 'Saludos',
        'answer': None,
        'tale_content': qa_model.tale
    }

    if request.method == 'POST':
        question = request.form.get('question')
        if "sentence-transformers" in model_name.lower():
            # Use SentenceTransformer for MiniLM or other embeddings
            top_k_sentences = qa_model.find_most_relevant_sentences(question, top_k=5)
            data['answer'] = top_k_sentences
        elif "roberta" in model_name.lower():
            # Use RoBERTa-based QA
            data['answer'] = qa_model.get_answer(question)

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
