import subprocess
import os
import tempfile
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS 

app = Flask(__name__)
CORS(app, resources={r"/run_code": {"origins": "http://127.0.0.1:3001"}})

@app.route('/run_code', methods=['POST'])
def run_code():
    data = request.get_json()
    code = data.get('code')
    language = data.get('language')
    
    if not code or not language:
        return jsonify({"output": "Error: Code or language not provided."}), 400

    # Create a temporary directory to store and run the code
    with tempfile.TemporaryDirectory() as temp_dir:
        output_data = ""
        error_data = ""
        
        try:
            if language == 'python':
                file_path = os.path.join(temp_dir, "script.py")
                with open(file_path, "w") as f:
                    f.write(code)
                
                result = subprocess.run(
                    ["python", file_path],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                output_data = result.stdout
                error_data = result.stderr
            
            elif language == 'cpp':
                file_path = os.path.join(temp_dir, "script.cpp")
                exe_path = os.path.join(temp_dir, "a.out")
                with open(file_path, "w") as f:
                    f.write(code)
                
                compile_result = subprocess.run(
                    ["g++", file_path, "-o", exe_path],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                if compile_result.stderr:
                    return jsonify({"output": compile_result.stderr})
                
                result = subprocess.run(
                    [exe_path],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                output_data = result.stdout
                error_data = result.stderr

            elif language == 'java':
                class_name = "Main"
                file_path = os.path.join(temp_dir, f"{class_name}.java")
                with open(file_path, "w") as f:
                    f.write(code)
                
                compile_result = subprocess.run(
                    ["javac", file_path],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                if compile_result.stderr:
                    return jsonify({"output": compile_result.stderr})
                
                result = subprocess.run(
                    ["java", "-classpath", temp_dir, class_name],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                output_data = result.stdout
                error_data = result.stderr

            else:
                return jsonify({"output": "Error: Unsupported language."}), 400

            full_output = (output_data + error_data).strip()
            if not full_output:
                full_output = "Code executed successfully, but produced no output."

            return jsonify({"output": full_output})

        except subprocess.TimeoutExpired:
            return jsonify({"output": "Error: Execution timed out. Possible infinite loop."}), 408
        except Exception as e:
            return jsonify({"output": f"An unexpected error occurred: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
