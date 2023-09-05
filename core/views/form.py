# class AjaxView(View):
#     def post(self, request, *args, **kwargs):
#         # Получите данные из POST запроса
#         data = json.loads(request.body)
#         name = data.get('name')
#         phone = data.get('phone')
#         question = data.get('question')
#         category = data.get('category')
#
#         # Создайте объект модели и сохраните данные
#         your_model_instance = YourModel(name=name, phone=phone, question=question, category=category)
#         your_model_instance.save()
#
#         # Верните успешный JSON-ответ
#         response_data = {'message': 'Данные успешно сохранены'}
#         return JsonResponse(response_data)
