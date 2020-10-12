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

from structurizr.model.model import Model, Relationship
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

    r = element1.uses(element2)

    assert list(element1.relationships) == [r]
    assert r.source is element1
    assert r.destination is element2
    assert r.description == "Uses"


def test_static_structure_element_delivers(empty_model: Model):
    """Ensure `uses` creates a relationship."""
    element1 = ConcreteElement(name="Element1")
    element2 = ConcreteElement(name="Element2")
    element1.set_model(empty_model)
    element2.set_model(empty_model)

    r = element1.delivers(element2)

    assert list(element1.relationships) == [r]
    assert r.source is element1
    assert r.destination is element2
    assert r.description == "Delivers"


def test_static_structure_element_add_relationship_shorthand(empty_model: Model):
    """Check the various forms of adding relationships with `>>`."""
    element1 = ConcreteElement(name="Element1")
    element2 = ConcreteElement(name="Element2")
    element3 = ConcreteElement(name="Element3")
    element4 = ConcreteElement(name="Element3")
    element1.set_model(empty_model)
    element2.set_model(empty_model)
    element3.set_model(empty_model)
    element4.set_model(empty_model)

    r = element1 >> element2
    assert list(element1.relationships) == [r]
    assert r.destination is element2
    assert r.description == "Uses"

    e = element2 >> "Publishes to" >> element3
    assert e is element3  # This allows chaining of further >>
    assert len(element2.relationships) == 1
    r = list(element2.relationships)[0]
    assert r.destination is element3
    assert r.description == "Publishes to"

    # Also check that you can add an existing relationship instance - whilst this is
    # not the preferred style, it enables subtyping of Relationship for more advanced
    # use-cases.
    r = Relationship(description="Depends on")
    element3 >> r >> element4
    assert list(element3.relationships) == [r]

    # Make sure you can't accidentally add wrong stuff
    with pytest.raises(TypeError):
        element1 >> 17
