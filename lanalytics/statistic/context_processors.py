from models import Site


def lanalytic_sites_amount(request):
    try:
        amount = request.user.lanalytic_sites.count()
    except:
        amount = 0

    return {
    'lanalytic_sites': amount,
    }
