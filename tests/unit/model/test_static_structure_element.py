# Copyright (c) 2020, Moritz E. Beber.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Ensure the expected behaviour of the model element."""


import pytest

from structurizr.model.model import Model
from structurizr.model.static_structure_element import StaticStructureElement


class ConcreteElement(StaticStructureElement):
    """Implement a concrete `StaticStructureElement` class for testing purposes."""

    pass


_model: Model = None  # Global reference to model so it doesn't get garbage-collected

@pytest.fixture(scope="function")
def empty_model() -> Model:
    """Provide an empty Model on demand for test cases to use."""
    global _model
    _model = Model()  # Stash it to prevent it being garbage_collected
    return _model


def test_static_structure_element_uses(empty_model: Model):
    """Ensure `uses` creates a relationship."""
    element1 = ConcreteElement(name="Element1")
    element2 = ConcreteElement(name="Element2")
    element1.set_model(empty_model)
    element2.set_model(empty_model)
    
    element1.uses(element2)

    assert len(element1.relationships) == 1
    r = list(element1.relationships)[0]
    assert r.source is element1
    assert r.destination is element2
    assert r.description == "Uses"


def test_static_structure_element_delivers(empty_model: Model):
    """Ensure `uses` creates a relationship."""
    element1 = ConcreteElement(name="Element1")
    element2 = ConcreteElement(name="Element2")
    element1.set_model(empty_model)
    element2.set_model(empty_model)
    
    element1.delivers(element2)

    assert len(element1.relationships) == 1
    r = list(element1.relationships)[0]
    assert r.source is element1
    assert r.destination is element2
    assert r.description == "Delivers"

