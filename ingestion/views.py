from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Breathe ESG Home</h1>")

def sap(request):
    if request.GET.get("csvfile"):
        filename = request.GET.get("csvfile")
        return HttpResponse(f"""
        <h1>SAP Upload Successful</h1>
        <h2>Selected File: {filename}</h2>
        <a href="/sap/">Upload Another File</a>
        """)

    return HttpResponse("""
    <h1>SAP Upload Page</h1>
    <form method="get" enctype="multipart/form-data">
        <input type="file" name="csvfile">
        <button type="submit">Upload CSV</button>
    </form>
    """)

def utility(request):
    if 'csvfile' in request.GET:
        filename = request.GET['csvfile']
        return HttpResponse(f"""
        <h1>Utility Upload Successful</h1>
        <h2>Selected File: {filename}</h2>
        <a href="/utility/">Upload Another File</a>
        """)

    return HttpResponse("""
    <h1>Utility Upload Page</h1>
    <form method="get" enctype="multipart/form-data">
        <input type="file" name="csvfile">
        <button type="submit">Upload CSV</button>
    </form>
    """)


def travel(request):
    if 'csvfile' in request.GET:
        filename = request.GET['csvfile']
        return HttpResponse(f"""
        <h1>Travel Upload Successful</h1>
        <h2>Selected File: {filename}</h2>
        <a href="/travel/">Upload Another File</a>
        """)

    return HttpResponse("""
    <h1>Travel Upload Page</h1>
    <form method="get" enctype="multipart/form-data">
        <input type="file" name="csvfile">
        <button type="submit">Upload CSV</button>
    </form>
    """)