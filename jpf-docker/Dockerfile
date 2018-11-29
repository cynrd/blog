FROM openjdk:8
# install dependencies
RUN apt update && apt install -y ant 
# copy junit related files
RUN mkdir /jpf 
COPY junit /jpf/junit
# clone repositories
RUN cd jpf && git clone https://github.com/javapathfinder/jpf-core.git && git clone https://github.com/SymbolicPathFinder/jpf-symbc.git
# copy site.properties
RUN mkdir /root/.jpf
COPY site.properties /root/.jpf/site.properties
# build jpf packages
RUN cd jpf/jpf-core && ./gradlew buildJars
RUN export JUNIT_HOME=/jpf/junit && cd /jpf/jpf-symbc && ant build
