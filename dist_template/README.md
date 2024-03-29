# Brimstone 0.1.7

This Grasshopper plugin retrieves data from Boverket's Klimatdatabas through API or file access, and makes data available in Grasshopper.

## Contents

This .zip file contains:

* Brimstone - Add Life Cycle Info to Honeybee Construction.ghuser
* Brimstone - Add Life Cycle Info to Honeybee Material.ghuser
* Brimstone - Add resource to Klimatdatabas data.ghuser
* Brimstone - Calculate Embodied Carbon of Honeybee Model.ghuser
* Brimstone - Calculate Operational Emissions.ghuser
* Brimstone - Calculate Solid Geometry.ghuser
* Brimstone - Create Klimatdatabas resource.ghuser
* Brimstone - Fly!.ghuser
* Brimstone - Get Categories.ghuser
* Brimstone - Get LCA Data.ghuser
* Brimstone - Get Resources.ghuser
* Brimstone - Honeybee Construction from Klimatdatabas materials.ghuser
* Brimstone - Modify thicknesses of Honeybee materials.ghuser
* brimstone_0.1.7.gh
* brimstone.py
* brimstone_data folder
    * 230728_HBKlimatdatabas.csv
    * 231208brimstone_constructions.json
    * 231211klimatdatabas_hb_materials.json
    * 231219hb_boverket_energy_schedules.json
    * klimatdatabas_02.05.000.json
* README.md (this file)
* License.txt

## Install instructions

* Extract the .zip file
* Move the .ghuser files and brimstone.py into the Grasshopper "User Objects" folder (accessed through File > Special Folders > User Objects in the GH interface)
* Move the brimstone_data folder and its contents into the Grasshopper "User Objects" folder as above
* Consult the included .gh file for example usage
* Optionally use the included database json file instead of API

## Contact

Author: Toivo Säwén, sawen@chalmers.se