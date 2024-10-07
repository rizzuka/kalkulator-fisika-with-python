from flask import Flask, render_template, redirect, url_for
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('badan.html')

@app.route('/run_glb')
def run_glb():
    script_path = os.path.join(os.getcwd(), 'glb.py')
    subprocess.run(['python', script_path], check=True)
    return redirect(url_for('home'))

@app.route('/run_glbb')
def run_glbb():
    script_path = os.path.join(os.getcwd(), 'glbb.py')
    subprocess.run(['python', script_path], check=True)
    return redirect(url_for('home'))

@app.route('/run_parabola')
def run_parabola():
    script_path = os.path.join(os.getcwd(), 'parabola.py')
    subprocess.run(['python', script_path], check=True)
    return redirect(url_for('home'))


@app.route('/run_vkawat')
def run_vkawat():
    script_path = os.path.join(os.getcwd(), 'volumekawat.py')
    subprocess.run(['python', script_path], check=True)
    return redirect(url_for('home'))


@app.route('/run_vkerucut')
def run_vkerucut():
    script_path = os.path.join(os.getcwd(), 'volumekerucut.py')
    subprocess.run(['python', script_path], check=True)
    return redirect(url_for('home'))


@app.route('/run_vsilinder')
def run_vsilinder():
    script_path = os.path.join(os.getcwd(), 'volumesilinder.py')
    subprocess.run(['python', script_path], check=True)
    return redirect(url_for('home'))


@app.route('/run_ek')
def run_ek():
    script_path = os.path.join(os.getcwd(), 'energikinetik.py')
    subprocess.run(['python', script_path], check=True)
    return redirect(url_for('home'))


@app.route('/run_hu')
def run_hu():
    script_path = os.path.join(os.getcwd(), 'HubunganUsaha.py')
    subprocess.run(['python', script_path], check=True)
    return redirect(url_for('home'))


@app.route('/run_usaha')
def run_usaha():
    script_path = os.path.join(os.getcwd(), 'usaha.py')
    subprocess.run(['python', script_path], check=True)
    return redirect(url_for('home'))

if __name__ == "__main__":
  print("Starting Flask server...")
  app.run(debug=True)
