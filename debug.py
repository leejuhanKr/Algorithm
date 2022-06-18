import os,sys
# 파이썬 디버깅

# TEST_CODE_PATH = "test.py"
# TEST_CASE_PATH = "testcase.txt"

# command = f'python3 {TEST_CODE_PATH} < {TEST_CASE_PATH}'

# os.system(command)


# 프로그래머스 디버깅
commands = [
    'echo "" > tmp_carrage.txt',
    'cat testcase.txt tmp_carrage.txt test.py > tmp_test.py',
    # 'python3 tmp_test.py'
    # 'rm -rf tmp_test.py'
]
for command in commands:
    os.system(command)



