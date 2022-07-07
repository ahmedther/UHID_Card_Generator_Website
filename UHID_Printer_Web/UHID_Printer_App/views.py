from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, FileResponse
from .oracle_config import Ora
from .card_generator import GenerateUHIDCard
import codecs
import io
import os
# Create your views here.


def index(request):
        
        
        if request.method == 'GET':
                
                return render(request,'UHID_Printer_App/index.html')
                
        elif request.method == 'POST':
                # Create a file-like buffer to receive PDF data.
                

                #assign uhid from user input
                uhid = (request.POST['uhid']).upper()
                #Show error if uhid is less the 12 characters
                if len(uhid) < 12:
                        return render(request,'UHID_Printer_App/index.html',{"error":"UHID Incomplete."})
                #search and get data from the database
                patient_details = []
                db = Ora()
                patient_details = db.get_patient_details(uhid)
                #Data to send on website
                if not patient_details:
                        return render(request,'UHID_Printer_App/index.html',{"error":f'This UHID ({uhid}) doesn''t exist in the database.\n'})
                
                patient_details = list(patient_details[0])

                #Filter data as per Printing Requirements for MAle and Female
                patient_name = "Name    :  " + patient_details[1]
                gender = ""
                if patient_details[2] == "M":
                        gender = "Sex       :  Male"

                elif patient_details[2] == "F":
                        gender = "Sex       :  Female"

                uhid = "UHID    :  " + patient_details[0]
                
                #file_location = "UHID_Printer_App\pdf\\" + patient_details[0] + ".pdf"
                file_location = "sample.pdf"
                #file = "aa.pdf"

                # Generate PDF file with barcode
                GenerateUHIDCard(filename=file_location,patient_name=patient_name,
                gender=gender,
                uhid=uhid)
                #filepath = os.path.join('UHID_Printer_App\pdf', 'sample.pdf')
                return FileResponse(open(file_location, 'rb'), content_type='application/pdf')
            
                
                
                
                
                
                
                
                #return FileResponse(buffer, as_attachment=True, filename=file)

                # try: 
                #         with codecs.open(file_location, 'r', encoding='utf-8',
                #         errors='ignore') as f:
                #                 file_data = f.read()

                #     # sending response 
                #                 response = HttpResponse(file_data, content_type='application/pdf')
                #                 response['Content-Disposition'] = 'attachment; filename="UHID_Printer_App\pdf\\" + {patient_details[0]} + ".pdf"'

                # except IOError:
                #     # handle file not exist case here
                #         response = HttpResponseNotFound('<h1>File not exist</h1>')

                #         return response
                #         return render(request,'UHID_Printer_App/index.html',)

                