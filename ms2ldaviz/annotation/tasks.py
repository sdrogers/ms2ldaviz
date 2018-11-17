
import numpy as np
import pandas as pd
from keras.models import load_model

from basicviz.models import Document, FeatureInstance
from models import SubstituentTerm, SubstituentInstance
from ms2ldaviz.celery_tasks import app


@app.task
def predict_substituent_terms(experiment_id):

    documents = Document.objects.filter(experiment__id=experiment_id)
    doc_names = []

    for doc in documents:
        doc_names.append(doc.name)

    MAX_MASS = 1000
    BIN_SIZE = 1
    intensities = pd.DataFrame(0.0, index=doc_names, columns=range((MAX_MASS // BIN_SIZE)), dtype=float)

    for doc in documents:
        feature_instances = FeatureInstance.objects.filter(document__id=doc.id)
        for feature_instance in feature_instances:
            mass = feature_instance.feature.name.split("_")[1]
            intensity = feature_instance.intensity

            # Populate the dataframe using each document's name to place data in the correct row.
            intensities.at[doc.name, mass] = intensity

    # Convert populated dataframe into a numpy array for use by neural networks.
    np_matrix = intensities.values
    np_index = intensities.index
    x_train_spectra = np.log(np_matrix + 1)

    model = load_model('saved_substituents_classifier_model.h5')
    predicted = model.predict(x_train_spectra)

    predicted_substituents = np.zeros(predicted.shape)
    predicted_substituents[predicted > 0.8] = 1

    legend_all = pd.read_csv("filtered_top_substituents_legend.txt", names=["name"])
    legends = legend_all["name"].values.tolist()

    for index, value in predicted_substituents:
        if value:
            doc_name = np_index[index]
            term = legends[index]
            probability = predicted[index]
            document = Document.objects.get(name=doc_name, experiment_id=experiment_id)
            subterm = SubstituentTerm.objects.get_or_create(name=term)[0]
            subintance = SubstituentInstance.objects.get_or_create(subterm=subterm, document=document)
            subintance.probability = probability
            subintance.save()
