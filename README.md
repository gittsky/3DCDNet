# Python

## devcontainer setup
When first using the repo copy the `.devcontainer/devcontainer.json.EXAMPLE` to the `.devcontainer/devcontainer.json`.
This is your local file that should not be pushed and can contain paths to the local file system or the GPU config on the Deep Learning server.

## launch.json
If possible only use to the docker container relative paths here, this allows debugging configurations to easily be shared between developers. 
Ideally no changes are necessary when sharing code that uses the repo, as long as both have configured their local devcontainer.json

## doc/tutorials
This folder is used as a placeholder and can be deleted once the templates are not needed.

## docs this should automatically build sphynx documentation
if it is not needed it can be removed aswell, howver then the part in the gitlab.ci.yml corresponding to it also has to be removed.

## docker
should a custom docker image be needed, this can be generated in the docker/Dockerfile. This abstracts the "development" docker file from the dependencies, as otherwise when restarting vscode the whole docker has to be rebuilt. 

to use your own Dockerfile edit the docker/Dockerfile, then set your desired ci tag in the Dockerfile for example: `conreg.ipmlan.ipm.fraunhofer.de/of/pointcloudpioneers/libraries/geo-tabulator:dev`
Following this the Docker Image has to be build ant tagged: `docker build -t conreg.ipmlan.ipm.fraunhofer.de/of/pointcloudpioneers/libraries/geo-tabulator:dev -f docker/Dockerfile .`

after this simply use the vscode extension `Dev Containers` and select reopen in container.

In case this does not work double check your GPU settings and the mounted local folders specified in the devcontainer.json

## CI

there is a minimum ci example present in this project. It builds the docker image and uploads it to the container registry. It also builds the sphynx documentation. 