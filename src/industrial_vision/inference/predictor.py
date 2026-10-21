"""High-level prediction interface."""


class AnomalyPredictor:
    """Load a trained detector and predict anomalies in images."""

    def predict(self, image):
        """Return prediction results for a single image."""
        raise NotImplementedError("Inference is not implemented yet.")
