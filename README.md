# Industrial Vision AI

Industrial anomaly detection using deep learning and computer vision.

## Project Status

Initial project structure created. Model implementation and evaluation are
planned as subsequent development steps.

## Objectives

- Detect anomalous patterns in industrial images.
- Explore pretrained visual feature extractors such as DINOv2.
- Evaluate anomaly detection approaches such as PatchCore.
- Provide a reproducible inference pipeline.
- Expose predictions through a FastAPI service.
- Support testing and containerized deployment.

## Dataset

The project is designed to explore the MVTec Anomaly Detection (MVTec AD)
dataset.

Official dataset page: https://www.mvtec.com/research-teaching/datasets

Dataset files are not included in this repository. Review the dataset's
terms and conditions before downloading or redistributing any data.

## Development Environment

- Python 3.11
- PyTorch
- torchvision
- FastAPI
- pytest
- Ruff

Model development and GPU-intensive experiments are intended to run in
Google Colab. Lightweight development and testing can run locally.

## Project Structure

- `configs/`: Experiment configuration.
- `data/`: Dataset instructions and local data.
- `docs/`: Architecture and model documentation.
- `notebooks/`: Exploration and experiment notebooks.
- `scripts/`: Training, evaluation, and prediction entry points.
- `src/industrial_vision/`: Reusable project source code.
- `tests/`: Automated tests.
- `artifacts/`: Local model artifacts and generated outputs.

## Project Status and Results

No model performance claims are made at this stage. Metrics will be added
after experiments have been executed and independently checked.

## License

A license will be selected after reviewing the licenses and terms of the
code dependencies, pretrained models, and datasets.
