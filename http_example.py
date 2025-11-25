import httpx

# body
data = {
    "title": "новая задача",
    "completed": False,
    "userID": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", data=data)

print(response.status_code)
print(response.json())

# headers, может крашить
headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.status_code)

# query
params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print(response.status_code)
print(response.json())

# send file
files = {"file": ("test.txt", open("test.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files = files)

print(response.status_code)
print(response)

# клиенты, нужны для переиспользования tcp, для ускорения
# хеддеры и прочие параметры можно передавать на уровне базового клиента, для всх
with (httpx.Client(
        base_url="https://jsonplaceholder.typicode.com",
        headers={"Authorization": "Bearer my_secret_token"}
) as client):
    response1 = client.get("/todos/1")
    response2 = client.get("/todos/2")

    client.close()

    print("\n\n\n")
    print(response1.json())
    print(response2.json())

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/todos/invalid")
    response.raise_for_status() #ожидание на 200
except httpx.HTTPStatusError as e:
    print(f"ошибка запроса: {e}")

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout = 10)
except httpx.ReadTimeout as e:
    print(f"запрос превысил лимит времени: {e}")