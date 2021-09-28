## NY helper 
    is my assistant for managing my projects.
    we plan to create our own project management system, with integration with github and everything else, perhaps we will add a graph interface.


## Install    
    to install, just clone the repository and run installer.sh in the repository folder
    `./installer.sh`
    the rest will be distributed by itself

## Manage
    2 command are now available
- `nys [-h] [--name NAME] [--dir DIR] [--env ENV] [--desk DESK]` creates a new project and adds it to the database, env will create a virtual python environment (by default, false)
- `nyb [name project]` builds the project into exe and packs it into a zip archive, you must specify the name of the project
