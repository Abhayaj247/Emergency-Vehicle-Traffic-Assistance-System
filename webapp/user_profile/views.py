from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.shortcuts import redirect, reverse
from user_profile.forms import UserProfileModelForm, UserDetailModelForm


# Create your views here.


class UserProfileView(TemplateView, LoginRequiredMixin):
    template_name = "user_profile/profile.html"

    def post(self, request, *args, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user_profile_form'] = user_profile_form = UserProfileModelForm(request.POST, request.FILES,
                                                                                instance=request.user.user_profile)
        context['user_detail_form'] = user_detail_form = UserDetailModelForm(request.POST,
                                                                             instance=request.user)
        if user_profile_form.is_valid() and user_detail_form.is_valid():
            user_profile_form.save()
            user_detail_form.save()
            return redirect(reverse('profile'))
        else:
            print(user_profile_form.errors, "++++++")

        return render(request, self.template_name, context=context)

    def get(self, request, *args, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['user_profile_form'] = UserProfileModelForm(instance=request.user.user_profile)
        context['user_detail_form'] = UserDetailModelForm(instance=request.user)
        return render(request, self.template_name, context=context)


class UserStatusView(TemplateView, LoginRequiredMixin):
    template_name = "user_profile/status.html"

def home2(request):
    return render(request, 'home2/home2.html')

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Patient

def save_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        blood_group = request.POST.get('blood_group')
        age = request.POST.get('age')
        details = request.POST.get('details')

        # Create a new patient object
        patient = Patient(
            name=name,
            blood_group=blood_group,
            age=age,
            details=details
        )

        # Save the patient object to the database
        patient.save()

        # Redirect to a success page
        return HttpResponse('done')

    # If the request is not POST, render a template with a form to input patient details
    return render(request, 'home2/patient_form.html')

import cv2
import cv2
import numpy as np
import os

def emergency_detection(request):
    cap = cv2.VideoCapture('emergencyv.mp4')
    while True:
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.4)
            cv2.imshow('Video', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()
    return HttpResponse('done')
