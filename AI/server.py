from flask import Flask, request, jsonify
import json
from flask_cors import CORS
from helper_functions import filter_by_coordinates
from llm import generate_batch_report


app = Flask(__name__)

CORS(app)

@app.route('/getDataWithinBounds', methods=['GET'])
def getDataWithinBounds():
    # process data through function
    lat_min = float(request.args.get('lat_min'))
    lat_max = float(request.args.get('lat_max'))
    lon_min = float(request.args.get('lon_min'))
    lon_max = float(request.args.get('lon_max'))

    filtered_data = filter_by_coordinates(lat_min, lat_max, lon_min, lon_max)
    filtered_data = filtered_data.drop(columns=['RMA'])

    # Convert DataFrame to dictionary
    df_dict = filtered_data.to_dict(orient='records')  # Converts DataFrame to a list of dictionaries
    
    # Return JSON response
    return jsonify(df_dict)  # `jsonify` can handle lists of dictionaries

@app.route('/askGemini', methods=['POST'])
def askGemini():
    # Get JSON data from the request body
    data = json.loads(request.data)
    
    # Check if data is not None
    if data is None:
        return jsonify({'error': 'Invalid JSON data'}), 400
    
    print(type(data))
    
    response = generate_batch_report(data)

    return response

if __name__ == "__main__":
    app.run(debug=True)