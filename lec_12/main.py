
import random
import time

def createFile(filename):
    with open(filename, 'w') as f:
        for _ in range(100):
            numbers = [str(random.randint(1, 100)) for _ in range(20)]
            f.write(' '.join(numbers) + '\n')

def readAndFilterFile(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    processed_lines = []
    for line in lines:
        numbers = list(map(int, line.split()))
        filtered_numbers = list(filter(lambda x: x > 40, numbers))
        processed_lines.append(filtered_numbers)

    return processed_lines

def writeProcessedFile(filename, data):
    with open(filename, 'w') as f:
        for line in data:
            f.write(' '.join(map(str, line)) + '\n')

def readAsGenerator(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield list(map(int, line.split()))

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@measure_time
def main():
    filename = 'randNums.txt'
    createFile(filename)
    processed_data = readAndFilterFile(filename)
    writeProcessedFile(filename, processed_data)
    generator = readAsGenerator(filename)
    for _ in range(5):
        print(next(generator))

if __name__ == "__main__":
    main()
