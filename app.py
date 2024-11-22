from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Enter Numbers</h1>
    <form method="POST" action="/calculate_mean">
        <label for="numbers">Numbers (comma-separated):</label>
        <input type="text" id="numbers" name="numbers">
        <button type="submit">Calculate</button>
    </form>
    '''

@app.route('/calculate_mean', methods=['POST'])
def calculate_mean():
    numbers = request.form.get('numbers', '')
    try:
        # Split numbers by commas and convert to a list of floats
        numbers_list = [float(num) for num in numbers.split(',')]
        mean_value = sum(numbers_list) / len(numbers_list)
        return f'''
        <h1>The mean is: {mean_value}</h1>
        <a href="/">Back</a>
        '''
    except ValueError:
        return '''
        <h1>Error: Please enter valid numbers separated by commas.</h1>
        <a href="/">Back</a>
        '''

if __name__ == '__main__':
    app.run(debug=True)
