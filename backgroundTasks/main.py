import time
import multiprocessing as mp

from py import check_the_sys_args
from py import start_database_updating_engine

def run():

    check_the_sys_args()

    processes = []
    p = mp.Process(target = start_database_updating_engine)
    p.start()
    processes.append(p)





    while any([p.is_alive() for p in processes]):
        time.sleep(30)
    for p in processes:
        p.join()


if __name__ == "__main__":
    run()