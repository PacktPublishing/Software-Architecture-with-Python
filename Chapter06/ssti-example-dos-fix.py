# Code Listing #12

"""

SSTI - Server Side Template Injection example (using Flask) with DoS attack path
fixed.

"""

# ssti-example-dos-fix.py
from flask import Flask
from flask import request, render_template_string, render_template

app = Flask(__name__)
TEMPLATE = '''
<html>
 <head><title> Hello {{ person.name | e }} </title></head>
 <body> Hello {{ person.name | e }} </body>
</html>
'''

@app.route('/hello-ssti')
def hello_ssti():
    person = {'name':"world", 'secret': 'jo5gmvlligcZ5YZGenWnGcol8JnwhWZd2lJZYo=='} 
    if request.args.get('name'):
        person['name'] = request.args.get('name')

    return render_template_string(TEMPLATE, person=person)

if __name__ == "__main__":
    app.run(debug=True)
