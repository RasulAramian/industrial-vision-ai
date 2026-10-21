"""Anomaly detection interfaces."""


class AnomalyDetector:
    """Interface for fitting and querying an anomaly detection model."""

    def fit(self, features):
        """Build the reference memory from normal training features."""
        raise NotImplementedError("Anomaly detector fitting is not implemented yet.")

    def predict(self, features):
        """Return anomaly scores and optional anomaly maps."""
        raise NotImplementedError("Anomaly prediction is not implemented yet.")
