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