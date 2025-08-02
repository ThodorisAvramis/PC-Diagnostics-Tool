import psutil

def get_cpu_info():
    return {
        "cores": psutil.cpu_count(logical=False),
        "logical_cores": psutil.cpu_count(logical=True),
        "frequency": psutil.cpu_freq().current,
        "usage": psutil.cpu_percent(interval=1)
    }

    from diagnostics.cpu import get_cpu_info

    if __name__ == '__main__':
        cpu = get_cpu_info()
        print("=== CPU Information ===")
        for k, v in cpu.items():
            print(f"{k}: {v}")