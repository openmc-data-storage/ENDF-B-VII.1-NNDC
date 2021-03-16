
import os
import unittest
import xml.etree.ElementTree as ET

import openmc

os.environ["OPENMC_CROSS_SECTIONS"] = '/share/h5_files/cross_sections.xml'


class TestH5FilesInSimulations(unittest.TestCase):

    def test_simulation_runs_with_isotopes(self):
        tree = ET.parse('/share/h5_files/cross_sections.xml')
        root = tree.getroot()   

        for elem in root:
            if elem.attrib['type'] == 'neutron':
                isotope_name = elem.attrib['materials']

                sett = openmc.Settings()
                sett.batches = 100
                sett.inactive = 0
                sett.particles = 500
                sett.run_mode = 'fixed source'

                mat1 = openmc.Material(1, "pure_isotope_material")
                mat1.add_nuclide(isotope_name, 1)
                mat1.set_density('g/cm3', 1)
                mats = openmc.Materials([mat1])

                outer_surface = openmc.Sphere(r=10, boundary_type='vacuum')
                cell1 = openmc.Cell(region=-outer_surface)
                cell1.fill = mat1
                universe = openmc.Universe(cells=[cell1])
                geom = openmc.Geometry(universe)

                model = openmc.model.Model(geom, mats, sett)
                model.run()
