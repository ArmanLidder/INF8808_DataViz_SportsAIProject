import os
from get_df import load_data
from Noe.preprocess import preprocess as noe_preprocess
from Arman.preprocess import preprocess as arman_preprocess
from khedrO.preprocess import preprocess_data
from Abdel.preprocess import preprocess as abdel_preprocess
from Amadeus.preprocess import preprocess as amadeus_preprocess
from Ibrahima.preprocess import preprocess as ibrahima_preprocess

match_infos, match_stats, player_stats, line_ups = load_data()


print("Processing data... please wait.")
data = noe_preprocess(match_infos, match_stats)
radar_data = arman_preprocess(match_stats)
bubble_data = preprocess_data(match_infos, player_stats, line_ups)
df_metrics, df_foot = abdel_preprocess(player_stats, line_ups)
df_amadeus = amadeus_preprocess(player_stats, line_ups)
df_ibrahima = ibrahima_preprocess(player_stats)


current_dir = os.path.dirname(os.path.abspath(__file__))
clean_dir = os.path.join(current_dir, 'assets', 'data', 'clean')
os.makedirs(clean_dir, exist_ok=True)


data.to_csv(os.path.join(clean_dir, 'noe_data.csv'), index=False)
radar_data.to_csv(os.path.join(clean_dir, 'arman_radar.csv'), index=False)
bubble_data.to_csv(os.path.join(clean_dir, 'khedro_bubble.csv'), index=False)
df_metrics.to_csv(os.path.join(clean_dir, 'abdel_metrics.csv'), index=False)
df_foot.to_csv(os.path.join(clean_dir, 'abdel_foot.csv'), index=False)
df_amadeus.to_csv(os.path.join(clean_dir, 'amadeus_data.csv'), index=False)
df_ibrahima.to_csv(os.path.join(clean_dir, 'ibrahima_tackles.csv'), index=False)

print("Data baking complete! Pre-baked files saved in src/assets/data/clean/")
