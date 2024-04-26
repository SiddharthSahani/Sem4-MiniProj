from flask import Flask, request, render_template
import pandas as pd
import pickle


app = Flask(__name__)

#TODO: ADD CSS

@app.route("/model.html", methods=['GET', 'POST'])
def model():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400

        file = request.files['file']
        if file.filename == '':
            return 'No file selected', 400

        if not file.filename.endswith('.csv'):
            return 'Invalid file format. Only CSV files are allowed', 400

        df = pd.read_csv(file.stream)
        
        df.columns = ['duration', 'src_bytes', 'dst_bytes', 'su_attempted', 'num_root', 'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate']
        
        with open('KNN.sav', 'rb') as file:
            model = pickle.load(file)

        predictions = model.predict(df)

        df['predictions'] = predictions

        html_table = df.to_html(classes='table table-striped', index=False)
        html_table = df[['duration', 'src_bytes', 'dst_bytes', 'su_attempted', 'predictions']].to_html(classes='table table-striped', index=False)
        return render_template('model.html', table=html_table)
    
    return render_template('model.html')


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

