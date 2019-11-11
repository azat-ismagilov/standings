from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Contest, Team, Participant, HandleInvoice
from django.contrib.auth.decorators import login_required


def index(request):
    try:
        contest = Contest.objects.all()[0]
    except:
        raise Http404("No contests available")
    codeforces_link = "https://codeforces.com/profile/"
    teams = contest.team_set.all()
    teams_sorted = sorted(teams, key=lambda t: t.get_rating(), reverse=True)
    return render(
        request,
        "index.html",
        context={
            "codeforces_link": codeforces_link,
            "contest": contest,
            "teams": teams_sorted,
        },
    )


from django.shortcuts import get_object_or_404
from django.urls import reverse

from .forms import AddParticipantHandleForm, UrlForm, FileForm


def add_handle(request, participant_id=None):
    if request.method == "POST":
        form = AddParticipantHandleForm(request.POST)

        if form.is_valid():
            if HandleInvoice.objects.count() > 10000:
                raise Http404("Too many invoices")
            participant = form.cleaned_data["participant"]
            codeforces_handle = form.cleaned_data["handle"]

            handleinvoice = HandleInvoice(
                participant=participant, handle=codeforces_handle
            )
            handleinvoice.save()

        return HttpResponseRedirect(reverse("add_handle_success"))
    else:
        try:
            participant = Participant.objects.get(id=participant_id)
        except:
            participant = None
        form = AddParticipantHandleForm(initial={"participant": participant})

    return render(request, "add_handle.html", {"form": form})


def add_handle_success(request):
    return render(request, "add_handle_success.html")


from .parser import (
    parse_contest,
    parse_contest_file,
    process_handles,
    process_handle,
    get_rating,
)


def success(request):
    return render(request, "success.html")


@login_required
def parse_teams(request):
    if request.method == "POST":
        form = UrlForm(request.POST)

        if form.is_valid():
            url = form.cleaned_data["url"]

            parse_contest(url)

        return HttpResponseRedirect(reverse("success"))
    else:
        form = UrlForm()

    return render(request, "form.html", {"form": form})


@login_required
def parse_teams_file(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            parse_contest_file(request.FILES['file'])
            return HttpResponseRedirect(reverse("success"))
    else:
        form = FileForm()

    return render(request, "form.html", {"form": form})


@login_required
def parse_rating(request):
    process_handles()
    return HttpResponseRedirect(reverse("success"))


@login_required
def process_invoices(request):
    try:
        handleinvoice = HandleInvoice.objects.all()[0]
        return render(
            request,
            "invoice.html",
            context={
                "profile": process_handle(handleinvoice.handle),
                "handleinvoice": handleinvoice,
            },
        )
    except IndexError:
        return HttpResponseRedirect(reverse("success"))


from .models import HandleInvoice
from django.core.exceptions import ObjectDoesNotExist


@login_required
def process_invoices_accept(request, handleinvoice_id):
    try:
        handleinvoice = HandleInvoice.objects.get(id=handleinvoice_id)
        handle = handleinvoice.handle
        participant = handleinvoice.participant
        participant.codeforces_handle = handle
        participant.codeforces_rating = get_rating(handle)
        participant.save()
        handleinvoice.delete()
    except ObjectDoesNotExist:
        pass
    return HttpResponseRedirect(reverse("process_invoices"))


@login_required
def process_invoices_decline(request, handleinvoice_id):
    try:
        handleinvoice = HandleInvoice.objects.get(id=handleinvoice_id)
        handleinvoice.delete()
    except ObjectDoesNotExist:
        pass
    return HttpResponseRedirect(reverse("process_invoices"))
