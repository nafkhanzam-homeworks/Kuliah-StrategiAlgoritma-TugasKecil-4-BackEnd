import sys
import json

if __name__ == "__main__":
    data = json.loads(sys.argv[1])
    print(data)
