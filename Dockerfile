
FROM openmc/openmc:develop

# Clones OpenMC data repo which contains the processing scripts
RUN git clone https://github.com/openmc-dev/data.git

# some nuclear data libr require unzip to decompress (e.g. Fendl 3.1d)
RUN apt-get install -y unzip

# Copies over the tests that simulate the h5 files
COPY tests tests/

ENV OPENMC_CROSS_SECTIONS=/share/cross_sections.xml
