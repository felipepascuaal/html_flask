from flask import Flask, render_template, request
import cohere
import json
import pickle
import os

#leemos el .env
from dotenv import load_dotenv
load_dotenv() #se pone la ruta del .env


#Leer variable de entorno
api_key = os.getenv("COHERE_API_KEY")

co = cohere.ClientV2(api_key)

app = Flask(__name__)

def get_features_img(image_url): 
    prompt = """A partir de la imagen, usa tu criterio para ver cuantos años, que sexo, el sexo es de tipo entero siendo 1 hombre y 0 mujer. y de que clase es la persona de la imagen. 
        Si hay más de una persona, elige una y si no hay personas, inventate una persona. La clase esta basada en las clases que había en el titanic
        siendo 1 la más alta y 3 la más baja.
        El resultado me lo tienes que dar en un json tal que así:
        {edad: 18 (entero)
        sexo: 0 (entero)
        clase: 1 (entero)}"""   
    
    response = co.chat(
        model="command-a-vision-07-2025",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            # Can be either a base64 data URI or a web URL.
                            "url": image_url,
                            "detail": "auto"
                        }
                    }
                ]
            }
        ]
    )
    
    return json.loads(response.message.content[0].text)
 



@app.route("/", methods = ['GET']) #"/" --> endpoint
def home():
    return render_template("index.html")

@app.route("/inicio", methods = ["POST", "GET"])
def inicio():
    #form es un diccionario
    if request.method == "POST":
        img_url = request.form.get("img_url")
        print(img_url)
        features_dict = get_features_img(img_url)

    if features_dict:
        age = features_dict["edad"]
        sex = features_dict["sexo"]
        clase = features_dict["clase"]
        age = int(age)
        sex = int(sex)
        clase = int(clase)
        with open("model.pkl", "rb") as f:
            read_rf = pickle.load(f)
        survived = "sobrevive" if read_rf.predict([[age,sex,clase]])[0] else "muere"
        res = f"La persona de la imagen {survived}"
        return render_template("index2.html", respuesta2 = res, img_url = img_url)
    else:
        return "No hay respuesta"

if __name__ == "__main__":
    app.run(debug = True, host = "localhost", port  = 5000)