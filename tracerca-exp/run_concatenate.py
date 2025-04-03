import pickle
from pathlib import Path

import click


@click.command()
@click.option('-i', '--input', 'input_files', multiple=True)
@click.option('-o', '--output', 'output_file')
@click.option('--add-root-cause', is_flag=True, default=False)
def main(input_files, output_file, add_root_cause):
    output_file = Path(output_file)
    output_file.parent.mkdir(exist_ok=True)
    
    all_data = []
    for input_file in input_files:
        with open(input_file, 'rb') as f:
            data = pickle.load(f)
            all_data.extend(data)
    
    with open(output_file, 'wb') as f:
        pickle.dump(all_data, f)

if __name__ == '__main__':
    main()