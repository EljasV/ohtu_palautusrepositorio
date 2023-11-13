class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, project_license, authors):
        self.name = name
        self.description = description
        self.project_license = project_license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_array(self, dependencies):
        return "\n- ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.project_license or '-'}"
            f"\n"
            f"\nAuthors: \n- {self._stringify_array(self.authors)}"
            f"\n"
            f"\nDependencies: \n- {self._stringify_array(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies: \n- {self._stringify_array(self.dev_dependencies)}"
        )
