import os
import argparse
from gynaie.calcuate_anomaly_score import CalcAnomalyScore
from gynaie.check import log_message
from gynaie.util import get_image_path_to_df, get_model_id, get_label, print_logo, save_df
from gynaie.sereening import Evaluater
from gynaie.viz import Vis

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--input_dir', type= str, required=True)
parser.add_argument('--result_dir', type= str, default='result')
parser.add_argument('--model_name', type= str, default='GynAIe-preview-clip-vit-large-patch14-336-8bit')
parser.add_argument('--batch_size', type= int, default=32)
parser.add_argument('--num_workers', default=os.cpu_count()//2)
parser.add_argument('--min_image_count', type= int, default=50,
                    help='Cases with fewer images than this number are marked as inadequate.')
parser.add_argument('--sort_by', default=['anomaly_score', 'age'])
parser.add_argument('--sort_ascending', default=[False, True])

def main():
    print_logo()

    input_df, case_df, case_name = get_image_path_to_df(args.input_dir)
    model_id = get_model_id(args.model_name)

    evaluater = Evaluater(input_df,
                          model_id,
                          get_label(args.model_name),
                          args.batch_size,
                          args.num_workers
                          )

    result_df = evaluater.run_evaluation()

    calc_anomaly_score = CalcAnomalyScore(result_df,
                                          case_df,
                                          get_label(args.model_name)[1],
                                          args.min_image_count
                                          )

    calculated_df = calc_anomaly_score.run_calc()

    vis = Vis(calculated_df, args.sort_by, args.sort_ascending, args.result_dir, case_name)
    vis.run_vis()

    save_df(result_df, calculated_df, args.result_dir, case_name)

    log_message(f"{case_df['case'].nunique()} cases have been successfully screening! Check the output files for detailed results.", 'notice')

if __name__ == '__main__':
    args = parser.parse_args()

    main()