# Automated Grading

This is sample code for automating some grading steps. For full use, you'll have to put this in a loop and send the scores to some kind of grade file. 

This can be used for complete automation of multiple choice exams. 

For coding, I just provide some simple function output and make no attempt at assigning a numerical score automatically. In practice, I would just use this for quick reference when grading by hand and provide additional comments in a separate file. 

Shout out to [William Gosset](https://en.wikipedia.org/wiki/William_Sealy_Gosset) as the sample student here. 

## Extensions
Use [pydrive](https://pythonhosted.org/PyDrive/) to send output directly and privately to a student.  

```
from pydrive.auth import GoogleAuth
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
from pydrive.drive import GoogleDrive
drive = GoogleDrive(gauth)

email_suffix = '@school.edu'
id_list = ['alexanderthclark']
grade_folder = 'folder_id_string'

for key, uni in enumerate(id_list):    
    # create folder if it doesn't already exist
    # if folder already exists, replace this with finding the folder under the parent folder
    student_folder = drive.CreateFile({'title': uni, 'parents':[ {'id': grade_folder}], 
                                       'mimeType': 'application/vnd.google-apps.folder'})
    student_folder.Upload()
    
    # make permissions
    new_perms = {
      'emailAddress': uni + suffix,
        'value': uni + suffix,
      'role': 'reader',
      'type': 'user'}
    student_folder.InsertPermission(new_perms)
    # delete other permissions if necessary ... 
    
    ## add file
    fname = f'{uni}_grade_report.pdf'
    file = drive.CreateFile({'title':'midterm_report','parents': [{'id': student_folder['id']}]})
    file.SetContentFile(fname)
    file.Upload()
   ```
