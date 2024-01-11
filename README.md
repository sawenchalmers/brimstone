# Brimstone

This Grasshopper plugin retrieves data from Boverket's Klimatdatabas through API or file access, and makes data available in Grasshopper. The plugin is [available on Food4Rhino](https://www.food4rhino.com/en/app/brimstone?lang=en).

## Features
* Info about component contents is maintained in /dist_template/Readme.md

## Development

* Development is done in the GHPython components in the brimstone_[version].gh file

### Releasing a new version
* Version increments are done globally by updating `brimstone.globals.version` in brimstone.py file
* To save a new version of a component, make any changes, and then for each component go to File > Create User Object in Grasshopper
    * Change the sub-category to the current version
    * Unfortunately there is no way of automating this for now
* Make sure that /dist_template/README.md is up to date
* Make sure to push any changes to Git as detailed below
* Place the following files in /dist/brimstone_[version]/ and zip them: 
    * .ghuser files for each component
    * brimstone_[version].gh
    * brimstone.py
    * brimstone_data folder containing:
        * [version]klimatdatabas_hb_materials.json
        * [version]_HBKlimatdatabas.csv
        * klimatdatabas_[version].json
    * License.txt (can be found in /dist_template/)
    * README.md (can be found in /dist_template/)
* The pack_brimstone.py utility can automate this:
    * Run using `python pack_brimstone.py -v [version]`
    * Use at your own peril!
* Upload the .zip file to Food4Rhino

## Git usage (general)
* `git add .` to add all changes made
* `git commit -m"chore/fix/feat: short description of commit"` to document
    * Use `chore` for minor changes, `fix` for bug fix, `feat` for new feature

### Git usage (authorised users)

* `git pull` to get updates from server (fix any merge issues)
* `git push` to push to server

### Git usage (unauthorised users)

* In GitHub, navigate to https://github.com/sawenchalmers/brimstone/
* Create a fork
    * In the top bar, click "Fork" and "+ Create a new fork"
* Clone the fork
* Make any changes locally
* When you are ready to merge with the main branch, create a pull request
    * In GitHub, navigate to your forked repository
    * Press "sync changes" to get any changes from the main repository
    * In GitHub, navigate to https://github.com/sawenchalmers/brimstone/
    * Click "New pull request"
    * Click "compare across fork" under the page title
    * Select the main fork as the "base repository"
    * Select your fork as the "head repository"
    * Click "Create pull request"
    * Give the pull request a title and comments as relevant
    * Click "Create pull request"
    * Done!



## Contact

Author: Toivo Säwén, sawen@chalmers.se

## Changelog

### 0.1.6
*

### 0.1.5
* Fixed inconsistent encodings being used to read the JSON data
* Replaced Klimatdatabas API URL
* Updated database mapping from Klimatdatabas to Honeybee

### 0.1.4
* Fixed not being able to enter custom (string) data into the "Calculate Solid Geometry" component
* Added new components to create a resource and add it to the database
* Reorganised user objects
* Started refactoring to use global .py file rather than spread out information

### 0.1.3
* Added multiple components for interacting with Honeybee model
* These components require Ladybug Tools 1.6.0 to be installed.

### 0.1.2

* "Categories" component now outputs database version retrieved (if available)
* Added optional language input for API component
* Fixed `WebRequests` for use with Rhino 8 WIP
* Moved global plug-in information to new "Fly" component
* New component connects LCA data to solid geometry and calculates 

### 0.1.1

* Fixed bug with energy category
* Allow list access to resources
* Include name in output
* Allow for extracting custom data

### 0.1.0

* Initial version
