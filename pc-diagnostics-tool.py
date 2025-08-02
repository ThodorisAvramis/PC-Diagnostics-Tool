from diagnostics.cpu import get_cpu_info

if __name__ == '__main__':
    cpu = get_cpu_info()
    print("=== CPU Information ===")
    for key, value in cpu.items():
        print(f"{key}: {value}")
