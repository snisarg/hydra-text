# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from omegaconf import MISSING
from typing import Any
from typing import List


@dataclass
class ResidualMLPConf:
    _target_: str = "text.representation.transformers.ResidualMLP"
    input_dim: int = MISSING
    hidden_dims: List[int] = MISSING
    dropout: float = 0.1
    activation: Any = MISSING  # type


@dataclass
class TransformerLayerConf:
    _target_: str = "text.representation.transformers.TransformerLayer"
    embedding_dim: int = 768
    attention: Any = MISSING  # Optional[MultiheadSelfAttention]
    residual_mlp: Any = MISSING  # Optional[ResidualMLP]
    dropout: float = 0.1
