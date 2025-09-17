
import os
import io
import sys
import base64

# from joblib import load
import pytest

import numpy as np
import keras

from PIL import Image


PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# sys.path.append(PATH)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from app import app as flask_app
# from app import to_data_url


image_folder = "image_to_test/"
MODEL_PATH = "../models/final_cnn.keras"



# -----------------------------------
# Load vectorizer and classifier
# -----------------------------------

# pipe = load('best_model_joblib.pkl')
# vectorizer = pipe.named_steps['tfidf']
# classifier = pipe.named_steps['clf']



# @pytest.fixture
# def client():
#     flask_app.config["TESTING"] = True
#     with flask_app.test_client() as client:
#         yield client





# ------------------------------------------
#
#           Mes tests
#
# ------------------------------------------

# S'assurer que l'on peut charger le modèle Kéras
def test_load_model():
    print("\n****** Test Load Model")
    try:
        _ = keras.saving.load_model(MODEL_PATH, compile=False)
        assert True
    except:
        assert False, f"Impossible de charger le modèle Kéras depuis '{MODEL_PATH}'."


# S'assurer que l'image peut être chargée
def test_load_image():
    print("\n****** Test Load Image")
    print('PATH:', PATH)
    print('Image folder:', image_folder)
    try:
        img_path = os.path.join(PATH + "\\images_to_test\\", "desert_96.jpg")
        _ = Image.open(img_path).convert("RGB")
        assert True
    except:
        assert False, f"Impossible de charger l'image depuis {img_path}."


# Assurez vous que les dimensions des tableaux numpy est compatible avec 
# la forme d'entrée du modèle Kéras
# def test_image_input_model():
    # print("Test Image Input Model")
#     img_path = os.path.join("C:/Users/Utilisateur/Documents/Livrable_BUG/images_to_test/", "desert_96.jpg")
#     pil_img = Image.open(img_path).convert("RGB")
#     model = keras.saving.load_model(MODEL_PATH, compile=False)
#     print("TF-IDF output:", X_transformed.shape)
#     print("Classifier input:", classifier.coef_.shape[1])
#     assert X_transformed.shape[1] == classifier.coef_.shape[1], f"ATTENTION !!!\n {X_transformed.shape[1]} != {classifier.coef_.shape[1]}"


# Assurez-vous que la probabilité de la prédiction de la classe prédite 
# est comprise entre 0 et 1 (en sortie de predict_proba() du classifieur)
# def test_probability():
#     probas = pipe.predict_proba(['super', 'nul', 'très mauvais'])
#     print("proba:", probas)
#     assert all([p >= 0 and p <= 1 for p in item] for item in probas), "Une probabilité n'est pas comprise entre 0 et 1"


# Assurez-vous que la requête GET sur la page d'accueil (route "/") renvoie bien le code HTTP 200.
# def test_request_connection(client):
#     response = client.get("/")
#     print("Code response:", response)
#     assert response.status_code == 200, \
#         f"La route '/' devrait renvoyer 200, mais a renvoyé {response.status_code}."


# Assurez-vous que le classifieur est bien une instance de le classe LogisticRegression (classe importée depuis sklearn.linear_model)
# def test_instance_LogisticRegression():
#     assert isinstance(classifier, LogisticRegression), f"Le classifieur est de type : {type(classifier)}"





if __name__ == "__main__":
    print("START MAIN")
    # test_load_model()
    test_load_image()
    # test_image_input_model()