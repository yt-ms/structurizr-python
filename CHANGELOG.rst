=======
History
=======

Next Release
------------


0.6.0 (2021-06-10)
------------------
* Feat: Add ``DynamicView`` (#77)
* Feat: Add ``FilteredView`` (#81)
* Breaking change: View.find_element_view and find_relationship_view parameter changes.

0.5.0 (2021-05-03)
------------------
* Feat: Add support for grouping elements (#72)
* Feat: Locking workspace in ``with`` block through ``lock()`` method (#62)
* Fix: On free plans, ignore errors when locking/unlocking workspaces (thanks @maximveksler)

0.4.0 (2021-02-05)
------------------
* Fix: Don't duplicate relationships if ``add_nearest_neighbours()`` called twice (#63)
* Fix: Support blank diagrams descriptions from the Structurizr UI (#40)
* Fix: External boundaries visible flag in ContainerView now preserved in JSON (#67)

0.3.0 (2020-11-29)
------------------
* Fix: Better error on bad ``ModelItem`` constructor argument (#50)
* Fix: Suppress archiving of downloaded workspaces by setting archive location to ``None`` (#54)
* Feat: Add ``DeploymentView`` (#55)

0.2.1 (2020-11-27)
------------------
* Docs: There is now documentation live at https://structurizr-python.readthedocs.io/

0.2.0 (2020-11-20)
------------------
* Fix: Add implied relationships to entities (#42)
* Fix: Add ``dump()``, ``dumps()`` and ``loads()`` methods to ``Workspace`` (#48)
* Fix: Add support for DeploymentNodes, ContainerInstances, SoftwareSystemInstances and InfrastructureNodes (#37)
* Fix: Remove need for Model in hydration methods (#52)

0.1.1 (2020-10-19)
------------------
* Fix: Adjust to change in httpx library API (#38)

0.1.0 (2020-10-15)
------------------
* Fix: Resolve overlap between add methods (#13)
* Fix: Add IDs to the big bank example (#16)
* Fix: Preserve tag order as in other SDKs (#22)
* Fix: Consistency of element relationships (#31)
* Add Python 3.9 to the test suite
