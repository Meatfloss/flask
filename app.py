from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            # verify login credential

            return redirect('/resource')
        except:
            return 'error for login'

    else:
        return render_template('login.html')

@app.route('/account', methods=['POST', 'GET'])
def account():
    if request.method == 'POST':
        try:
            # save data to database

            return redirect('/account')
        except:
            return 'error for account'

    else:
        return render_template('account.html')

@app.route('/resource', methods=['POST', 'GET'])
def resource():
    if request.method == 'POST':
        try:
            # verify login credential

            return redirect('/resource')
        except:
            return 'error for login'

    else:
        return render_template('resource.html')

@app.route('/list')
def resource_list():
    # get reources information, get data from database instead of dummy data
    class resource:  
        def __init__(self, orderId, name, usage, system, cpu, memory, price, status, detail):  
            self.orderId = orderId  
            self.name = name 
            self.usage = usage 
            self.system = system 
            self.cpu = cpu 
            self.memory = memory 
            self.price = price 
            self.status = status 
            self.detail = detail
   
    resources = [resource("13242", "test", "testUsage", "1", "1","1","1","待审批", "详细信息"), resource("13243", "test2", "testUsage", "2", "2","2","2","已通过", "一、什么是冠状病毒？冠状病毒是自然界广泛存在的一类病毒，因该病毒形态在电镜下观察类似王冠而得名。二、什么是新型冠状病毒？冠状病毒是一个大型病毒家族，已知可引起感冒以及中东呼吸综合征和严重急性呼吸综合征等疾病。此次武汉等地区的新型冠状病毒是一种先前尚未在人类中发现的新型冠状病毒。")]


    return render_template('list.html', resources = resources)

@app.route('/approve')
def approve():
    # get reources information, get data from database instead of dummy data
    class resource:  
        def __init__(self, orderId, name, usage, system, cpu, memory, price, status, detail, approvedBy):  
            self.orderId = orderId  
            self.name = name 
            self.usage = usage 
            self.system = system 
            self.cpu = cpu 
            self.memory = memory 
            self.price = price 
            self.status = status 
            self.detail = detail
            self.approvedBy = approvedBy
   
    resources = [resource("13242", "test", "testUsage", "1", "1","1","1","待审批", "详细信息", "小北"), resource("13243", "test2", "testUsage", "2", "2","2","2","已通过", "一、什么是冠状病毒？冠状病毒是自然界广泛存在的一类病毒，因该病毒形态在电镜下观察类似王冠而得名。二、什么是新型冠状病毒？冠状病毒是一个大型病毒家族，已知可引起感冒以及中东呼吸综合征和严重急性呼吸综合征等疾病。此次武汉等地区的新型冠状病毒是一种先前尚未在人类中发现的新型冠状病毒。", "小董，小楠，小曦，小北")]


    return render_template('approve.html', resources = resources)
        
if __name__ == "__main__":
    app.run(debug=True)