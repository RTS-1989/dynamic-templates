import csv
from django.shortcuts import render


def get_inflation_info(file: csv):
    with open(file, encoding='utf8', newline='') as inf:
        list_of_inflation = [item for item in csv.reader(inf, delimiter=';')]
        return list_of_inflation


def inflation_view(request):
    # чтение csv-файла и заполнение контекста
    inflation_info = get_inflation_info('inflation_russia.csv')
    for item in inflation_info[1:]:
        for i in item:
            if not i:
                i_ind = item.index(i)
                item.pop(i_ind)
                item.insert(i_ind, '-')
    template_name = 'inflation.html'
    context = {
               'header': inflation_info[0],
               'inflation': inflation_info[1:]
    }

    return render(request, template_name,
                  context)
