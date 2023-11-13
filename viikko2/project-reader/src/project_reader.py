from urllib import request

import toml

from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        loaded = toml.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        tool_poetry = loaded["tool"]["poetry"]
        dependencies_array = tool_poetry["dependencies"].keys()
        dev_dependencies_array = tool_poetry["group"]["dev"]["dependencies"].keys()
        return Project(tool_poetry["name"], tool_poetry["description"], dependencies_array, dev_dependencies_array,
                       tool_poetry["license"], tool_poetry["authors"])
