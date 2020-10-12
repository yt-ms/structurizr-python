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


"""Provide a superclass for all static structure model elements."""


from abc import ABC
from typing import TYPE_CHECKING, Optional, Union

from .element import Element, ElementIO


if TYPE_CHECKING:  # pragma: no cover
    from .relationship import Relationship


__all__ = ("StaticStructureElementIO", "StaticStructureElement")


class StaticStructureElementIO(ElementIO, ABC):
    """
    Define a superclass for all static structure model elements.

    This is the superclass for model elements that describe the static structure
    of a software system, namely Person, SoftwareSystem, Container and Component.

    """

    pass


class StaticStructureElement(Element, ABC):
    """
    Define a superclass for all static structure model elements.

    This is the superclass for model elements that describe the static structure
    of a software system, namely Person, SoftwareSystem, Container and Component.

    """

    def uses(
        self,
        destination: Element,
        description: str = "Uses",
        technology: str = "",
        **kwargs,
    ) -> Optional["Relationship"]:
        """Add a unidirectional "uses" style relationship to another element."""
        return self.get_model().add_relationship(
            source=self,
            destination=destination,
            description=description,
            technology=technology,
            **kwargs,
        )

    def delivers(
        self,
        destination: Element,
        description: str = "Delivers",
        technology: str = "",
        **kwargs,
    ) -> Optional["Relationship"]:
        """Add a unidirectional relationship to another element."""
        return self.uses(
            destination=destination,
            description=description,
            technology=technology,
            **kwargs,
        )

    def __rshift__(self, other: Union["StaticStructureElement", str]) -> Relationship:
        """Add a simple relationship using `>>` syntax.

        Examples:
            element1 >> element2                      # This forms a "Uses" relationship from element1 to element2
            element1 >> "Publishes to" >> element 2   # Form a relationship providing a specific description
        """
        if isinstance(other, StaticStructureElement):
            return self.uses(other)
        elif isinstance(other, str):
            return self.add_relationship(description=other)
        elif isinstance(other, Relationship):
            return self.add_relationship(other)
        else:
            raise TypeError(
                f"Adding relationship with >> not supported for type {type(other)}."
            )

    def __rrshift__(self, other: Relationship) -> "StaticStructureElement":
        """Complete a relationship of the form `elt1 >> "description" >> elt2`."""
        other.destination = self
        return self
