import os

def getRandomFields():
    file_name = 'random_fields.csv';
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_path, 'r') as f:
        lines = f.readlines()
        result = []
        # print each line
        for line in lines:
            #remove the newline character
            line = line.replace('\n', '')
            fields = line.split(',')
            result.append({
                "name": fields[0],
                "value": fields[1:]
                })
    return result
