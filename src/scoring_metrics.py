import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error,r2_score

def scoring_metrics(model, X_train, y_train,X_test,y_test):
    train_rmse = np.sqrt(mean_squared_error(y_train, model.predict(X_train)))
    test_rmse = np.sqrt(mean_squared_error(y_test, model.predict(X_test)))
    train_r2 = r2_score(y_train, model.predict(X_train))
    test_r2 = r2_score(y_test, model.predict(X_test))
    
    metrics = {
        'train_rmse' : train_rmse,
        'test_rmse' : test_rmse,
        'train_r2' : train_r2,
        'test_r2' : test_r2
    }

    result_metrics = pd.DataFrame(metrics,index=[0])

    return result_metrics
