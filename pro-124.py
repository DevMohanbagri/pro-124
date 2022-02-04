from flask import Flask,jsonify,request

app = Flask(__name__)

# creating a array a of tasks with each task as a different obj in it
contact = [
    {
        "Contact": "123456789",
        "Name": "Raju",
        "done": False,
        "id" : 1
    },
    {
        
        "Contact": "987654321",
        "Name": "Rahul",
        "done": False,
        "id": 2
    }
]

@app.route('/add-data',methods = ['POST'])
def add_task():
    if(not request.json):
        return jsonify({
            "status": "error",
            "message": "Please provide the data",
        },400)
    
    task = {
        'id': contact[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact',""),
        'done': False
    }
    contact.append(task)
    return jsonify({
        "status": "Success",
        "message": "Task added successfully",
    })

@app.route('/get-data')
def get_task():
    return jsonify({
        "data":contact,
    })

if(__name__=='__main__'):
    app.run(debug=True)
