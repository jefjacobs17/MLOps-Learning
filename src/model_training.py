import logging

from sklearn.linear_model import LogisticRegression

logger = logging.getLogger(__name__)



def train_model(X_train, y_train):

    logger.info("Model training has started.")

    model = LogisticRegression(max_iter=1000)

    model.fit(X_train, y_train)

    logger.info("Model training completed.")

    return model