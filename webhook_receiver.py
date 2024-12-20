from flask import Flask, jsonify, request 
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    if request.method == 'POST':
        print(request.method)
        payload = request.json  
        json_string = json.dumps(payload)
        print(f"Received payload is here...: \n {json_string}")  
        return jsonify(payload), 200
    return jsonify({"error": "Invalid method..."}), 405

# home route
# @app.route('/', methods=['POST', 'GET'])
# def home():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         data = fetch_repos(username, GITHUB_TOKEN)
#         print(data)
#         return render_template('home.html', data=data)
#     return render_template('home.html')

# # fetch data from api
# def fetch_repos(username, github_token):
#     headers = {
#         "Authorization": f"token {github_token}",
#         "Accept": "application/vnd.github.v3+json"
#     }

#     try:
#         response = requests.get(f"{GITHUB_API_URL}/users/{username}", headers=headers)
        
#         """
#         {GITHUB_API_URL}/users/{username}/repos
#         {GITHUB_API_URL}/users/{username}
#         """

#         if response.status_code == 200:
#             print(response.json()['login'])
#             data = {
#                 'owner_name': response.json()['login'],
#                 'github_url': response.json()['html_url'],
#                 'owned_private_repos': response.json()['owned_private_repos'],
#                 'public_repos': response.json()['public_repos'],
#                 'followers': response.json()['followers'],
#                 'following': response.json()['following'],
#                 'created_at': response.json()['created_at']
#             }
#             return data
#         else:
#             return 'error'
#         # else:
#         #     return jsonify({
#         #         "error": "Failed to fetch data from GitHub",
#         #         "status_code": response.status_code,
#         #         "message": response.json().get('message')
#         #     }), response.status_code

#     except Exception as e:
#         return jsonify({"error": "An error occurred", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
