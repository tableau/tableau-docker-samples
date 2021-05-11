FROM openjdk:8-jre

ADD https://downloads.tableau.com/esdalt/2021.1.0/tableau-tabcmd-2021-1-0_all.deb /tableau-tabcmd.deb

RUN apt-get update \
  && apt-get -y install ./tableau-tabcmd.deb \
  && ./opt/tableau/tabcmd/bin/tabcmd --accepteula > /dev/null

ENV PATH="/opt/tableau/tabcmd/bin:${PATH}"

CMD [ "bash" ]
