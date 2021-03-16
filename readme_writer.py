
"""Automatically writes the README.md markdown file for the templated
repository."""

import os

full_repo_name = os.getenv('GITHUB_REPOSITORY')
repo_name = full_repo_name.split('/')[-1]


new_readme = ('[![process_test_h5_files](https://github.com/{}/actions/workflows/process_test_nuc_data.yml/badge.svg)](https://github.com/openmc-data-storage/{}/actions/workflows/process_test_nuc_data.yml)\n\n'
    'Nuclear data from the {} library in h5 file format for use in OpenMC.\n\n'
    "Automatically processed in the OpenMC h5 file format using GitHub actions CI pipline.\n\n"
    "The generated h5 files have also be tested in simulations using OpenMC.\n\n"
    "Interfaces with the [openmc_data_downloader](https://github.com/openmc-data-storage/openmc_data_downloader) to provide easy nuclear data downloading.\n").format(full_repo_name, repo_name, repo_name)

with open("README.md", "w") as text_file:
    text_file.write(new_readme)
