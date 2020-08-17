from tslearn.clustering import TimeSeriesKMeans
import numpy as np


def knn():
    model = TimeSeriesKMeans.from_json('res/knn_model.txt')
    model
    pred = model.predict(test)
    a = np.zeros((320,), dtype=int)
    b = np.ones((80,), dtype=int)
    true = np.concatenate([a, b])
    # confusion_matrix(true, pred)
    return pred



#     a = list[np.ndarray[np.ndarray[np.int64]]]