from flask import Flask, render_template, request
import requests
import pandas as pd
import matplotlib.pyplot as plt
import os 
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    plot_url = None

    if request.method == 'POST':
        start_year = int(request.form['start_year'])
        end_year = int(request.form['end_year'])
        
        
        API_KEY = os.getenv("API_KEY")
        url = f"https://api.stlouisfed.org/fred/series/observations?series_id=CPIAUCSL&api_key={API_KEY}&file_type=json"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

           
            df = pd.DataFrame(data['observations'])
            df['value'] = df['value'].astype(float)
            df['date'] = pd.to_datetime(df['date'])

           
            inflation_start_year = df[df['date'].dt.year == start_year]['value'].values[0] if not df[df['date'].dt.year == start_year].empty else 0

           
            df['normalized_inflation'] = ((df['value'] - inflation_start_year) / inflation_start_year) * 100

            
            df_filtered = df[(df['date'].dt.year >= start_year) & (df['date'].dt.year <= end_year)]

           
            average_normalized_inflation = df_filtered['normalized_inflation'].mean()
            print(f"Average Normalized Inflation Rate from {start_year} to {end_year}: {average_normalized_inflation:.2f}%")

            plt.figure(figsize=(10, 6))
            plt.plot(df_filtered['date'], df_filtered['normalized_inflation'], label='Normalized Inflation Rate', color='blue')
            plt.axhline(0, color='red', linestyle='--', label='0% Inflation')
            plt.xlabel('Year')
            plt.ylabel('Normalized Inflation (%)')
            plt.title(f'Normalized U.S. Inflation ({start_year} - {end_year})')
            plt.legend()
            plt.grid()
            plt.xticks(rotation=45)  
            plt.tight_layout()
            
            plot_path = 'static/inflation_plot.png'
            plt.savefig(plot_path)
            plt.close()
            
            plot_url = plot_path
        else:
            print(f"Error fetching data: {response.status_code} - {response.text}")

    return render_template('index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)

