#Cykl pracy: Dockerfile -(docker build)-> obraz Dockera -(docker run)-> Kontener 

FROM python:3.12

WORKDIR / app

#pierwsza kropka skąd bierzemy pliki, druga kropka gdzie będą kopiowane - tu do katalogu app
#polecenie COPY nie wybiera automatycznie potrzebnych plików, stąd stosowaie .dockerignore
COPY . .

#podczas budowania obrazu instaluje naszą aplikację i jej zależności. Kropka na kóńcu oznacza bieżący katalog, w kórym znajduje się plik pyproject.toml
#--no-cache-dir - nie zapisuje pamięci podręcznej pobranych pakietów pip
RUN pip install --no-cache-dir .

#określenie polecenia uruchomieniowego
CMD ["research-analyzer"]
