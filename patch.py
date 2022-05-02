#!/usr/bin/python
import subprocess
import sys

# b8 01 00 00 00    mov $0x0, %eax
# c3                ret
CODE = bytes.fromhex('b8 01 00 00 00 c3')


def main():
    if len(sys.argv) != 2:
        print(f"Usage {sys.argv[0]} <path of libmkl_core.so>")
        return 1
    try:
        output = subprocess.check_output(
            f'objdump -T {sys.argv[1]} | grep mkl_serv_intel_cpu',
            shell=True,
            text=True).rstrip('\n').split('\n')
        offsets = [int(i.split(' ')[0], 16) for i in output]

    except subprocess.CalledProcessError:
        print("no mkl symbols was found.")
        return 1

    try:
        with open(sys.argv[1], 'r+b') as file:
            for offset in offsets:
                file.seek(offset, 0)
                file.write(CODE)
        print("patch succeed")
    except PermissionError:
        print(
            "cannot write to file, do you have write permission to the file?")

    return 0


if __name__ == "__main__":
    sys.exit(main())
