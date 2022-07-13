from flask import Flask, jsonify
from flask import make_response 
from flask import abort

app = Flask(__name__) 

tasks = [ 
  { 
    'id': 1, 
    'title': 'Team 1',
    'name': 'Iva, Denus, Olya, Mykola', 
    'description': 'Develop Continious Integrtion',
    'project': 'CI', 
    'done': False 
  }, 
  { 
    'id': 2, 
    'title': 'Team 2',
    'name': 'Iva, Denus, Olya, Mykola', 
    'description': 'Develop Continious Delivery',
    'project': 'CD', 
    'done': True 
  } 
] 

@app.errorhandler(404) 
def not_found(error):
  return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/healthcheck/api/tasks', methods=['GET'])
def get_tasks():
  return jsonify({'tasks': tasks})

@app.route('/healthcheck/api/tasks/<int:task_id>', methods=['GET']) 
def get_task(task_id):
  print("***task_id= %s" % str(task_id))
  task = list(filter(lambda t: t['id'] == task_id, tasks))
  print("***len(task)= %s" % str(len(task)))
  if len(task) == 0: 
    abort(404)
  print(task[0])
  ret = task[0]
  print(ret)
  return jsonify({'task': ret})

if __name__ == '__main__': 
  app.run(host='0.0.0.0', debug=True, port=80)