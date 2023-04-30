import multiprocessing

# Funktion, die auf einem anderen Prozessor ausgeführt werden soll
def thread_decreaser():
    # Hier kommen die Anweisungen für die zu erledigende Aufgabe
    pass

def thread_increaser():
    pass
    
# Hauptprogramm
if __name__ == '__main__':
    # Anzahl der Prozessoren ermitteln
    num_processors = multiprocessing.cpu_count()
    print('count processors: ' + str(num_processors))
    
    # Pool von Prozessen erstellen
    pool = multiprocessing.Pool(processes=num_processors)

    # Aufgabe auf jedem Prozessor im Pool ausführen
    #pool.map(task_on_another_processor, range(num_processors))

    # Pool schließen
    pool.close()
    pool.join()
