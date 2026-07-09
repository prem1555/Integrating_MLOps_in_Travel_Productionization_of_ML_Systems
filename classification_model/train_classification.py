import joblib
import os
import mlflow
import mlflow.sklearn

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

from preprocess import preprocess_data


# Load data
X_train, X_test, y_train, y_test = preprocess_data()

mlflow.set_tracking_uri(
    'file:../mlruns'
)


# SET EXPERIMENT
mlflow.set_experiment(
    'Gender_Classification'
)


# START RUN
with mlflow.start_run():

    print('MLflow Started')


    # Parameters
    n_estimators = 100
    random_state = 42

    # Model
    model = RandomForestClassifier(

        n_estimators=n_estimators,
        random_state=random_state

    )

    # Train
    model.fit(X_train, y_train)

    # Predictions
    predictions = model.predict(X_test)

    # Metrics
    accuracy = accuracy_score(
        y_test,
        predictions
    )

    precision = precision_score(
        y_test,
        predictions,
        average='weighted'
    )

    recall = recall_score(
        y_test,
        predictions,
        average='weighted'
    )

    f1 = f1_score(
        y_test,
        predictions,
        average='weighted'
    )

    # Print metrics
    print('Accuracy:', accuracy)

    print('Precision:', precision)

    print('Recall:', recall)

    print('F1 Score:', f1)

    # Log parameters
    mlflow.log_param(
        'n_estimators',
        n_estimators
    )

    mlflow.log_param(
        'random_state',
        random_state
    )

    # Log metrics
    mlflow.log_metric(
        'Accuracy',
        accuracy
    )

    mlflow.log_metric(
        'Precision',
        precision
    )

    mlflow.log_metric(
        'Recall',
        recall
    )

    mlflow.log_metric(
        'F1_Score',
        f1
    )

    # Log model
    mlflow.sklearn.log_model(

        model,

        'gender_classification_model'

    )

    # Save model
    joblib.dump(

        model,

        'models/gender_model.pkl'

    )

    print('Classification Model Logged')