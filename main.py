import psutil

def get_tgid(pid):
	path = "/proc/{}/status".format(pid)
	f = open(path, "r")
	linhas = f.read().splitlines()
	for linha in linhas:
		if linha.startswith("Tgid"):
			return linha.split("	")[-1]

	return None

def get_data():
    print('PID\tTGID\tPPID\tNAME\tSTATE\tMEM_RES\tTHREADS')

    pids = psutil.pids()
    for pid in pids:
        proc = psutil.Process(pid)

        pid = proc.pid;
        ppid = psutil.Process.ppid(proc)
        name = psutil.Process.name(proc)
        state = psutil.Process.status(proc)
        memory = psutil.Process.memory_info(proc)
        res_memory = memory[0]
        threads = psutil.Process.num_threads(proc)
        tgid = get_tgid(pid)

        print(pid, '\t', tgid, '\t', ppid, '\t', name, '\t', state, '\t', res_memory, '\t', threads)


def main():
    get_data()

if __name__ == '__main__':
    main()