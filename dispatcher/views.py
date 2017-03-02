from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone
from .models import Client, LabRequest, MedCenRequest, ReqCategory, Delivery
import random


def load_main(request):
    clients = Client.objects.all()
    return render(request, 'dispatcher/clients.html', {'clients': clients})


def sort(request, param):

    clients = Client.objects.filter(Q(last_name__startswith=param))
    return render(request, 'dispatcher/clients.html', {'clients': clients})


def lab_request(request):

    lab_rqsts = LabRequest.objects.all()
    return render(request, 'dispatcher/lab_req.html', {'lab_rqsts': lab_rqsts})


def sort_lab_request(request, param):

    lab_rqsts = LabRequest.objects.order_by(param)
    return render(request, 'dispatcher/lab_req.html', {'lab_rqsts': lab_rqsts})


def med_request(request):

    med_rqsts = MedCenRequest.objects.all()
    return render(request, 'dispatcher/med_req.html', {'med_rqsts': med_rqsts})


def sort_med_request(request, param):

    med_rqsts = MedCenRequest.objects.order_by(param)
    return render(request, 'dispatcher/med_req.html', {'med_rqsts': med_rqsts})


def create_two_clients():
    first_names = (
    'Агапит', 'Булат', 'Рамиз', 'Лука', 'Исмаил', 'Раймонд', 'Никола', 'Давид', 'Ждан', 'Рустам', 'Платон', 'Ян',
    'Трофим', 'Еремей', 'Владлен')
    last_names = (
    'Прохоров', 'Афанасьев', 'Комаров', 'Воронов', 'Горбунов', 'Муравьёв', 'Тетерин', 'Гуляев', 'Антонов', 'Елисеев',
    'Кулаков', 'Орехов', 'Якушев', 'Авдеев', 'Агафонов')
    middle_names = (
    'Ермилич', 'Евфимиевич', 'Диомидович', 'Власиевич', 'Бенедиктович', 'Викторович', 'Климентович', 'Исаакиевич',
    'Кондратович', 'Якубович', 'Феликсович', 'Фролович', 'Эрнстович', 'Фомич', 'Авраамович')
    client = Client(first_name=get_name(first_names), last_name=get_name(last_names), middle_name=get_name(middle_names), sex='m', birthday=timezone.now())
    client.save()
    Client.objects.create(first_name=get_name(first_names), last_name=get_name(last_names), middle_name=get_name(middle_names), sex='m', birthday=timezone.now())


def get_name(fn_list):
    name = random.choice(fn_list)
    return name


def create_lab_request():
    catecgry = random.choice(ReqCategory.objects.all())
    client = Client.objects.all()
    lab = LabRequest(serial_number=get_req_number(), category=catecgry, create_date=timezone.now(), client=random.choice(client))
    lab.save()
    category2 = random.choice(ReqCategory.objects.all())
    lab2 = LabRequest(serial_number=get_req_number(), create_date=timezone.now())
    lab2.category =category2
    lab2.client =random.choice(client)
    lab2.save()


def create_med_request():
    category = random.choice(ReqCategory.objects.all())
    client = Client.objects.all()
    deliv = Delivery.objects.all()
    med = MedCenRequest(serial_number=get_req_number(), category=category, create_date=timezone.now(),
                         client=random.choice(client), req_delivery=random.choice(deliv))
    med.save()
    category2 = random.choice(ReqCategory.objects.all())
    med = MedCenRequest(serial_number=get_req_number(), create_date=timezone.now())
    med.category = category2
    med.client = random.choice(client)
    med.req_delivery = random.choice(deliv)
    med.save()


def get_req_number():

    number = 0
    while LabRequest.objects.filter(serial_number=number).count != 0 and number == 0:
        number = random.randrange(999999)
    return number


def get_format_req():

    req_list = LabRequest.objects.filter(client__first_name='Еремей', client__last_name='Авдеев', client__middle_name='Викторович')

    return req_list.count()


def get_format_start_req():

    req_list = LabRequest.objects.filter(Q(client__last_name__startswith='А') & Q(client__first_name__startswith='А'))

    return req_list.count()


def get_format_number_req():

    req_list = LabRequest.objects.filter(serial_number__lte=4500)

    return req_list.count()


def req_change():

    client = Client.objects.get(first_name='Еремей', last_name='Авдеев', middle_name='Викторович')

    LabRequest.objects.filter(client=client).update(modify_date=timezone.now())



def req_delete():

    req_list = LabRequest.objects.filter(serial_number__lte=4500)

    req_list.delete()
