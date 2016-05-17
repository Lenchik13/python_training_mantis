import pytest
from data.add_project import constant as testdata


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_new_project(app, db, project):
    app.session.login("administrator", "root")
    old_projects = db.get_project_list()
    app.project.create(project)
    new_projects = db.get_project_list()
    assert len(new_projects) == len(old_projects) + 1