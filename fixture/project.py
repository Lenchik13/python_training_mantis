import time

class ProjectHelper:

    def __init__(self, app):
        self.app = app


    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        # init group creations
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()
        self.fill_projects_form(project)
        # submit group creation
        wd.find_element_by_css_selector("input.button").click()


    def fill_projects_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)


    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_projects_page()
        self.select_project_by_id(id)
        time.sleep(3)
        #submit delision
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.get(self.app.base_url + 'manage_proj_edit_page.php?project_id=%s' % id)