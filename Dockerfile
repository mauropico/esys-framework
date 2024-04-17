# docker build -t esys-settling .
# docker run -ti -e OMPI_ALLOW_RUN_AS_ROOT=1 -e OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1 -v ${PWD}:/usr/local/bin esys-settling

FROM muro230/esys-particle

WORKDIR /usr/local/bin

RUN apt update && apt install python3-pip -y
RUN pip install h5py

CMD ["sh", "main/run.sh"]
