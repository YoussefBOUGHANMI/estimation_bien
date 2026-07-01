import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import GradientBoostingRegressor
import joblib


def ft_pred(type_bien, surface_m2, 
            nb_pieces, nb_chambres, etage,
           dpe , code_postal):

    

    le_etage = joblib.load("utils/le_etage.joblib")
    etage = le_etage.transform([etage])[0]

    le_type_bien = joblib.load("utils/le_type_bien.joblib")
    type_bien = le_type_bien.transform([type_bien])[0]

    mapping_dpe = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7}
    dpe = mapping_dpe[dpe]

    model = joblib.load("utils/model.joblib")

    estimation = model.predict([[type_bien, surface_m2, 
            nb_pieces, nb_chambres, etage,
           dpe , code_postal]])

    return(estimation[0])