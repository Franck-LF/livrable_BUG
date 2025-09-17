
import os
import io
import base64
import logging

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

import numpy as np
import keras

from PIL import Image


# ---------------- Config ----------------
UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXT = {"png", "jpg", "jpeg", "webp"}
CLASSES = ['desert', 'forest', 'meadow', 'mountain']

app = Flask(__name__)


# ---------------- Logger ----------------
# Create and configure logger
# logging.basicConfig(filename="logs/newfile.log",
#                     format='%(asctime)s %(message)s',
#                     filemode='w'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logs_dir = os.path.join(BASE_DIR, "logs")

logging.basicConfig(level = logging.INFO,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.FileHandler("logs\\newfile.log"),
                    # handlers=[logging.FileHandler(os.path.join(logs_dir, app.log")),
                              logging.StreamHandler()]
                    )

# Creating an object
logger = logging.getLogger(__name__)

# Setting the threshold of logger to DEBUG
# logger.setLevel(logging.DEBUG)

# Log examples
# logger.debug("Harmless debug Message")
# logger.info("Just an information")
# logger.warning("Its a Warning")
# logger.error("Did you try to divide by zero")
# logger.critical("Internet is down")



# ---------------- Model ----------------
MODEL_PATH = "models/final_cnn.keras"

try:
    model = keras.saving.load_model(MODEL_PATH, compile=False)
    logger.info(f"Modele Keras charge depuis '{MODEL_PATH}'.")
except:
    logger.critical(f"Impossible de charger le modèle Keras depuis '{MODEL_PATH}'.")



# ---------------- Utils ----------------
def allowed_file(filename: str) -> bool:
    """Vérifie si le nom de fichier possède une extension autorisée.
    La vérification est **insensible à la casse** et ne regarde que la sous-chaîne
    après le dernier point. Dépend de la constante globale `ALLOWED_EXT`.

    Args:
        filename: Nom du fichier soumis (ex. "photo.PNG").

    Returns:
        True si l’extension (ex. "png", "jpg") est dans `ALLOWED_EXT`, sinon False.

    Examples:
        >>> ALLOWED_EXT = {"png", "jpg", "jpeg", "webp"}
        >>> allowed_file("img.JPG")
        True
        >>> allowed_file("archive.tar.gz")
        False
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXT


def to_data_url(pil_img: Image.Image, fmt="JPEG") -> str:
    """Convertit une image PIL en Data URL base64 affichable dans un <img src="...">.
    L’image est encodée en mémoire (sans I/O disque), sérialisée en base64, puis
    encapsulée comme `data:<mime>;base64,<payload>`. Le type MIME est déduit de `fmt`.

    Args:
        pil_img: Image PIL à encoder.
        fmt: Format d’encodage PIL (ex. "JPEG", "PNG"). Par défaut "JPEG".

    Returns:
        Chaîne Data URL prête à être insérée dans une balise <img>.

    Raises:
        ValueError: si la sauvegarde PIL échoue pour le format demandé.

    Examples:
        >>> url = to_data_url(Image.new("RGB", (10, 10), "red"), fmt="PNG")
        >>> url.startswith("data:image/png;base64,")
        True
    """
    buffer = io.BytesIO()
    pil_img.save(buffer, format=fmt)
    b64 = base64.b64encode(buffer.getvalue()).decode("ascii")
    mime = "image/jpeg" if fmt.upper() == "JPEG" else f"image/{fmt.lower()}"
    return f"data:{mime};base64,{b64}"

def preprocess_from_pil(pil_img: Image.Image, target_size:tuple) -> np.ndarray:
    """Prépare une image PIL pour une prédiction Keras (normalisation + batch).
    Convertit en RGB, normalise en [0, 1] (float32) et ajoute l’axe batch.

    Args:
        pil_img: Image PIL source.

    Returns:
        np.ndarray de forme (1, H, W, 3), dtype float32, valeurs ∈ [0, 1].
    """
    img = pil_img.convert("RGB")
    # Redimensionnement pour correspondre à la taille d'entrée du modèle
    logger.info(f"taille initiale de l'image : {img.size}")
    img = img.resize(target_size)
    img_array = np.asarray(img, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis = 0)
    return img_array

# ---------------- Routes ----------------
@app.route("/", methods=["GET"])
def index():
    """Affiche la page d’upload.

    Returns:
        Réponse HTML rendant le template "upload.html".
    """
    return render_template("upload.html")

@app.route("/predict", methods=["POST"])
def predict():
    """Traite l'upload, exécute la prédiction et affiche le résultat.

    Attendu: une requête `multipart/form-data` avec le champ `file`.
    Étapes:
      1) Validation de présence et d'extension du fichier.
      2) Lecture du contenu en mémoire et ouverture en PIL.
      3) Prétraitement -> tenseur (1, H, W, 3).
      4) Prédiction Keras -> probas, top-1 (label, confiance).
      5) Encodage de l'image en Data URL et rendu du template résultat.

    Redirects:
        - Redirige vers "/" si le fichier est manquant ou invalide.

    Returns:
        Réponse HTML rendant "result.html" avec:
        - `image_data_url` : image soumise encodée (base64),
        - `predicted_label` : classe prédite (str),
        - `confidence` : score softmax (float),
        - `classes` : liste des classes (pour les boutons).
    """

    if "file" not in request.files:
        return redirect("/")

    file = request.files["file"]
    if file.filename == "" or not allowed_file(secure_filename(file.filename)):
        if file.filename == "":
            logger.warning("Aucun fichier sélectionné pour l'upload.")
        else:
            logger.warning(f"Extension de fichier non autorisée: '{file.filename}'")
        return redirect("/")

    logger.info(f"Fichier choisi : {file.filename}")
    print(type(file))
    raw = file.read()

    try:
        pil_img = Image.open(io.BytesIO(raw))
    except:
        logger.error(f"Erreur lors de l'ouverture de l'image : '{file.filename}'")
        return redirect("/")

    input_shape = model.get_config()["layers"][0]["config"]["batch_shape"]
    print("Input_shape", input_shape)

    img_array = preprocess_from_pil(pil_img, target_size = input_shape[1:3])

    if img_array.shape[1:] != input_shape[1:]:
        logger.error(f"Après traitement de l'image, la taille de l'image incorrecte: {img_array.shape[1:]} au lieu de {input_shape[1:]}")
        return redirect("/")

    assert img_array.shape[1:] == input_shape[1:], \
        f"ATTENTION !!! La taille de l'image ne correspond pas à la taille d'entrée du modèle\
        \n {img_array.shape[1:]} != {input_shape}"

    probs = model.predict(img_array, verbose=0)[0]
    cls_idx = int(np.argmax(probs))
    label = CLASSES[cls_idx]
    conf = float(probs[cls_idx])

    image_data_url = to_data_url(pil_img, fmt="JPEG")

    return render_template("result.html", image_data_url=image_data_url, predicted_label=label, confidence=conf, classes=CLASSES)

@app.route("/feedback", methods=["GET"])
def feedback_ok():
    """Affiche la page de confirmation de feedback (placeholder).

    Returns:
        Réponse HTML rendant le template "feedback_ok.html".
    """
    return render_template("feedback_ok.html")

if __name__ == "__main__":
    app.run(debug=True)
