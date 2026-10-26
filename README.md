python -m pip install -r requirements.txt

#uruchomienie sprawdzenia błędów
python -m ruff check . 

#naprawa błędów oznaczonych [*]
python -m ruff check . --fix