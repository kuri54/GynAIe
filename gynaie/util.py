import pandas as pd
from natsort import natsorted
from pathlib import Path
from gynaie.check import handle_error_and_exit, check_supported_model, check_csv_exists
from gynaie.check import check_single_csv, check_csv_name_matches_directory, check_case_counts_match
from gynaie.models import base_model
from gynaie.check import log_message

def print_logo():
    logo = r"""
             _____                          _____
            / ___ |                  /\    |_   _|
           | |  __  _   _  _ __     /  \     | |    ___
           | | |_ || | | || '_ \   / /\ \    | |   / _ \
           | |__| || |_| || | | | / ____ \  _| |_ |  __/
            \_____| \__, ||_| |_|/_/    \_\|_____| \___|
                     __/ |
                    |___/
            """

    print(logo)

def get_image_path_to_df(input_dir):
    input_dir = Path(input_dir)
    image_path_list = natsorted([str(path) for path in input_dir.glob('**/*.jpg')])
    case_csv = list(input_dir.glob('*.csv'))

    # Ensure there is at least one CSV file in the directory.
    try:
        check_csv_exists(case_csv)
        log_message('CSV file successfully located.', 'success')
    except Exception:
        handle_error_and_exit()

    # Ensure there is exactly one CSV file in the directory.
    try:
        check_single_csv(case_csv)
        log_message('Exactly one CSV file found, proceeding with processing.', 'success')
    except Exception:
        handle_error_and_exit()

    case_df = pd.read_csv(str(case_csv[0]))
    case_name = case_csv[0].stem
    log_message(f'Case: {case_name}', 'notice')

    # Validate that CSV name matches the directory name.
    try:
        check_csv_name_matches_directory(input_dir, case_name)
        log_message('CSV file name matches the directory name.', 'success')
    except Exception:
        handle_error_and_exit()

    path_df = pd.DataFrame(data={'path': image_path_list})

    # add group
    def extract_group(path):
        parts = path.split('/')
        return parts[-2]

    path_df['case'] = path_df['path'].apply(extract_group)

    # Check for consistency between case counts in CSV and extracted paths.
    try:
        check_case_counts_match(case_df, path_df)
        log_message('Case counts in the CSV match the unique case entries in the path data.', 'success')
        log_message(f"Number of cases: {len(path_df['case'].unique())}", 'notice')
    except Exception:
        handle_error_and_exit()

    return path_df, case_df, case_name

def get_model_id(model_name):
    check_supported_model(model_name) # Check if the model name is supported.
    log_message(f'Model: {model_name}', 'notice')

    return base_model.get(model_name, {}).get('model_id')

def get_label(model_name):
    return base_model.get(model_name, {}).get('label')

def save_df(result_df, calculated_df, result_dir, case_name):
    result_df.to_csv(f'{result_dir}/{case_name}/{case_name}_result.csv', index=False)
    calculated_df.to_csv(f'{result_dir}/{case_name}/{case_name}_calculated.csv', index=False)