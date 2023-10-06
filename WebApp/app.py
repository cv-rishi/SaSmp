from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Sample data for labeling
data_to_label = [
    {"id": 1, "text": "This product is fantastic!", "sentiment": None},
    {"id": 2, "text": "I had a terrible experience with their customer service.", "sentiment": None},
    # Add more data entries as needed
]

# Index route to display the labeling interface
@app.route('/')
def index():
    global data_to_label
    if len(data_to_label) == 0:
        return "No more data to label!"
    entry = data_to_label.pop(0)  # Get the first entry
    return render_template('index.html', entry=entry)

# Route to handle labeling submission
@app.route('/label', methods=['POST'])
def label():
    global data_to_label
    sentiment = request.form.get('sentiment')
    entry_id = request.form.get('entry_id')  # Add a hidden input field in your HTML to include the entry_id
    
    if sentiment:
        with open('labeled_data.csv', mode='a', newline='') as csvfile:
            fieldnames = ['id', 'text', 'sentiment']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Find the corresponding entry in data_to_label by ID
            labeled_entry = next((entry for entry in data_to_label if entry['id'] == int(entry_id)), None)
            
            if labeled_entry:
                writer.writerow({'id': entry_id, 'text': labeled_entry['text'], 'sentiment': sentiment})
    
    if data_to_label:
        entry = data_to_label.pop(0)  # Get the next entry
        return render_template('index.html', entry=entry)
    else:
        return "No more data to label!"

if __name__ == '__main__':
    app.run(debug=True)

