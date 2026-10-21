"""Visual feature extraction interfaces."""


class FeatureExtractor:
    """Interface for a pretrained visual feature extractor."""

    def extract(self, images):
        """Extract visual features from input images."""
        raise NotImplementedError("Feature extraction is not implemented yet.")
