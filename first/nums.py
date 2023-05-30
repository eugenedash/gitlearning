import uuid
#random UUID
uuid.uuid4()

class Dispatcher:
    def __init__(self):
        self.crews = {}  # Словарь для хранения информации о бригадах

    def receive_request(self, address, patient_info):
        # Обработка заявки на получение скорой помощи
        request_id = self.generate_request_id()  # Генерация уникального идентификатора заявки
        request = {
            'address': address,
            'patient_info': patient_info,
            'status': 'received'
        }
        self.update_request(request_id, request)  # Обновление информации о заявке
        print(f"Получена заявка с ID {request_id} на адрес {address} с информацией о больном: {patient_info}")

    def inform_crew(self, request_id, patient_condition):
        # Информирование бригады о состоянии больного
        if request_id in self.crews:
            crew = self.crews[request_id]
            crew['patient_condition'] = patient_condition
            crew['status'] = 'informed'
            self.update_crew(request_id, crew)  # Обновление информации о бригаде
            print(f"Состояние больного по заявке {request_id}: {patient_condition}. Бригада уведомлена.")
        else:
            print(f"Заявка с ID {request_id} не найдена.")

    def dispatch_crew(self, request_id):
        # Отправка бригады на указанный адрес
        if request_id in self.crews:
            crew = self.crews[request_id]
            crew['status'] = 'dispatched'
            self.update_crew(request_id, crew)  # Обновление информации о бригаде
            print(f"Бригада для заявки {request_id} выезжает на адрес {crew['address']}")
        else:
            print(f"Заявка с ID {request_id} не найдена.")

    def generate_request_id(self):
        # Генерация уникального идентификатора заявки
        # В реальной системе это может быть, например, генерация случайного числа или использование временной метки
        return str(uuid.uuid4())

    def update_request(self, request_id, request):
        # Обновление информации о заявке
        # В реальной системе здесь может быть взаимодействие с базой данных или другим хранилищем
        # В данном примере мы просто сохраняем информацию в словаре
        self.crews[request_id] = request

    def update_crew(self, request_id, crew):
        # Обновление информации о бригаде
        # В реальной системе здесь может быть взаимодействие с базой данных или другим хранилищем
        # В данном примере мы просто обновляем информацию в словаре
        self.crews[request_id] = crew

    def main(self):
        # Основная функция для взаимодействия с пользователем
        address = input("Введите адрес вызова: ")
        patient_info = input("Введите информацию о больном: ")

        self.receive_request(address, patient_info)
        request_id = list(self.crews.keys())[-1]  # Получение последнего созданного идентификатора заявки
        patient_condition = input("Введите состояние больного: ")
        self.inform_crew(request_id, patient_condition)
        self.dispatch_crew(request_id)


def receive_request(address, patient_info):
    pass

def inform_crew(patient_condition):
    pass

def dispatch_crew(address):
    pass

def receive_request(address, patient_info):
 # Обработка заявки на получение скорой помощи
    pass

def inform_crew(patient_condition):
    # Информирование бригады о состоянии больного
    pass

def dispatch_crew(address):
    # Отправка бригады на указанный адрес
    pass

def main():
    # Основная функция для взаимодействия с пользователем
    pass

if __name__ == "__main__":
    dispatcher = Dispatcher()
    dispatcher.main()