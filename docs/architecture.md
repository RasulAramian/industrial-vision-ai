# Architecture

## Planned Pipeline

1. Load and validate industrial images.
2. Apply deterministic image preprocessing.
3. Extract visual features using a pretrained backbone.
4. Fit or construct the anomaly detection memory bank using normal training images.
5. Generate image-level anomaly scores and pixel-level anomaly maps where supported.
6. Evaluate performance on the official dataset splits.
7. Serve predictions through a FastAPI application.

## Candidate Components

- Feature extraction: DINOv2.
- Anomaly detection: PatchCore.
- API: FastAPI.
- Testing: pytest.

These components are planned candidates. Compatibility, implementation details,
and computational requirements must be verified during development.
