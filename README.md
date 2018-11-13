# Containerized Tableau REST API and TABCMD client
 
## Containerized Tableau REST API client 

Docker for the official [Tableau REST API client](https://github.com/tableau/server-client-python).

## Build image

```bash
    cd rest-api-client-docker/src/main/docker/defailt/
    docker build .
```

## Use the image to publish data source

Run the following command (That will mount the folder (LOCALFOLDER) containing the datasource (DATASOURCE) you wish to publish as a volume and start an interactive session with publishing script started):

```bash
    docker run -v <LOCALFOLDER>:/Data \
        -it -t image_tag_name \
        /publish_datasource.py \
        --server <SERVER> \
        --project <TARGETPROJECT> \
        --filepath /Data/<DATASOURCE>.tdsx \
        --username <USERNAME> \
        --password <PASSWORD> \
        --logging-level error
```
> Notice that *TARGETPROJECT* is a name of the project, not a full name and that due to the existing limitation of client package we are using it is not possible to correctly target the project if its name is not unique accross all top level and nested projects. So if you have the following projects *Project1*, *Project2*/*Project1*, *Project1*/*Project3* then only *Project2* and *Project3* (*Project1*/*Project3*) could be used as a target project name. But when you specify *Project1* as a target it will be resolved either as *Project1* or as *Project2*/*Project1*.

You can target a specific site name using `--siteid` parameter.

## Use the image to publish workbook

Run the following command (That will mount the folder (LOCALFOLDER) containing the workbook (WORKBOOK) you wish to publish as a volume and start an interactive session with publishing script started):

```bash
    docker run -v <LOCALFOLDER>:/Data \
        -it -t image_tag_name \
        /publish_workbook.py \
        --server <SERVER> \
        --project <TARGETPROJECT> \
        --showtabs no \
        --filepath /Data/<WORKBOOK>.twbx \
        --username <USERNAME> \
        --password <PASSWORD> \
        --logging-level error
```

You can target a specific site name using `--siteid` parameter.

## How to create a stand-alone repro container for a publishing failure?

1. Create a new docker file that uses this image as a base (e.g. `FROM image_tag_name`)
2. Embedd the content file (twb, twbx, tdsx, tds, tde, hyper) into the image (e.g. `ADD ./<CONTENTFILE> <CONTENTFILE>`)
3. Add bash script to publish that file using either publish_workbook or publish_datasource script that accept server/site/project/username/password as parameters. (e.g. `ADD ./<BASHFILE> <BASHFILE>`)
4. Grant execute permissions for it. (e.g. `RUN chmod +x <BASHFILE>`)
5. Specify to use it as entrypoint (e.g. `ENTRYPOINT ["<bashfile>"]`)

## Containerized Tabcmd client 

Docker for the official [Tabcmd client](https://onlinehelp.tableau.com/current/server/en-us/tabcmd.htm).

## Build image

```bash
    cd tabcmd-client-docker/src/main/docker/defailt/
    docker build .
```

## Use the image to publish data source/workbooks

Run the following command (That will mount the folder (LOCALFOLDER) containing the datasource (CONTENTFILE) you wish to publish as a volume and start an interactive session with publishing script started):

```bash
    docker run -v <LOCALFOLDER>:/Data \
        -it -t image_tag_name
```

That will connect you to the container's terminal. Now sign in to the server:

```bash
    cd ./opt/tableau/tabcmd/bin/
    ./tabcmd --accepteula
    ./tabcmd login --no-certcheck --server <SERVER> --username <USERNAME> --password <PASSWORD>
```

Then trigger the publishing:

```bash
    ./tabcmd publish /Data/<CONTENTFILE> -o --no-certcheck
```

## How to create a stand-alone repro container for a publishing failure?

1. Create a new docker file that uses this image as a base (e.g. `FROM image_tag_name`)
2. Embedd the content file (twb, twbx, tdsx, tds, tde, hyper) into the image (e.g. `ADD ./<CONTENTFILE> <CONTENTFILE>`)
3. Add bash script to publish that file using either publish_workbook or publish_datasource script that accept server/site/project/username/password as parameters. (e.g. `ADD ./<BATCHFILE> <BATCHFILE>`)
4. Specify to use it as entrypoint (e.g. `ENTRYPOINT ["<BATCHFILE>"]`)


## Contribution

We are using git flow - create a branch from develop, commit/push then PR back to develop. This [document](./CONTRIBUTING.md) describes the contribution process in details.
