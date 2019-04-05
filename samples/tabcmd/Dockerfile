FROM openjdk:8

ADD https://downloads.tableau.com/esdalt/2018.2.3/tableau-tabcmd-2018-2-3_all.deb /tableau-tabcmd-2018-2-3_all.deb

RUN apt-get install ./tableau-tabcmd-2018-2-3_all.deb
RUN ./opt/tableau/tabcmd/bin/tabcmd --accepteula > /dev/null

ENV PATH="/opt/tableau/tabcmd/bin:${PATH}"

CMD [ "bash" ]
