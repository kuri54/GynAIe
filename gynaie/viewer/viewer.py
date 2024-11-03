import pandas as pd
import streamlit as st
from pathlib import Path
from PIL import Image

PROJECT_ROOT_DIR = Path(__file__).parents[2].resolve()
INPUT_ROOT_DIR = PROJECT_ROOT_DIR / 'input'
RESULT_ROOT_DIR = PROJECT_ROOT_DIR / 'result'

CHECKED_COLUMN = 'checked'

def load_available_dirs():
    if isinstance(RESULT_ROOT_DIR, Path) and RESULT_ROOT_DIR.exists() and RESULT_ROOT_DIR.is_dir():
        available_dirs = [d.name for d in RESULT_ROOT_DIR.iterdir() if d.is_dir()]
    else:
        available_dirs = []
    return available_dirs

@st.cache_data(show_spinner=False)
def load_image(image_path):
    return Image.open(image_path)

def run():
    available_dirs = load_available_dirs()

    st.title('GynAIe Image Viewer')

    if available_dirs:
        selected_dir = st.sidebar.selectbox('Select a directory:', available_dirs)

        if selected_dir:
            RESULT_DIR = RESULT_ROOT_DIR / selected_dir
            INPUT_DIR = INPUT_ROOT_DIR / selected_dir
            summary_image_path = RESULT_DIR / f'{selected_dir}.jpg'

            if summary_image_path.exists():
                summary_image = Image.open(summary_image_path)
                st.sidebar.image(summary_image, caption=f'{summary_image_path.name}', use_column_width=True)

            csv_path = RESULT_DIR / f'{selected_dir}_result.csv'
            if csv_path.exists():
                df = pd.read_csv(csv_path)

                if CHECKED_COLUMN not in df.columns:
                    df[CHECKED_COLUMN] = 0

                unique_labels = df['pred_label'].unique()
                unique_cases = df['case'].unique()

                st.sidebar.header('Filter Options')
                selected_case = st.sidebar.selectbox('Filter by Case:', ['All'] + list(unique_cases))
                selected_label = st.sidebar.selectbox('Filter by Label:', ['All'] + list(unique_labels))
                checked_filter = st.sidebar.selectbox('Filter by Checked Status:', ['All', 'Checked', 'Unchecked'])

                filtered_df = df
                if selected_label != 'All':
                    filtered_df = filtered_df[filtered_df['pred_label'] == selected_label]

                if selected_case != 'All':
                    filtered_df = filtered_df[filtered_df['case'] == selected_case]

                if checked_filter == 'Checked':
                    filtered_df = filtered_df[filtered_df[CHECKED_COLUMN] == 1]
                elif checked_filter == 'Unchecked':
                    filtered_df = filtered_df[filtered_df[CHECKED_COLUMN] == 0]

                st.sidebar.write(f'Number of images selected: {len(filtered_df)}')

                st.header('Images')
                columns = st.columns(3)

                for idx, row in filtered_df.iterrows():
                    with columns[idx % 3]:
                        try:
                            image = load_image(row['path'])
                            st.image(image, use_column_width=True)
                        except FileNotFoundError:
                            st.warning(f"Image not found: {row['path']}")

                        col1, col2 = st.columns([1, 2])
                        with col1:
                            checked = st.checkbox('Checked', value=bool(row[CHECKED_COLUMN]), key=f'checkbox_{idx}', label_visibility='hidden')
                        with col2:
                            st.caption(f"{Path(row['path']).name}  \nLabel: {row['pred_label']}  \nScore: {row['pred_score']}")
                        
                        if checked != row[CHECKED_COLUMN]:
                            df.at[idx, CHECKED_COLUMN] = int(checked)

                df.to_csv(csv_path, index=False)

    else:
        st.write('No result directories found.')

if __name__ == '__main__':
    run()