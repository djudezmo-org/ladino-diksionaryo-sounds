from yaml import safe_load
import os

def load_sounds():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sounds = {}
    #print(root)
    with open(os.path.join(root, 'people.yaml')) as fh:
        people = safe_load(fh)
    #print(people)
    folders = set(filter(lambda name: os.path.isdir(os.path.join(root, 'docs', name)) and name not in ['.git', 'ladino'], os.listdir(os.path.join(root, 'docs'))))
    #print(list(folders))
    difference = set(people.keys()).difference(set(folders))
    #print(people.keys())
    #print(folders)
    if difference:
        raise Exception(difference)
    for folder in folders:
        #print(folder)
        sound_files = set(os.listdir(os.path.join(root, 'docs', folder)))
        #print(sound_files)
        filenames = set(item['file'] for item in  people[folder]['files'])
        #print(filenames)
        if sound_files != filenames:
            exit("Not the same")
    for folder in people:
        for sound in people[folder]['files']:
            ladino = sound['ladino']
            if ladino not in sounds:
                sounds[ladino] = []
            sounds[ladino].append({
                'filename': folder + '/' + sound['file'],
                'nombre': people[folder]['nombre'],
                'titulo': people[folder]['titulo'],
            })

    return sounds


if __name__ == '__main__':
    sounds = load_sounds()
    print("Looks good")
    print(sounds)
