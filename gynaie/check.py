import sys
import traceback
from rich.console import Console
from gynaie.models import base_model, get_supported_models

console = Console()
def error_message(message):
    # console.print(message, style='bold red')
    console.log(message, style='bold red')

def pass_message(message):
    #  console.print(message, style='bold green')
    console.log(f'Success! {message}', style='bold green')

def notification_message(message):
    # console.print(message)
    console.log(f'Notice {message}', style='bold yellow')

def handle_error_and_exit():
    tb = traceback.format_exc()
    last_line = tb.strip().split('\n')[-1]
    # print(last_line)
    error_message(last_line)
    sys.exit(1)

def check_supported_model(model_name):
    if model_name not in base_model:
        supported_models = ', '.join(get_supported_models())

        raise ValueError(f'Unsupported model {model_name}. Supported models are: {supported_models}')

def check_csv_exists(case_csv):
    if not case_csv:
        raise FileNotFoundError(f'No CSV file found in the input directory')

def check_single_csv(case_csv):
    if len(case_csv) > 1:
        raise ValueError(f'More than one CSV file found in the input directory. Only one is expected.')

def check_csv_name_matches_directory(input_dir, case_name):
    directory_name = input_dir.name

    if case_name != directory_name:
        raise ValueError(f'CSV name "{case_name}" does not match directory name "{directory_name}".')

def check_case_counts_match(case_df, path_df):
    if 'case' not in case_df.columns:
        raise ValueError('The CSV file does not contain a "case" column.')

    csv_case_count = case_df['case'].nunique()
    path_case_count = path_df['case'].nunique()

    if csv_case_count != path_case_count:
        raise ValueError(f'The number of unique cases in CSV ({csv_case_count}) does not match the unique cases in path_df ({path_case_count}).')