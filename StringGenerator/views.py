import os

import cv2
import numpy as np
from django.shortcuts import render
from django.views import View
from .models import Strings


def create_video_opencv(message: str):
    if len(message) > 50:
        title = message[:50]
    else:
        title = message
    width, height = 1920, 1000
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    out = cv2.VideoWriter(f"Static/img/{title}.mp4", fourcc, 24, (width, height))
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 10
    font_thickness = 10
    font_color = (255, 255, 255)
    message_size = cv2.getTextSize(message, font, font_scale, font_thickness)
    x, y = width, height // 2
    while True:
        frame.fill(0)
        x -= 30
        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)
        out.write(frame)
        if x + message_size[0][0] < 0:
            break
    out.release()
    return f"Static/img/{title}.mp4"


class StringGeneratorView(View):
    template_name = 'StringGenerator/string_gen.html'

    def get(self, request):
        if request.GET.get('std'):
            Strings.objects.filter(name=request.GET.get('std')).delete()
            os.remove(request.GET.get('std'))
        context = {}
        videos = Strings.objects.all()
        if videos:
            context = {"videos": videos}
        return render(request, self.template_name, context)

    def post(self, request):
        video = create_video_opencv(request.POST.get('msg'))
        if Strings.objects.filter(name=video):
            Strings.objects.filter(name=video).delete()
        Strings.objects.create(name=video)

        context = {"video": video}
        videos = Strings.objects.all()
        if videos:
            context["videos"] = videos[:len(videos) - 1]
        return render(request, self.template_name, context)
