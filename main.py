from flask import Flask,render_template, url_for, redirect, request
import requests

app = Flask(__name__)

cat_endpoint = 'https://api.thecatapi.com/v1/images/search'
cat_api_key = 'live_DpyGTGanW9wn3fY1L7FVVlvxj4ckba2x8TMhSaildfJ69Kgsrf7YMedpi5oqHbb1'

HEADERS = {
    'x-api-key': cat_api_key
}

parameters = {
    'limit' : 3
}


@app.route('/')
def main():
    response = requests.get(cat_endpoint, params=parameters, headers=HEADERS)
    data_image = response.json()
    print(data_image)
    url_image = data_image[0]['url']
    print(url_image)
    urls = [data_image[it]['url'] for it in range(len(data_image))]
    print(urls)
    return render_template('index.html', img = urls)

@app.route('/new-random-image', methods=['GET', 'POST'])
def new_random():
    if request.method == 'POST':
        response_new = requests.get(cat_endpoint, params=parameters, headers=HEADERS)
        data_image_new = response_new.json()
        url_image_new = data_image_new[0]['url']

        new_urls = [data_image_new[it2]['url'] for it2 in range(len(data_image_new))]

        return redirect(url_for('main', img = new_urls))

if __name__ == "__main__":
    app.run(debug=True, port=5006)