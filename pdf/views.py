from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io


# View function for form submission
def accept(request):
    if request.method == 'POST':
        # Get data from the POST request
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        summary = request.POST.get('summary', '')
        degree = request.POST.get('degree', '')
        school = request.POST.get('school', '')
        university = request.POST.get('university', '')
        work = request.POST.get('work', '')
        skills = request.POST.get('skills', '')

        # Create a Profile object with the obtained data
        profile = Profile(
            name=name, email=email, phone=phone, summary=summary,
            degree=degree, school=school, university=university, work=work,
            skills=skills
        )

        # Save the Profile object to the database
        profile.save()

        # Redirect to success page
        return render(request, 'pdf/success.html')

    return render(request, 'pdf/accept.html')


# Retrieve the user profile and generate pdf
def cv(request, user_id):
    user_profile = Profile.objects.get(pk=user_id)
    template = loader.get_template('pdf/cv.html')
    html = template.render({'user_profile': user_profile})
    options = {
        'encoding': 'UTF-8',
        'page-size': 'Letter',
    }
    pdf = pdfkit.from_string(html, False, options=options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = ('attachment; filename="{}".pdf'
                                       .format(user_profile.name))

    return response


def cv_list(request):
    all_cv = Profile.objects.all()
    return render(request, 'pdf/list.html', {'cv': all_cv})
