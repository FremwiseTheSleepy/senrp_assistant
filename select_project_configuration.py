
import sys
import os


def select_project_configuration(project_name="OneRing"):
    """
    Imports appropriate project's information
    :param project_name: string of project name to import, must match file structure
    :return: string, path to folder containing project specific information
    """
    if len(sys.argv) == 2:
        project_name = sys.argv[1]

    directory_path_of_file = os.path.dirname(__file__)
    project_configuration_path = os.path.join(directory_path_of_file, "Configurations", project_name)
    if os.path.exists(project_configuration_path):
        sys.path.append(project_configuration_path)
    return project_configuration_path
