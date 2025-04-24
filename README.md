# 🧠 SentIA — Clasificación de Sentimientos con NLP

Bienvenido a **SentIA**, un proyecto de procesamiento de lenguaje natural (PLN) centrado en la detección y clasificación de emociones a partir de texto.

Este repositorio forma parte de la práctica final del máster en IA & Big Data, y tiene como objetivo construir una aplicación funcional de análisis de sentimientos sobre reseñas reales.

---

## 🚀 Funcionalidades

- Clasificación de sentimientos utilizando modelos de deep learning entrenados.
- Interfaz sencilla construida con `streamlit` para probar el modelo en tiempo real.
- Visualización rápida del análisis.
- Preparado para su futura integración en una app de apoyo psicológico o monitoreo de opiniones de usuarios.

---

## 🛠️ Tecnologías utilizadas

- `Python`
- `Transformers` (HuggingFace)
- `PyTorch`
- `Scikit-learn`
- `Pandas`, `NumPy`
- `Streamlit`

---

## 📂 Estructura del repositorio

```bash
.
├── app.py                  # App principal con streamlit
├── predictor.py            # Código para cargar y ejecutar el modelo
├── requirements.txt        # Dependencias del proyecto
├── Practica_Final.ipynb    # Notebook explicativo del desarrollo
├── model/                  # Archivos auxiliares del modelo (tokenizer, config, etc. para los modelos de prueba del notebook)
├── models/                 # Archivos del modelo final usado en la app (La carpeta hay que cumplimentarla con los archivos del link que se indica mas adelante)
└── logo.png                # Logo del proyecto
```
🧼 Nota: los archivos pesados (>100MB) han sido eliminados del historial para cumplir con las políticas de GitHub.

## ▶️ ¿Cómo ejecutar el proyecto?

1. Instala las dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecuta la app:

```bash
streamlit run app.py
```

3. Abre tu navegador en `http://localhost:8501` para interactuar con SentIA.

## 📌 Notas adicionales

- El modelo fue entrenado localmente, pero se puede adaptar para utilizar HuggingFace Hub o algún almacenamiento en la nube.

- Este proyecto es una prueba de concepto, ideal para evolucionar hacia un sistema más avanzado de análisis de emociones o apoyo psicológico.

- Enlace al contenido de la carpeta model:
  [https://drive.google.com/drive/folders/12SEtWuEsUXx2p5z7Kfs3cT3SIc3_kbW-?usp=sharing](https://drive.google.com/drive/folders/1pEXMWlSeU9CXu4eeiiR_4BRVnskNYb98?usp=drive_link)
  
  

## ✨ Autores

Álvaro Yuste

Joaquín Moreno

Ángel Saenz

## 📄 Licencia
MIT License – Siéntete libre de usarlo, modificarlo o adaptarlo con cariño 😄
