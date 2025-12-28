# ⚓ Titanic Image Analyzer

Una aplicación web profesional inspirada en el **Titanic (1912)** que permite analizar imágenes y estimar características de personas (edad, sexo y clase social) basadas en las clases del Titanic, además de predecir su supervivencia usando un modelo preentrenado.

---

## 🌊 Características principales

- 🎨 **Interfaz elegante con temática Titanic**: azul marino, dorado y estilo art déco.  
- 🖼️ Análisis de imágenes PNG a través de URL.  
- 👤 Estimación de:
  - Edad
  - Sexo (0 = mujer, 1 = hombre)  
  - Clase social (1 = alta, 3 = baja)  
- 🔮 Predicción de supervivencia usando `model.pkl`.  
- 💻 CSS **embebido** en los HTML, sin archivos externos necesarios.  

---

## 📂 Estructura del proyecto

.
├── app.py # Servidor Flask
├── templates/
│ ├── index.html # Página de inicio
│ └── index2.html # Página de resultados
├── model.pkl # Modelo de predicción
├── .env # Variables de entorno (COHERE_API_KEY)
└── README.md # Este archivo

---

## ⚙️ Requisitos

- Python 3.10+
- Librerías:
  ```bash
  pip install flask cohere python-dotenv

## 🚀 Uso
1. Ejecuta la aplicación:
    python app.py

2. Abre tu navegador y visita:
    http://localhost:5000

3. Ingresa la URL de una imagen PNG.

4. Visualiza:
- La imagen ingresada
- Estimación de edad, sexo y clase
- Predicción de supervivencia

5. Vuelve al inicio para analizar otra imagen.