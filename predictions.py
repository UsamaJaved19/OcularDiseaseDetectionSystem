from keras.preprocessing import image
from keras.models import load_model
import numpy as np


def prediction(uploaded_imag):
    img = image.load_img(uploaded_imag, target_size=(150, 150))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img/255.0
    model = load_model('bestmodel.keras',compile=False)
    predictations = model.predict(img)
    classes = ['age-related macular degeneration', 'cataract', 'diabetes', 'glaucoma',
           'hypertensive retinopathy', 'normal', 'other disease', 'pathological myopia']
    result = classes[np.argmax(predictations)]
    return result
