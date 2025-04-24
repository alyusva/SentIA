from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np
import torch.nn.functional as F

# Cargar modelo y tokenizer desde la carpeta "models"
MODEL_PATH = "models"
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

# Labels del modelo
label_names = ["😢 sadness / tristeza", "😄 joy / alegría", "❤️ love / amor", "😡 anger / ira", "😨 fear / miedo", "😲 surprise / sorpresa"]

def predict_emotion(text):
    # Tokenizar texto
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    # Desactivar gradientes y obtener predicción
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = F.softmax(logits, dim=1).numpy().flatten()  # Obtener probabilidades

    # Imprimir distribución en terminal
    print(f"\n📊 Distribución de emociones para: {text}")
    for i, prob in enumerate(probs):
        print(f"{label_names[i]}: {prob*100:.2f}%")

    # Obtener la clase con mayor probabilidad
    predicted_class_id = np.argmax(probs)
    return label_names[predicted_class_id]
