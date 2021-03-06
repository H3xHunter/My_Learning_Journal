import random
import os
import hashlib

ORIG_FILE_NAME = "license_2"
ORIG_OUT = "origin_out"
PARAMETER = "AAAAAAAAAA"

FUZZ_FILE_NAME = "license_2_fuzzed"
FUZZ_OUT = "fuzz_out"

os.system("./license_2 {} > origin_out".format(PARAMETER))


def flip_it(stringy):
    element = random.randint(0, len(stringy) - 1)
    random_ascii_char = chr(random.randint(0, 255))
    in_bytes = bytes(random_ascii_char, "latin-1")
    return stringy[:element] + in_bytes + stringy[element + 1:]


def check_output():
    os.system("./{} {} > {}".format(FUZZ_FILE_NAME, PARAMETER, FUZZ_OUT))
    return md5_check(ORIG_OUT) == md5_check(FUZZ_OUT)


def md5_check(file):
    with open(file, 'rb') as fh:
        md5 = hashlib.md5()
        while True:
            data = fh.read(8129)
            if not data:
                break
            md5.update(data)
        return md5.hexdigest()


while True:
    try:
        with open(ORIG_FILE_NAME, "rb") as original_f, open(FUZZ_FILE_NAME, "wb") as fuzzed:
            os.system("chmod 777 license_2_fuzzed")
            fuzzed.write(flip_it(original_f.read()))
            fuzzed.close()
    except Exception as e:
        break

    if check_output() and md5_check(ORIG_FILE_NAME) != md5_check(FUZZ_FILE_NAME):
        print("{} - {}\nFound it".format(md5_check(ORIG_FILE_NAME),md5_check(FUZZ_FILE_NAME))
        break
    else:
        os.system("rm fuzz_out")
        os.system("rm license_2_fuzzed")
        continue
   
