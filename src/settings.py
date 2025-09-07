from pathlib import Path
import numpy as np

np.random.seed(0)

# Paths
project_root_path = Path(__file__).parent.parent.resolve()
data_root_path = project_root_path / "data"

logs_root_path = project_root_path / "logs"
logs_root_path.mkdir(exist_ok=True)
models_root_path = project_root_path / "models"
models_root_path.mkdir(exist_ok=True)
