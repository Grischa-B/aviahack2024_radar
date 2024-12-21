# stats/influxdb_client.py

from influxdb_client import InfluxDBClient
import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# Чтение переменных окружения
INFLUXDB_URL = os.getenv('INFLUXDB_URL', 'http://localhost:8086')
INFLUXDB_TOKEN = os.getenv('INFLUXDB_TOKEN')
INFLUXDB_ORG = os.getenv('INFLUXDB_ORG')
INFLUXDB_BUCKET = os.getenv('INFLUXDB_BUCKET')

# Проверка наличия переменных окружения
if not all([INFLUXDB_URL, INFLUXDB_TOKEN, INFLUXDB_ORG, INFLUXDB_BUCKET]):
    raise ValueError("Не все необходимые переменные окружения заданы.")

# Создание клиента InfluxDB
client = InfluxDBClient(url=INFLUXDB_URL, token=INFLUXDB_TOKEN, org=INFLUXDB_ORG)

@csrf_exempt
def create_record(request):
    """
    POST метод для записи данных в InfluxDB
    """
    if request.method != 'POST':
        return JsonResponse({"status": "error", "message": "Invalid request method. Only POST allowed."}, status=405)

    try:
        # Чтение данных из тела запроса
        data = json.loads(request.body)

        # Проверка наличия обязательных полей
        required_fields = {"dateCreate", "claim_count", "suggestion_count", "thank_count", "average_rank", "SLI"}
        if not required_fields.issubset(data.keys()):
            return JsonResponse({"status": "error", "message": f"Missing required fields: {required_fields - data.keys()}"}, status=400)

        # Преобразование даты в ISO формат
        timestamp = datetime.strptime(data['dateCreate'], "%Y-%m-%d %H:%M:%S").isoformat() + "Z"

        # Проверка, существует ли запись с такой же датой
        query = f"""
            from(bucket: "{INFLUXDB_BUCKET}")
              |> range(start: 0)
              |> filter(fn: (r) => r._measurement == "daily_statistics")
              |> filter(fn: (r) => r._time == {timestamp})
              |> limit(n: 1)
        """
        query_api = client.query_api()
        result = query_api.query(query=query, org=INFLUXDB_ORG)

        if result:  # Если есть результаты, значит, запись с этой датой уже существует
            return JsonResponse({"status": "error", "message": "Record with the specified date already exists."}, status=400)

        # Формирование точки для записи
        point = {
            "measurement": "daily_statistics",
            "time": timestamp,
            "fields": {
                "claim_count": int(data['claim_count']),
                "suggestion_count": int(data['suggestion_count']),
                "thank_count": int(data['thank_count']),
                "average_rank": float(data['average_rank']),
                "SLI": int(data['SLI'])
            }
        }

        # Запись данных в InfluxDB
        write_api = client.write_api()
        write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point)

        return JsonResponse({"status": "success", "message": "Data written to InfluxDB"})

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

@csrf_exempt
def read_records_by_date(request):
    if request.method != 'GET':
        return JsonResponse({"status": "error", "message": "Invalid request method. Only GET allowed."}, status=405)

    date = request.GET.get('date')
    if not date:
        return JsonResponse({"status": "error", "message": "Missing required 'date' parameter in query string."}, status=400)

    try:
        # Форматируем дату для поиска
        start_date = f"{date}T00:00:00Z"
        end_date = f"{date}T23:59:59Z"

        query = f'''
        from(bucket: "{INFLUXDB_BUCKET}")
          |> range(start: {start_date}, stop: {end_date})
          |> filter(fn: (r) => r["_measurement"] == "daily_statistics")
        '''

        query_api = client.query_api()
        result = query_api.query(query, org=INFLUXDB_ORG)

        def transform_response(result):
            """Преобразует ответ InfluxDB в компактный JSON."""
            transformed_data = {}
            for table in result:
                for record in table.records:
                    field = record.get_field()
                    value = record.get_value()
                    transformed_data[field] = value
            return transformed_data

        # Форматируем данные в JSON
        # result_data = []
        # for table in result:
        #     for record in table.records:
        #         result_data.append({
        #             "time": str(record.get_time()),
        #             "fields": record.values
        #         })
        formatted_data = transform_response(result)

        if not formatted_data:
            return JsonResponse({"status": "success", "message": "No data found for the specified date.", "data": []})

        return JsonResponse({"status": "success", "data": formatted_data})

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
    
@csrf_exempt
def update_record(request):
    """PATCH метод для обновления данных в InfluxDB."""
    if request.method != 'PATCH':
        return JsonResponse({"status": "error", "message": "Invalid request method. Only PATCH allowed."}, status=405)

    date = request.GET.get('date')
    if not date:
        return JsonResponse({"status": "error", "message": "Missing required 'date' parameter in query string."}, status=400)

    try:
        # Форматируем дату для поиска
        start_date = f"{date}T00:00:00Z"
        end_date = f"{date}T23:59:59Z"

        # Чтение данных из тела запроса
        data = json.loads(request.body)

        # Проверка наличия обязательных полей для обновления
        required_fields = {"dateCreate"}
        if not required_fields.issubset(data.keys()):
            return JsonResponse({"status": "error", "message": f"Missing required fields: {required_fields - data.keys()}"}, status=400)

        # Преобразование даты в ISO формат
        timestamp = datetime.strptime(data['dateCreate'], "%Y-%m-%d %H:%M:%S").isoformat() + "Z"

        # Проверка, существует ли запись с такой же датой
        query = f'''
        from(bucket: "{INFLUXDB_BUCKET}")
          |> range(start: {start_date}, stop: {end_date})
          |> filter(fn: (r) => r["_measurement"] == "daily_statistics")
        '''
        query_api = client.query_api()
        result = query_api.query(query=query, org=INFLUXDB_ORG)

        if not result:  # Если записи нет, вернуть ошибку
            return JsonResponse({"status": "error", "message": "No record found with the specified date."}, status=400)

        # Составляем объект для обновления
        fields_to_update = {}

        # Обновление полей, если они присутствуют в запросе
        if 'average_rank' in data:
            fields_to_update['average_rank'] = float(data['average_rank'])
        if 'SLI' in data:
            fields_to_update['SLI'] = int(data['SLI'])
        if 'claim_count' in data:
            fields_to_update['claim_count'] = int(data['claim_count'])
        if 'suggestion_count' in data:
            fields_to_update['suggestion_count'] = int(data['suggestion_count'])
        if 'thank_count' in data:
            fields_to_update['thank_count'] = int(data['thank_count'])

        # Если нет полей для обновления, возвращаем ошибку
        if not fields_to_update:
            return JsonResponse({"status": "error", "message": "No fields provided for update."}, status=400)

        # Формирование точки для обновления
        point = {
            "measurement": "daily_statistics",
            "time": timestamp,
            "fields": fields_to_update
        }

        # Запись обновленных данных в InfluxDB
        write_api = client.write_api()
        write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point)

        return JsonResponse({"status": "success", "message": "Data updated successfully."})

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)
