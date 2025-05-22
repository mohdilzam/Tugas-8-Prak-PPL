from django.http import HttpResponse
from django.shortcuts import render

ITEMS = {
    'elektronik': [
        {'id': 1, 'nama': 'Laptop Acer', 'deskripsi': 'Laptop ringan untuk kerja', 'toko': 'TokoA'},
        {'id': 2, 'nama': 'Kamera Canon', 'deskripsi': 'Kamera untuk profesional', 'toko': 'TokoB'},
    ],
    'pakaian': [
        {'id': 1, 'nama': 'Kaos Hitam', 'deskripsi': 'Nyaman dan stylish', 'toko': 'TokoFashion'},
    ]
}

def dashboard(request):
    kategori_list = ITEMS.keys()
    return render(request, 'produk/dashboard.html', {'kategori_list': kategori_list})

def item_kategori(request, kategori):
    items = ITEMS.get(kategori, [])
    return render(request, 'produk/item_kategori.html', {'kategori': kategori, 'items': items})

def detail_item(request, kategori, item_id):
    items = ITEMS.get(kategori, [])
    item = next((i for i in items if i['id'] == item_id), None)
    return render(request, 'produk/detail_item.html', {'item': item})

def toko(request, nama_toko):
    produk = [item['nama'] for k in ITEMS.values() for item in k if item['toko'] == nama_toko]
    return render(request, 'produk/toko.html', {'nama_toko': nama_toko, 'produk': produk})

def about(request):
    return render(request, 'produk/about.html')
