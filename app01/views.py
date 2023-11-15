from django.shortcuts import render
from django.http import JsonResponse
from app01 import models
# Create your views here.
def index(request):
    return render(request,"index.html")
def customers_get_data(request):
    customers = models.Customers.objects.all()
    cts=[]
    for customer in customers:
        cts.append({"id":customer.id,
                    "name":customer.name,
                    "family":customer.family,
                    "birth_year":customer.birth_year,
                    "ssn":customer.ssn,
                    "tel":customer.tel,
                    "address":customer.address
                   })
    return JsonResponse({"customers":cts})
def customers_store(request):
    id = int(request.POST["id"])
    if id == 0 :
        name = request.POST["name"]
        family = request.POST["family"]
        birth_year = request.POST["birth_year"]
        ssn = request.POST["ssn"]
        tel = request.POST["tel"]
        address = request.POST["address"]
        customers = models.Customers.objects.create(name = name , family=family,birth_year=birth_year,ssn=ssn,tel=tel,address=address)
        return JsonResponse({"message":"saved"}) 
    else:
        customer = models.Customers.objects.get(id=id)
        customer.name = request.POST["name"]
        customer.family = request.POST["family"]
        customer.birth_year = request.POST["birth_year"]
        customer.ssn = request.POST["ssn"]
        customer.tel = request.POST["tel"]
        customer.address = request.POST["address"]
        customer.save()
        return JsonResponse({"message":"saved"})
def customers_delete(request,id):
    customer = models.Customers.objects.get(id=id)
    customer.delete()
    return JsonResponse({"message":"success"})
def brands_get_data(request):
    brands = models.Brand.objects.all()
    brnd=[]
    for brand in brands:
        brnd.append({"id":brand.id,
                    "name":brand.name})
    return JsonResponse({"brands":brnd})
def brands_store(request):
    id = int(request.POST["id"])
    if id == 0:
        name = request.POST["brand"]
        if len(models.Brand.objects.filter(name = name))==0:
            models.Brand.objects.create(name = name)
            return JsonResponse({"message":"saved"})
        else:
            return JsonResponse({"message":"error"})
    else :
        brand = models.Brand.objects.get(id=id)
        brand.name = request.POST["brand"]
        brand.save()
        return JsonResponse({"message":"saved"})
def brands_delete(request,id):
    brand = models.Brand.objects.get(id=id)
    products = models.Product.objects.filter(brand=brand)
    if len(products)==0:
        brand.delete()
        return JsonResponse({"error":False,"message":"success"})
    else:
        return JsonResponse({"error":True,"message":"brand is alreaady in use"})
def sellers_get_data(request):
    sellers = models.Seller.objects.all()
    slr=[]
    for seller in sellers:
        slr.append({"id":seller.id,
                    "name":seller.name,
                    "address":seller.address})
    return JsonResponse({"sellers":slr})
def sellers_store(request):
    name = request.POST["name"]
    address = request.POST["address"]
    sellers = models.Seller.objects.create(name = name,address=address)
    sellers.save()
    return JsonResponse({"message":"saved"}) 
def sellers_delete(request,id):
    seller = models.Seller.objects.get(id=id)
    seller.delete()
    return JsonResponse({"message":"success"})
def categories_get_data(request):
    categories = models.Category.objects.all()
    ctg=[]
    for category in categories:
        ctg.append({"id":category.id,
                    "name":category.name})
    return JsonResponse({"categories":ctg})
def categories_store(request):
    name = request.POST["categories"]
    if len(models.Category.objects.filter(name = name))==0:
        models.Category.objects.create(name = name)
        return JsonResponse({"message":"saved"})
    else:
        return JsonResponse({"message":"error"})
def categories_delete(request,id):
    categories = models.Category.objects.get(id=id)
    products = models.Product.objects.filter(categories = categories)
    if len(products) == 0:
        categories.delete()
        return JsonResponse({"error":False,"message":"success"})
    else:
        return JsonResponse({"error":True,"message":"category is alreaady in use"})
def products_get_data(request):
    products = models.Product.objects.all()
    prd=[]
    for product in products:
        ctg=[]
        for category in product.categories.all():
            ctg.append(category.name)
        prd.append({"id":product.id,
                    "name":product.name,
                    "price":product.price,
                    "brand":product.brand.name,
                    "categories":ctg})
    return JsonResponse({"products":prd})
def products_store(request):
    name = request.POST["name"]
    price = request.POST["price"]
    br = request.POST["brand"]
    products = models.Product.objects.create(name=name,price=price,brand = models.Brand.objects.get(id=br))
    categories = request.POST.getlist("categories")
    for category in categories:
            products.categories.add(models.Category.objects.get(id=category))
    products.save()
    return JsonResponse({"message":"saved"}) 
def products_delete(request,id):
    products = models.Product.objects.filter(id=id)
    products.delete()
    return JsonResponse({"message":"success"})
def brands_edit(request,id):
    brands = models.Brand.objects.get(id=id)
    content={"id":brands.id,
             "name":brands.name}
    return JsonResponse(content)
def products_edit(request,id):
    return render(request,"product.html")
def products_get_one(request):
    products = models.Product.objects.get(id=request.POST["id"])
    ctg=[]
    for category in products.categories.all():
        ctg.append(category.name)
    content={"id":products.id,
             "name":products.name,
             "price":products.price,
             "brand":products.brand.id,
             "categories":ctg}
    return JsonResponse(content)
def categories_edit(request,id):
    categories = models.Category.objects.get(id=id)
    content={"id":categories.id,
             "name":categories.name}
    return JsonResponse(content)
def customers_edit(request,id):
    customers = models.Customers.objects.get(id=id)
    content={"id":customers.id,
             "name":customers.name,
             "family":customers.family,
             "birth_year":customers.birth_year,
             "ssn":customers.ssn,
             "tel":customers.tel,
             "address":customers.address}
    return JsonResponse(content)
def sellers_edit(request,id):
    sellers = models.Seller.objects.get(id=id)
    content={"id":sellers.id,
             "name":sellers.name,
             "address":sellers.address}
    return JsonResponse(content)
def brands_index(request):
    return render(request,"brands.html")
def customers_index(request):
    return render(request,"customers.html")
def sellers_index(request):
    return render(request,"sellers.html")
def categories_index(request):
    return render(request,"categories.html")
def products_index(request):
    return render(request,"products.html")
def products_form(request):
    return render(request,"product.html")