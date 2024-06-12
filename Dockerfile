# docker build -t esys-particle . --no-cache
# docker run -ti -e OMPI_ALLOW_RUN_AS_ROOT=1 -e OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1 -v ${PWD}:/simulation esys-particle


### SELECT 1 OF THE FOLLOWING FROM STATEMENTS
# Uncomment for Mac/Linux execution
FROM muro230/custom-esys-particle-3:vainilla

# Uncomment for Windows execution
#FROM muro230/custom-esys-particle-3-windows:vainilla

WORKDIR /simulation

RUN apt update && apt install python3-pip -y
RUN pip install h5py

CMD ["sh", "main/run.sh"]
