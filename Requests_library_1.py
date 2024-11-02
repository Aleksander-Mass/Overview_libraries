# Выбор библиотек `requests`, `numpy` и `matplotlib`, так как они позволяют продемонстрировать разнообразные задачи:
# работу с веб-запросами, анализ данных и визуализацию.
#
# ### 1. Библиотека `requests`
#
# Библиотека `requests` упрощает отправку HTTP-запросов в Python. С её помощью можно взаимодействовать с веб-API,
# скачивать данные с сайтов и выполнять другие сетевые операции.
#
# *Пример использования `requests`:

import requests

# 1. Отправка GET-запроса на сайт JSONPlaceholder для получения данных
response = requests.get("https://jsonplaceholder.typicode.com/posts")
if response.status_code == 200:
    print("Data retrieved successfully")
else:
    print("Failed to retrieve data")

# Вывод на консоль:
# => Data retrieved successfully

# # 2. Извлечение JSON данных из ответа
data = response.json()
print(f"Number of posts: {len(data)}")
print("First post:", data[0])

# Вывод на консоль:
# =>
"""
Data retrieved successfully
Number of posts: 100
First post: {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 
             'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut 
              quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
"""

# 3. Отправка POST-запроса с JSON данными (создание нового поста)
post_data = {
    "title": "Test Post",
    "body": "This is a test post",
    "userId": 1
}
post_response = requests.post("https://jsonplaceholder.typicode.com/posts", json=post_data)
print("Response for POST request:", post_response.json())

# Вывод на консоль:
# =>
"""
Data retrieved successfully

Number of posts: 100
First post: {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 
             'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut 
              quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}
              
Response for POST request: {'title': 'Test Post', 'body': 'This is a test post', 'userId': 1, 'id': 101}
"""
# Библиотека `requests`: Эта библиотека значительно упрощает работу с сетевыми запросами в Python, позволяя быстро
# интегрировать веб-данные в приложения.