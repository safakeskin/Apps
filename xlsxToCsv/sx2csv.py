import pandas as pd, sys, os
from pathlib import Path

def toCsv( fname ):
    x_f_name = fname.split('/')[-1]
    dir_path = '/'.join(fname.split('/')[:-1]) # fname directory
    csv_path = Path(dir_path) / 'csv' # output directory

    if csv_path.exists() and csv_path.is_dir():
        print("csv directory is found.")
    else:
        print("csv directory is not found.")
        csv_path.mkdir()
        print("csv directory is created.")

    with pd.ExcelFile(fname) as xl:
        for sheet in xl.sheet_names:
            f_path = csv_path / x_f_name.split('.')[0]
            f_path.mkdir(exist_ok=True)
            
            df = xl.parse(sheet, index_col=None)
            df.to_csv(f_path.as_posix() + '/' + sheet + '.csv', 
                encoding='utf-8', index=False)

def main(fnames):
    for fname in fnames:
        toCsv(fname)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Input file is not provided. Program will be terminated.")
    else:
        main( sys.argv[1:] )