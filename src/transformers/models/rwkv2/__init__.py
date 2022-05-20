# flake8: noqa
# There's no way to ignore "F401 '...' imported but unused" warnings in this
# module, but to preserve other warnings. So, don't check this module at all.

# Copyright 2020 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import TYPE_CHECKING

# rely on isort to merge the imports
from ...utils import  _LazyModule, OptionalDependencyNotAvailable, is_tokenizers_available
from ...utils import is_torch_available




_import_structure = {
    "configuration_rwkv2": ["RWKV2_PRETRAINED_CONFIG_ARCHIVE_MAP", "RWKV2Config"],
    "tokenization_rwkv2": ["RWKV2Tokenizer"],
}

try:
    if not is_tokenizers_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["tokenization_rwkv2_fast"] = ["RWKV2TokenizerFast"]

try:
    if not is_torch_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["modeling_rwkv2"] = [
        "RWKV2_PRETRAINED_MODEL_ARCHIVE_LIST",
#        "RWKV2ForMaskedLM",
        "RWKV2ForCausalLM",
#        "RWKV2ForMultipleChoice",
#        "RWKV2ForQuestionAnswering",
#        "RWKV2ForSequenceClassification",
#        "RWKV2ForTokenClassification",
#        "RWKV2Layer",
        "RWKV2Model",
        "RWKV2PreTrainedModel",
#        "load_tf_weights_in_rwkv2",
    ]




if TYPE_CHECKING:
    from .configuration_rwkv2 import RWKV2_PRETRAINED_CONFIG_ARCHIVE_MAP, RWKV2Config
    from .tokenization_rwkv2 import RWKV2Tokenizer

    try:
        if not is_tokenizers_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .tokenization_rwkv2_fast import RWKV2TokenizerFast

    try:
        if not is_torch_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .modeling_rwkv2 import (
            RWKV2_PRETRAINED_MODEL_ARCHIVE_LIST,
            RWKV2ForMaskedLM,
            RWKV2ForCausalLM,
            RWKV2ForMultipleChoice,
            RWKV2ForQuestionAnswering,
            RWKV2ForSequenceClassification,
            RWKV2ForTokenClassification,
            RWKV2Layer,
            RWKV2Model,
            RWKV2PreTrainedModel,
            load_tf_weights_in_rwkv2,
        )



else:
    import sys

    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure, module_spec=__spec__)
