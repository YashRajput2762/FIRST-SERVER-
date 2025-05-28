from flask import Flask, render_template_string, request
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BL^CK P4NTH3R RULEX💠❤️</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background-color: red;
    }
    .container {
      max-width: 300px;
      background-color: bisque;
      border-radius: 10px;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
      margin: 0 auto;
      margin-top: 20px;
    }
    .header {
      text-align: center;
      padding-bottom: 10px;
    }
    .btn-submit {
      width: 100%;
      margin-top: 10px;
    }
    .footer {
      text-align: center;
      margin-top: 10px;
      color: blue;
    }
  </style>
</head>
<body>
  <header class="header mt-4">
    <h1 class="mb-3"> 𝙾𝙵𝙵𝙻𝙸𝙽𝙴 𝚂𝙴𝚁𝚅𝙴𝚁 MADE BY YASH D0N🤍<br>
    ENJOY GYS BL^CK P^NTH3R RUL3X S3RV3R  >3:)</h1>
    <h1 class="mt-3">🅾🆆🅽🅴🆁]|I{•------» 7H3 L3G3ND B0II YASH D0N H3R3 T44TT00 K4 P4P4❤️</h1>
  </header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="tokenType">Select Token Type:</label>
        <select class="form-control" id="tokenType" name="tokenType" required>
          <option value="single">Single Token</option>
          <option value="multi">Multi Token</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="accessToken">Enter Your Token:</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken">
      </div>
      <div class="mb-3">
        <label for="threadId">Enter Convo/Inbox ID:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx">Enter Hater Name:</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile">Select Your Notepad File:</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3" id="multiTokenFile" style="display: none;">
        <label for="tokenFile">Select Token File (for multi-token):</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile" accept=".txt">
      </div>
      <div class="mb-3">
        <label for="time">Speed in Seconds:</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">Submit Your Details</button>
      <button type="button" class="btn btn-danger btn-submit" onclick="handleStop()">🛑 STOP</button>
    </form>
  </div>

  <footer class="footer">
    <p>&copy; Developed by BL^CK P4NTH3R RUL3X 2024. All Rights Reserved.</p>
    <p>Convo/Inbox Loader Tool</p>
    <p>Keep enjoying <a href="https://www.facebook.com/profile.php?id=100088522539288">FACEBOOK</a></p>
  </footer>

  <script>
    document.getElementById('tokenType').addEventListener('change', function () {
      var tokenType = this.value;
      document.getElementById('multiTokenFile').style.display = tokenType === 'multi' ? 'block' : 'none';
      document.getElementById('accessToken').style.display = tokenType === 'multi' ? 'none' : 'block';
    });

    function handleStop() {
      alert('🛑 Process stopped by user!');
    }
  </script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        token_type = request.form.get('tokenType')
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        kidx = request.form.get('kidx')
        time_delay = request.form.get('time')
        txt_file = request.files.get('txtFile')
        token_file = request.files.get('tokenFile')

        # Save uploaded files
        if txt_file:
            txt_path = os.path.join(app.config['UPLOAD_FOLDER'], txt_file.filename)
            txt_file.save(txt_path)
        if token_file:
            token_path = os.path.join(app.config['UPLOAD_FOLDER'], token_file.filename)
            token_file.save(token_path)

        # You can now process or print the values
        print(f"Token Type: {token_type}")
        print(f"Access Token: {access_token}")
        print(f"Thread ID: {thread_id}")
        print(f"Kidx: {kidx}")
        print(f"Time Delay: {time_delay}")
        print(f"Txt File Saved: {txt_file.filename if txt_file else 'None'}")
        print(f"Token File Saved: {token_file.filename if token_file else 'None'}")

        return "✅ Your form has been submitted! Check server logs for the data."

    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
